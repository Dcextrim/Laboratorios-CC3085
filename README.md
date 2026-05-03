## Laboratorio #10 - Inteligencia Artificial (CC3085)

### Integrantes
- **Dulce Ambrosio** - 231143
- **Daniel Chet** - 231177
- **Gadiel Ocaña** - 231270

### Descripción
Este laboratorio trabaja con **Redes Bayesianas e inferencia aproximada mediante Filtrado de Partículas**, aplicado al sistema de seguimiento de vehículos **LogiTrack**: un patio de 20 carriles (0–19) con sensores RFID ruidosos.

El laboratorio cubre dos grandes tareas:
- **Task 2**: Depuración de un filtro de partículas con un bug deliberado (remuestreo greedy en lugar de probabilístico).
- **Task 3**: Implementación completa desde cero, análisis experimental, detección de colapso y dictamen ejecutivo.

### Contenido
- **`Lab10.ipynb`** — Notebook principal con la implementación completa.

---

## Modelo del Sistema LogiTrack

- **Dominio**: 20 carriles discretos (0–19)
- **Dinámica de transición**: el vehículo se mueve ±1 carril o permanece en el mismo con probabilidad uniforme (1/3 cada opción); con reflexión en los bordes.
- **Modelo de sensor (emisión)**:
  - P(obs = h) = 0.6 (lectura correcta)
  - P(obs = h ± 1) = 0.2 c/u (carril adyacente)
  - Resto distribuido uniformemente entre los demás carriles

---

## Task 2 — Depuración del sistema con bug deliberado

Se analiza una implementación buggy del filtro de partículas donde el paso de remuestreo usa `np.argsort` para seleccionar deterministamente las K partículas con mayor peso (**Beam Search**), en lugar de muestreo probabilístico proporcional al peso.

- **Bug**: `idx = np.argsort(pesos_norm)[-K:]` — selección greedy, no estocástica.
- **Corrección**: `idx = np.random.choice(len(propuestas), size=K, replace=True, p=pesos_norm)` — remuestreo proporcional al peso.
- Se demuestra con una secuencia crítica (`[16,16,16,16,16,3,3,3,3]`) que el bug falla al adaptarse a cambios bruscos, y se verifica el caso de pesos uniformes donde ambas versiones son equivalentes.

---

## Task 3 — Implementación y Análisis

### Task 3.1 — Implementación base (K=5)

Implementación desde cero sin librerías de inferencia probabilística:

- `simular_vehiculo(pasos)`: genera trayectoria real oculta + observaciones ruidosas del sensor.
- `filtro_particulas(observaciones, K)`: algoritmo completo con los 3 pasos (proponer → ponderar → remuestrear probabilísticamente).
- `visualizar_simulacion(...)`: gráfica con trayectoria real, observaciones, estimación y nube de partículas.

### Task 3.2 — Análisis experimental

50 simulaciones independientes de 30 pasos cada una, comparando **K=5 vs K=20**:

- Gráfica de error promedio por paso (los primeros pasos tienen mayor error por inicialización uniforme).
- Identificación de las 5 peores simulaciones: el fallo se debe principalmente a la **cantidad insuficiente de partículas** (K=5), que provoca colapso cuando ninguna partícula queda cerca de la posición real.
- Tabla comparativa: K=20 reduce el error promedio en ~86% respecto a K=5.

### Task 3.3 — Detección de colapso

- **Métrica de diversidad**: varianza σ² de las partículas. Umbral: σ² < 2.0 (6% de la varianza uniforme teórica ≈ 33.25).
- `alerta_colapso(particulas, umbral)`: retorna flag de colapso + valor de σ².
- Tres escenarios demostrativos:
  1. **Sin colapso** — K=20, trayectoria gradual.
  2. **Colapso recuperable** — K=5, sensor erróneo durante 3 pasos; el filtro se recupera por la dispersión natural de la dinámica.
  3. **Colapso irrecuperable** — K=5, sensor sistemáticamente en zona opuesta; todas las partículas convergen a la región incorrecta de forma permanente.

### Task 3.4 — Dictamen ejecutivo

K=5 es insuficiente para uso operativo: el error supera los 7–10 carriles en ~12–18% de los escenarios. Se recomienda K ≥ 20 como mínimo, o mejorar la precisión del modelo de sensor si el hardware no lo permite.

---

## Ejecución

En `Lab10.ipynb`, ejecutar las celdas en orden:

1. **Task 2**: celdas de la versión buggy, corregida, tabla de errores y verificación de pesos.
2. **Task 3.1**: definición del modelo y visualización demo (K=5, 20 pasos).
3. **Task 3.2**: experimento con 50 simulaciones, gráficas y tabla comparativa.
4. **Task 3.3**: función `alerta_colapso` y los 3 escenarios de colapso.
5. **Task 3.4**: dictamen ejecutivo (celda markdown).
