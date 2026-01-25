import pandas as pd
import numpy as np

np.random.seed(42)

edades = np.random.randint(18, 65, size=100)
salarios = np.random.randint(800, 5000, size=100)

compras = np.array([0]*90 + [1]*10)
np.random.shuffle(compras)

df = pd.DataFrame({
    "Edad": edades,
    "Salario": salarios,
    "Compró_Producto": compras
})

num_nan = int(0.10 * len(df))
indices_nan = np.random.choice(df.index, num_nan, replace=False)

for i in indices_nan:
    df.loc[i, "Edad"] = np.nan

suma_edades = 0
contador = 0

for edad in df["Edad"]:
    if not pd.isna(edad):
        suma_edades += edad
        contador += 1

promedio_edad = suma_edades / contador

for i in range(len(df)):
    if pd.isna(df.loc[i, "Edad"]):
        df.loc[i, "Edad"] = promedio_edad

# Usar el promedio para imputar valores faltantes puede ser una mala idea cuando existen valores extremos, ya que estos pueden desplazar el promedio y generar valores poco representativos; en esos casos, la mediana suele ser una mejor alternativa.

def undersampling_manual(dataframe):
    clase_0 = dataframe[dataframe["Compró_Producto"] == 0]
    clase_1 = dataframe[dataframe["Compró_Producto"] == 1]

    n_minoria = len(clase_1)

    clase_0_reducida = clase_0.sample(n=n_minoria, random_state=42)

    df_balanceado = pd.concat([clase_0_reducida, clase_1])
    df_balanceado = df_balanceado.sample(frac=1, random_state=42).reset_index(drop=True)

    return df_balanceado

df_balanceado = undersampling_manual(df)

print("Dataset original:", df.shape)
print("Dataset balanceado:", df_balanceado.shape)
print(df_balanceado["Compró_Producto"].value_counts())
