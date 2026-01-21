from Formulas import *

formulas = FormulasParaMR()

y_real = [100,150,200,250,300]
y_pred = [110,140,210,240,500]

print ("Bienvenido a la Tarea 3 - Métricas de Desempeño")

rmse = formulas.RMSE(y_real, y_pred)
mae = formulas.MAE(y_real, y_pred)

print("El valor de RMSE es: ", round(rmse, 2))
print("El valor de MAE es: ", round(mae, 2))