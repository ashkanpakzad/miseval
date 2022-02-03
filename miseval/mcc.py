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
import math
# Internal modules
from miseval.confusion_matrix import calc_ConfusionMatrix

#-----------------------------------------------------#
#     Calculate : Matthews Correlation Coefficient    #
#-----------------------------------------------------#
"""
References:
    Chicco, D., Jurman, G. The advantages of the Matthews correlation coefficient
    (MCC) over F1 score and accuracy in binary classification evaluation.
    BMC Genomics 21, 6 (2020). https://doi.org/10.1186/s12864-019-6413-7
"""
def calc_MCC(truth, pred, c=1):
    # Obtain confusion mat
    tp, tn, fp, fn = calc_ConfusionMatrix(truth, pred, c)
    # Compute mcc
    top = tp*tn - fp*fn
    bot_raw = (tp+fp) * (tp+fn) * (tn+fp) * (tn+fn)
    bot = math.sqrt(bot_raw)
    if bot != 0 : mcc = top / bot
    else : mcc = 0.0
    # Return mcc score
    return mcc

# MCC normalized
# MCC approximated
