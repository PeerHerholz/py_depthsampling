# -*- coding: utf-8 -*-
"""
VTK depth samling across subjects.

The purpose of this script is to visualise cortical depth sampling results from
vtk files. The script can visualise statistical maps from vtk files. Vertices
are selected according to several criteria:

    (1) The vertex has to be contained within the ROI (as defined by by a csv
        file containing the indices of the ROI vertices, can be created with
        paraview based on a retinotopic map).
    (2) Selection criterion 2 -  vertices that are BELOW threshold at any depth
        levels are excluded. (For example, a venogram, or a T2* weighted EPI
        image with low intensities around veins that is defined at all depth
        level can be used.)
    (3) Selection criterion 3 - same as (2). Vertices that are BELOW threshold
        at any depth level are excluded.
    (4) Selection criterion 4 - same as (2). Vertices that are BELOW threshold
        at any depth level are excluded.
"""


from ds_main import ds_main


# *****************************************************************************
# *** Define parameters

# Region of interest ('v1' or 'v2'):
lstRoi = ['v1', 'v2']

# Hemispheres ('lh' or 'rh'):
lstHmsph = ['lh', 'rh']

# List of subject identifiers:
lstSubIds = ['20171023',
             '20171109',
             '20171204_01',
             '20171204_02',
             '20171211',
             '20171213',
             '20180111',
             '20180118']

# Condition levels (used to complete file names) - nested list:
lstNstCon = [['Pd', 'Cd', 'Ps'],
             ['Pd_min_Ps'],
             ['Pd_min_Cd']]

# Condition labels:
lstNstConLbl = [['PacMan Dynamic', 'Control Dynamic', 'PacMan Static'],
                ['PacMan D - PacMan S'],
                ['PacMan D - Control D']]

# Base path of vtk files with depth-sampled data, e.g. parameter estimates
# (with subject ID, hemisphere, and stimulus level left open):
strVtkDpth01 = '/media/sf_D_DRIVE/MRI_Data_PhD/05_PacMan/{}/cbs/{}/{}_pe1.vtk'

# (1)
# Restrict vertex selection to region of interest (ROI)?
lgcSlct01 = True
# Base path of csv files with ROI definition (i.e. patch of cortex selected on
# the surface, e.g. V1 or V2) - i.e. the first vertex selection criterion (with
# subject ID, hemisphere, and ROI left open):
strCsvRoi = '/media/sf_D_DRIVE/MRI_Data_PhD/05_PacMan/{}/cbs/{}/{}.csv'
# Number of header lines in ROI CSV file:
varNumHdrRoi = 1

# (2)
# Use vertex selection criterion 2 (vertices that are BELOW threshold are
# excluded - mean across depth levels):
lgcSlct02 = True
# Path of vtk files with for vertex selection criterion. This vtk file is
# supposed to contain one set of data values for each depth level. (With
# subject ID and hemisphere left open.)
strVtkSlct02 = '/media/sf_D_DRIVE/MRI_Data_PhD/05_PacMan/{}/cbs/{}/R2_multi.vtk'  #noqa
# Threshold for vertex selection:
varThrSlct02 = 0.1

# (3)
# Use vertex selection criterion 3 (vertices that are BELOW threshold are
# excluded - minimum across depth levels):
lgcSlct03 = True
# Path of vtk files with for vertex selection criterion. This vtk file is
# supposed to contain one set of data values for each depth level. (With
# subject ID and hemisphere left open.)
strVtkSlct03 = '/media/sf_D_DRIVE/MRI_Data_PhD/05_PacMan/{}/cbs/{}/combined_mean.vtk'  #noqa
# Threshold for vertex selection:
varThrSlct03 = 7000.0

# (4)
# Use vertex selection criterion 2 (vertices that are BELOW threshold are
# excluded - mean of absolute across depth levels):
lgcSlct04 = True
# Path of vtk files with for vertex selection criterion. This vtk file is
# supposed to contain one set of data values for each depth level. (With
# subject ID and hemisphere left open.)
strVtkSlct04 = '/media/sf_D_DRIVE/MRI_Data_PhD/05_PacMan/{}/cbs/{}/Pd_zstat1.vtk'  #noqa
# Threshold for vertex selection:
varThrSlct04 = 2.0

# Number of cortical depths:
varNumDpth = 11

# Beginning of string which precedes vertex data in data vtk files (i.e. in the
# statistical maps):
strPrcdData = 'SCALARS'

# Number of lines between vertex-identification-string and first data point:
varNumLne = 2

# Label for axes:
strXlabel = 'Cortical depth level (equivolume)'
strYlabel = 'fMRI signal [a.u.]'

# Output path for plots - prefix:
strPltOtPre = '/home/john/PhD/PacMan_Plots/pe/plots_{}/'

