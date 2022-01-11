#==============================================================================#
#  Author:       Dominik Müller                                                #
#  Copyright:    2022 IT-Infrastructure for Translational Medical Research,    #
#                University of Augsburg                                        #
#                                                                              #
#  This program is free software: you can redistribute it and/or modify        #
#  it under the terms of the GNU General Public License as published by        #
#  the Free Software Foundation, either version 3 of the License, or           #
#  (at your option) any later version.                                         #
#                                                                              #
#  This program is distributed in the hope that it will be useful,             #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of              #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
#  GNU General Public License for more details.                                #
#                                                                              #
#  You should have received a copy of the GNU General Public License           #
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
#==============================================================================#
#-----------------------------------------------------#
#                   Library imports                   #
#-----------------------------------------------------#
# External modules
import numpy as np
# Internal modules
from miseval.confusion_matrix import calc_ConfusionMatrix

#-----------------------------------------------------#
#           Calculate : Sensitivity via Sets          #
#-----------------------------------------------------#
def calc_Sensitivity_Sets(truth, pred, c=1):
    # Obtain sets with associated class
    gt = np.equal(truth, c)
    pd = np.equal(pred, c)
    # Calculate sensitivity
    if gt.sum() != 0 : sens = np.logical_and(pd, gt).sum() / gt.sum()
    else : sens = 0.0
    # Return sensitivity
    return sens

#-----------------------------------------------------#
#            Calculate : Sensitivity via CM           #
#-----------------------------------------------------#
def calc_Sensitivity_CM(truth, pred, c=1):
    # Obtain confusion matrix
    tp, tn, fp, fn = calc_ConfusionMatrix(truth, pred, c)
    # Calculate sensitivity
    if (tp + fn) != 0 : sens = (tp) / (tp + fn)
    else : sens = 0.0
    # Return sensitivity
    return sens
