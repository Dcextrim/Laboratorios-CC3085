from numpy import *

class FormulasParaMR:

    #Root Mean Squared Error
    def RMSE(self, y_real, y_pred):
        error = array(y_real) - array(y_pred)
        pot = error **2
        prom = mean(pot)
        totalRMSE = sqrt(prom)
        return totalRMSE
    
    #Mean Absolute Error
    def MAE(self, y_real, y_pred):
        error = array(y_real) - array(y_pred)
        error_abs = abs(error)
        totalMAE = mean(error_abs)
        return totalMAE