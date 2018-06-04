# -*- coding: utf-8 -*-
"""
Plot difference between conditions.

Plot median of between stimulus conditions difference, with bootstrapped
confidence intervals (percentile bootstrap).
"""

# Part of py_depthsampling library
# Copyright (C) 2018  Ingo Marquardt
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.


from py_depthsampling.boot.boot_plot_diff import boot_plot
# from py_depthsampling.boot.boot_plot_diff_sngl_sub import boot_plot_sngl

# -----------------------------------------------------------------------------
# *** Define parameters

# Which draining model to plot ('' for none):
lstMdl = ['_deconv_model_1']  # ['', '_deconv_model_1']

# Meta-condition (within or outside of retinotopic stimulus area):
lstMetaCon = ['stimulus']  # ['stimulus', 'periphery']

# ROI ('v1' or 'v2'):
lstRoi = ['v1', 'v2']

# Hemisphere ('rh' or 'lh'):
lstHmsph = ['rh']  # ['lh', 'rh']

# Path for corrected depth-profiles (meta-condition, ROI, hemisphere,
# condition, and model index left open):
strPthData = '/home/john/PhD/PacMan_Depth_Data/Higher_Level_Analysis/{}/{}_{}_{}{}.npy'  #noqa

# Output path & prefix for plots (meta-condition, ROI, ROI, hemisphere, and
# model index left open):
strPthPltOt = '/home/john/PhD/PacMan_Plots/boot_diff/{}/{}/{}_{}{}'  #noqa

# Output path for single subject plot (heatmap), (ROI, metacondition,
# hemisphere, drain model, and condition left open):
# sttPthPtlSnglOt = '/home/john/PhD/PacMan_Plots/boot_diff_sngle/{}_{}_{}{}_{}'

# File type suffix for plot:
strFlTp = '.png'

# Figure scaling factor:
varDpi = 80.0

# Label for axes:
strXlabel = 'Cortical depth level (equivolume)'
strYlabel = 'fMRI signal change [arbitrary units]'

# Condition levels (used to complete file names):
lstCon = ['Pd_sst', 'Cd_sst', 'Ps_sst']

# Condition labels:
# lstConLbl = ['PacMan Dynamic Sustained',
#              'Control Dynamic Sustained',
#              'PacMan Static Sustained']
lstConLbl = ['Pd_sst', 'Cd_sst', 'Ps_sst']

# Which conditions to compare (list of tuples with condition indices):
lstDiff = [(0, 1), (0, 2)]

# Number of resampling iterations for peak finding (for models 1, 2, and 3) or
# random noise samples (models 4 and 5):
# varNumIt = 10000

# Lower & upper bound of percentile bootstrap (in percent), for bootstrap
# confidence interval (models 1, 2, and 3) - this value is only printed, not
# plotted - or plotted confidence intervals in case of model 5:
# varCnfLw = 0.5
# varCnfUp = 99.5
varCnfLw = 2.5
varCnfUp = 97.5
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# *** Loop through ROIs / conditions

# Loop through models, ROIs, hemispheres, and conditions to create plots:
for idxMtaCn in range(len(lstMetaCon)):  #noqa
    for idxMdl in range(len(lstMdl)):  #noqa
        for idxRoi in range(len(lstRoi)):
            for idxHmsph in range(len(lstHmsph)):

                # Limits of axes need to be adjusted based on ROI,
                # condition, hemisphere.

                if idxRoi == 0:  # v1

                    if lstMetaCon[idxMtaCn] == 'stimulus':
                        if lstMdl[idxMdl] == '':
                            varYmin = -50.0
                            varYmax = 50.0
                        if lstMdl[idxMdl] == '_deconv_model_1':
                            varYmin = -50.0
                            varYmax = 50.0
                    if lstMetaCon[idxMtaCn] == 'periphery':
                        if lstMdl[idxMdl] == '':
                            varYmin = -50.0
                            varYmax = 50.0
                        if lstMdl[idxMdl] == '_deconv_model_1':
                            varYmin = -50.0
                            varYmax = 50.0

                elif idxRoi == 1:  # v2

                    if lstMetaCon[idxMtaCn] == 'stimulus':
                        if lstMdl[idxMdl] == '':
                            varYmin = -50.0
                            varYmax = 50.0
                        if lstMdl[idxMdl] == '_deconv_model_1':
                            varYmin = -50.0
                            varYmax = 50.0
                    if lstMetaCon[idxMtaCn] == 'periphery':
                        if lstMdl[idxMdl] == '':
                            varYmin = -50.0
                            varYmax = 50.0
                        if lstMdl[idxMdl] == '_deconv_model_1':
                            varYmin = -50.0
                            varYmax = 50.0

                # Create average plots:
                boot_plot(strPthData.format(lstMetaCon[idxMtaCn],
                                            lstRoi[idxRoi],
                                            lstHmsph[idxHmsph],
                                            '{}',
                                            lstMdl[idxMdl]),
                          (strPthPltOt.format(lstMetaCon[idxMtaCn],
                                              lstRoi[idxRoi],
                                              lstRoi[idxRoi],
                                              lstHmsph[idxHmsph],
                                              lstMdl[idxMdl])
                           + strFlTp),
                          lstCon,
                          lstConLbl,
                          varNumIt=10000,
                          varConLw=varCnfLw,
                          varConUp=varCnfUp,
                          strTtl='',
                          varYmin=varYmin,
                          varYmax=varYmax,
                          strXlabel='Cortical depth level (equivolume)',
                          strYlabel='Difference score',
                          lgcLgnd=True,
                          lstDiff=lstDiff)

            # Create single subject plot(s):
            # boot_plot_sngl(strPthData.format(lstMetaCon[idxMtaCn],
            #                                  lstRoi[idxRoi],
            #                                  lstHmsph[idxHmsph],
            #                                  '{}',
            #                                  lstMdl[idxMdl]),
            #                (sttPthPtlSnglOt.format(lstRoi[idxRoi],
            #                                        lstMetaCon[idxMtaCn],
            #                                        lstHmsph[idxHmsph],
            #                                        lstMdl[idxMdl],
            #                                        '{}')
            #                 + strFlTp),
            #                lstCon,
            #                lstConLbl,
            #                strXlabel='Cortical depth level (equivolume)',
            #                strYlabel='Subject',
            #                lstDiff=lstDiff)
# -----------------------------------------------------------------------------