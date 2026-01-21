from Formulas import *

formulas = FormulasParaMR()

y_real = [100,150,200,250,300]
y_pred = [110,140,210,240,500]

print ("Bienvenido a la Tarea 3 - Métricas de Desempeño")

rmse = formulas.RMSE(y_real, y_pred)
mae = formulas.MAE(y_real, y_pred)

print("El valor de RMSE es: ", round(rmse, 2))
print("El valor de MAE es: ", round(mae, 2))

print("\n--- ANÁLISIS COMPARATIVO ---")
print("\n¿Cuál métrica penalizó más el error del último dato (500)?")
print("RMSE penalizó más porque eleva los errores al cuadrado, magnificando")
print("errores grandes (200² = 40,000 vs MAE que usa 200 directamente).\n")

print("¿Por qué es importante al predecir dosis de medicamentos?")
print("En medicina, errores grandes pueden ser fatales. RMSE penaliza fuertemente")
print("errores extremos que pondrían en riesgo la vida del paciente, mientras que")
print("MAE trata todos los errores linealmente, subestimando riesgos críticos.")
