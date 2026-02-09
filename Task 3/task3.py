import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


df = pd.read_csv("high_diamond_ranked_10min.csv")

# Variable objetivo
objetivo = "blueWins"


# Eliminación de columnas espejo / redundantes
# Idea: si una variable del lado rojo es simplemente el negativo
# o complemento del lado azul, usarla causaría redundancia
# y potencial data leakage (sabemos indirectamente info del rival).

columnas_a_eliminar = [
    col for col in df.columns
    if col.startswith("red")
]

df_limpio = df.drop(columns=columnas_a_eliminar)

# Separación de features y target
X = df_limpio.drop(columns=[objetivo])
y = df_limpio[objetivo]

# Train / Test split 80/20
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
    )

# Escalado
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ¿Por qué SVM necesita escalado y los Árboles no?
# SVM calcula distancias y productos internos para definir márgenes
# y vectores de soporte. Si una variable tiene magnitudes mucho mayores
# que otra, dominará la función objetivo artificialmente.
#
# Los Árboles, en cambio, toman decisiones basadas en umbrales
# (x_j < c), no en distancias, por lo que el escalado no altera
# la estructura del árbol de forma significativa.


# SVM con Kernel Lineal
svm_lineal = SVC(
    kernel="linear",
    C=1.0,
    random_state=42
)

svm_lineal.fit(X_train_scaled, y_train)
pred_lineal = svm_lineal.predict(X_test_scaled)
acc_lineal = accuracy_score(y_test, pred_lineal)

# SVM con Kernel RBF
svm_rbf = SVC(
    kernel="rbf",
    C=1.0,
    gamma="scale",
    random_state=42
)

svm_rbf.fit(X_train_scaled, y_train)
pred_rbf = svm_rbf.predict(X_test_scaled)
acc_rbf = accuracy_score(y_test, pred_rbf)

print("Accuracy SVM Lineal:", acc_lineal)
print("Accuracy SVM RBF:", acc_rbf)

# Pregunta de análisis:
# Si el Kernel RBF funciona mejor (o igual),
# esto sugiere que la frontera entre partidas ganadas y perdidas
# NO es estrictamente lineal en el espacio original.
# El RBF proyecta los datos a un espacio de mayor dimensión
# donde una separación más compleja puede volverse lineal.



arbol = DecisionTreeClassifier(
    max_depth=3,  # limitado para visualización e interpretabilidad
    random_state=42
)

arbol.fit(X_train, y_train)
pred_arbol = arbol.predict(X_test)
acc_arbol = accuracy_score(y_test, pred_arbol)

print("Accuracy Árbol de Decisión:", acc_arbol)

# Visualización del árbol
plt.figure(figsize=(18, 8))
plot_tree(
    arbol,
    feature_names=X.columns,
    class_names=["Lose", "Win"],
    filled=True
)
plt.show()

# Feature Importance

importancias = pd.Series(
    arbol.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

top5 = importancias.head(5)


# ¿Tiene sentido para un jugador de LoL?
# Sí. Para un jugador es lógico que el oro sea más importante que los dragones
# al minuto 10, porque el oro da poder inmediato (objetos, stats),
# mientras que los dragones son ventajas acumulativas que impactan más tarde.
# Por eso el modelo prioriza oro/diferencias de oro sobre objetivos neutrales.

plt.figure(figsize=(8, 4))
top5.plot(kind="bar")
plt.title("Top 5 Features más importantes según el Árbol")
plt.ylabel("Importancia")
plt.show()

# Comentario conceptual:
# Si variables como goldDiff, dragons o heralds aparecen arriba,
# tiene sentido desde la lógica del juego:
# el oro representa poder inmediato,
# mientras que objetivos neutrales generan ventajas acumulativas.