# Output path for plots - suffix:
strPltOtSuf = '_{}_{}_{}.png'

# Figure scaling factor:
varDpi = 80.0

# If normalisation - data from which input file to divide by?
# (Indexing starts at zero.) Note: This functionality is not used at the
# moment. Instead of dividing by a reference condition, all profiles are
# divided by the grand mean within subjects before averaging across subjects
# (if lgcNormDiv is true).
varNormIdx = 0

# Normalise by division?
lgcNormDiv = False

# Output path for depth samling results (within subject means):
strDpthMeans = '/home/john/PhD/PacMan_Depth_Data/Higher_Level_Analysis/{}_{}_{}.npy'  #noqa

# Maximum number of processes to run in parallel: *** NOT IMPLEMENTED
# varPar = 10
# *****************************************************************************


# *****************************************************************************
# *** Loop through ROIs / conditions

# Loop through ROIs, hemispheres, and conditions to create plots:
for idxRoi in range(len(lstRoi)):
    for idxHmsph in range(len(lstHmsph)):
        for idxCon in range(len(lstNstCon)):

            # Limits of axes need to be adjusted based on ROI, condition,
            # hemisphere.

            # Limits of y-axis for SINGLE SUBJECT PLOTS (list of tuples,
            # [(Ymin, Ymax)]):

            if idxRoi == 0:  # v1
                if idxCon == 0:  # v1 simple contrasts
                    lstLimY = [(-750.0, 25.0)] * len(lstSubIds)
                elif idxCon == 1:  # v1 Pd_min_Ps
                    lstLimY = [(-50.0, 50.0)] * len(lstSubIds)
                elif idxCon == 2:  # v1 Pd_min_Cd
                    lstLimY = [(-50.0, 50.0)] * len(lstSubIds)

            elif idxRoi == 1:  # v2
                if idxCon == 0:  # v2 simple contrasts
                    lstLimY = [(-500.0, 20.0)] * len(lstSubIds)
                elif idxCon == 1:  # v2 Pd_min_Ps
                    lstLimY = [(-50.0, 50.0)] * len(lstSubIds)
                elif idxCon == 2:  # v2 Pd_min_Cd
                    lstLimY = [(-50.0, 50.0)] * len(lstSubIds)

            # Limits of y-axis for ACROSS SUBJECT PLOTS:

            if idxRoi == 0:  # v1
                if idxCon == 0:  # v1 simple contrasts
                    # Limits of y-axis for across subject plot:
                    varAcrSubsYmin = -500.0
                    varAcrSubsYmax = 200.0
                elif idxCon == 1:  # v1 Pd_min_Ps
                    # Limits of y-axis for across subject plot:
                    varAcrSubsYmin = -70.0
                    varAcrSubsYmax = 70.0
                elif idxCon == 2:  # v1 Pd_min_Cd
                    # Limits of y-axis for across subject plot:
                    varAcrSubsYmin = -70.0
                    varAcrSubsYmax = 70.0

            elif idxRoi == 1:  # v2
                if idxCon == 0:  # v2 simple contrasts
                    # Limits of y-axis for across subject plot:
                    varAcrSubsYmin = -500.0
                    varAcrSubsYmax = 200.0
                elif idxCon == 1:  # v2 Pd_min_Ps
                    # Limits of y-axis for across subject plot:
                    varAcrSubsYmin = -70.0
                    varAcrSubsYmax = 70.0
                elif idxCon == 2:  # v2 Pd_min_Cd
                    # Limits of y-axis for across subject plot:
                    varAcrSubsYmin = -70.0
                    varAcrSubsYmax = 70.0

            # Title for mean plot:
            strTitle = lstRoi[idxRoi].upper()

            # Call main function:
            ds_main(lstRoi[idxRoi], lstHmsph[idxHmsph], lstSubIds,
                    lstNstCon[idxCon], lstNstConLbl[idxCon], strVtkDpth01,
                    lgcSlct01, strCsvRoi, varNumHdrRoi, lgcSlct02,
                    strVtkSlct02, varThrSlct02, lgcSlct03, strVtkSlct03,
                    varThrSlct03, lgcSlct04, strVtkSlct04, varThrSlct04,
                    varNumDpth, strPrcdData, varNumLne, strTitle, lstLimY,
                    varAcrSubsYmin, varAcrSubsYmax, strXlabel, strYlabel,
                    strPltOtPre.format(lstRoi[idxRoi]), strPltOtSuf.format(
                    lstHmsph[idxHmsph], lstRoi[idxRoi], lstNstCon[idxCon][0]),
                    varDpi, varNormIdx, lgcNormDiv, strDpthMeans.format(
                    lstRoi[idxRoi], lstHmsph[idxHmsph], lstNstCon[idxCon][0]))
# *****************************************************************************