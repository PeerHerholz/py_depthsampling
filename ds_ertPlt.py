# -*- coding: utf-8 -*-
"""
Function of the depth sampling pipeline.

Function of the event-related timecourses depth sampling sub-pipeline.
"""

# Part of py_depthsampling library
# Copyright (C) 2017  Ingo Marquardt
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.

import numpy as np  # noqa
import matplotlib.pyplot as plt
import matplotlib.colors as colors


def funcPltErt(aryRoiErtMeanDpth,  #noqa
               aryError,
               varNumDpth,
               varNumCon,
               varNumVol,
               varDpi,
               varYmin,
               varYmax,
               varStimStrt,
               varStimEnd,
               varTr,
               lstConLbl,
               lgcLgnd,
               strXlabel,
               strYlabel,
               lgcCnvPrct,
               strTitle,
               strPthOut):
    """Plot event-related timecourses."""
    # Create figure:
    fgr01 = plt.figure(figsize=(1200.0/varDpi, 800.0/varDpi),
                       dpi=varDpi)
    # Create axis:
    axs01 = fgr01.add_subplot(111)

    # Plot horizontal bar for stimulus interval (plot this one first so that it
    # is first in the legend):
    plot03 = plt.plot(((varStimStrt - 0.35), (varStimEnd + 0.35)),  #noqa
                      ((varYmin + 0.006), (varYmin + 0.006)),
                      color=(0.3, 0.3, 0.3),
                      linewidth=8.0,
                      label='Stimulus')

    # Vector for x-data:
    vecX = range(0, varNumVol)

    # Prepare colour map:
    objClrNorm = colors.Normalize(vmin=0, vmax=(varNumCon - 1))
    objCmap = plt.cm.winter

    # Loop through conditions:
    # for idxCon in range(0, varNumCon):
    for idxCon in [3, 2, 1, 0]:

        # Adjust the colour of current line:
        # vecClrTmp = objCmap(objClrNorm(varNumCon - 1 - idxCon))
        vecClrTmp = objCmap(objClrNorm(idxCon))

        # Plot timecourse for current condition:
        plt01 = axs01.plot(vecX,  #noqa
                           aryRoiErtMeanDpth[idxCon, :],
                           color=vecClrTmp,
                           alpha=0.9,
                           label=(lstConLbl[idxCon]),
                           linewidth=8.0,
                           antialiased=True)

        # Plot error shading:
        plot02 = axs01.fill_between(vecX,  #noqa
                                    np.subtract(aryRoiErtMeanDpth[idxCon, :],
                                                aryError[idxCon, :]),
                                    np.add(aryRoiErtMeanDpth[idxCon, :],
                                           aryError[idxCon, :]),
                                    alpha=0.4,
                                    edgecolor=vecClrTmp,
                                    facecolor=vecClrTmp,
                                    linewidth=0,
                                    # linestyle='dashdot',
                                    antialiased=True)

    # Plot horizontal bar for stimulus interval:
    # plot04 = plt.plot((0, 2),  #noqa
    #                  (0, 0),
    #                  color=(0.9, 0.1, 0.1),
    #                  linewidth=10.0,
    #                  label='Baseline')

    # Reduce framing box:
    axs01.spines['top'].set_visible(False)
    axs01.spines['right'].set_visible(False)
    axs01.spines['bottom'].set_visible(True)
    axs01.spines['left'].set_visible(True)

    # Set x-axis range:
    axs01.set_xlim([-0.5, (varNumVol - 0.5)])
    # Set y-axis range:
    axs01.set_ylim([varYmin, varYmax])

    # Which x values to label with ticks:
    axs01.set_xticks(vecX)
    # We convert the volume indicies ('0, 1, 2 ...') into seconds, with time
    # point zeros at stimulus onset (e.g. '-9.0, -6.0, -3.0, 0.0, 3.0, ...').
    # First, set the index of the volume of stimulus onset to zero:
    vecXlbl = np.subtract(np.array((vecX), dtype=np.float64),
                          varStimStrt)
    # Convert to seconds (multiply by volume TR):
    vecXlbl = np.multiply(vecXlbl, varTr)
    # Round:
    vecXlbl = np.around(vecXlbl, decimals=1)

    # Convert labels from float to list of strings:
    lstXlbl = map(str, vecXlbl)

    # Label every second volume:
    if False:
        # For better readibility, we would like to only label every second
        # volume, starting from the second volume. The label for every other
        # volume will be an empty string. Indicies of volumes to label with
        # empty sting:
        vecXlblIdx02 = np.arange(0, varNumVol, 2, dtype=np.int16)
        # Replace respective entries with empty strings:
        for idxLbl in vecXlblIdx02:
            lstXlbl[idxLbl] = ''
    # Label every third volume:
    if True:
        # Indicies of volumes NOT to label with emtpy string:
        vecXlblIdx02 = np.arange(0, varNumVol, 3, dtype=np.int16)
        # Replace respective entries with empty strings:
        for idxLbl in range(0, varNumVol):
            # Is the current volume index NOT in the vector of indicies NOT to
            # label with an empty string?
            if not (idxLbl in vecXlblIdx02):
                lstXlbl[idxLbl] = ''

    # Labels for x ticks:
    axs01.set_xticklabels(lstXlbl)

    # Which y values to label with ticks:
    # vecYlbl = np.linspace(varYmin, varYmax, num=4, endpoint=True)
    # vecYlbl = np.arange(varYmin, varYmax, 0.02)
    vecYlbl = np.linspace(0.0, varYmax, num=5, endpoint=True)
    # Round:
    # vecYlbl = np.around(vecYlbl, decimals=2)
    # Set ticks:
    axs01.set_yticks(vecYlbl)
    # Convert labels to percent?
    if lgcCnvPrct:
        # Multiply by 100 to convert to percent:
        vecYlbl = np.multiply(vecYlbl, 100.0)
        # Convert labels from float to a list of strings, with well-defined
        # number of decimals (including trailing zeros):
        lstYlbl = [None] * vecYlbl.shape[0]
        for idxLbl in range(vecYlbl.shape[0]):
            lstYlbl[idxLbl] = '{:0.1f}'.format(vecYlbl[idxLbl])
    else:
        # Convert labels from float to a list of strings, with well-defined
        # number of decimals (including trailing zeros):
        lstYlbl = [None] * vecYlbl.shape[0]
        for idxLbl in range(vecYlbl.shape[0]):
            lstYlbl[idxLbl] = '{:0.2f}'.format(vecYlbl[idxLbl])
    # Set tick labels for y ticks:
    axs01.set_yticklabels(lstYlbl)

    # Set x & y tick parameters:
    axs01.tick_params(labelsize=36,  # Fontsize
                      length=8,     # Height of the ticks
                      width=2,       # Width of the ticks
                      top='off',
                      right='off')

    # Adjust labels:
    axs01.set_xlabel(strXlabel,
                     fontsize=36)
    axs01.set_ylabel(strYlabel,
                     fontsize=36)

    # Adjust title:
    axs01.set_title(strTitle, fontsize=36)

    # Legend for axis 1:
    if lgcLgnd:
        axs01.legend(loc=0,
                     frameon=False,
                     prop={'size': 36})

    # Save figure:
    fgr01.savefig(strPthOut,
                  facecolor='w',
                  edgecolor='w',
                  orientation='landscape',
                  transparent=False,
                  frameon=None)

    # Close figure:
    plt.close(fgr01)