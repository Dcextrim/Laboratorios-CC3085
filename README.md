## Laboratorio #5 - Inteligencia Artificial (CC3085)

### Equipo
- **Dulce Ambrosio** - 231143
- **Daniel Chet** - 231177
- **Gadiel Ocaña** - 231270

### Descripción
Se implementó el algoritmo de Q-Learning sobre el entorno `FrozenLake-v1` de Gymnasium, modelado como un Proceso de Decisión de Markov (MDP) estocástico. El agente aprende una política óptima interactuando con el entorno durante 10,000 episodios, utilizando una estrategia Epsilon-Greedy para balancear exploración y explotación.

### Contenido

- **`Lab5.ipynb`** — Notebook principal con la implementación completa.

---

### Task 2.1 — Preparación del entorno

Se utilizó la biblioteca `gymnasium` para crear el entorno `FrozenLake-v1` en una cuadrícula 4×4 con hielo resbaladizo (`is_slippery=True`), lo que lo convierte en un entorno estocástico.

```
S  F  F  F
F  H  F  H
F  F  F  H
H  F  F  G
```

**Componentes del MDP:**

| Componente | Descripción |
|---|---|
| **Estados** | 16 estados (0–15), numerados fila por fila |
| **Acciones** | 4 acciones: Izquierda (0), Abajo (1), Derecha (2), Arriba (3) |
| **Recompensa** | +1.0 al llegar al Goal (G), 0.0 en cualquier otro caso |
| **Estocástico** | `is_slippery=True` — el agente puede deslizarse en direcciones no deseadas |

---

### Task 2.2 — Implementación de Q-Learning

Se inicializó la Q-table con ceros y se entrenó el agente con los siguientes hiperparámetros:

| Hiperparámetro | Valor | Descripción |
|---|---|---|
| `alpha` | 0.1 | Learning rate — cuánto confiar en la nueva información |
| `gamma` | 0.99 | Factor de descuento — qué tanto se valoran las recompensas futuras |
| `epsilon` | 1.0 → 0.01 | Control de exploración vs. explotación (decae con `epsilon_decay = 0.999`) |
| `episodes` | 10,000 | Número de episodios de entrenamiento |

La actualización de la Q-table sigue la fórmula de Q-Learning:

$$Q(s, a) \leftarrow Q(s, a) + \alpha \left[ r + \gamma \max_{a'} Q(s', a') - Q(s, a) \right]$$

La estrategia **Epsilon-Greedy** selecciona una acción aleatoria con probabilidad ε (exploración) o la acción de mayor valor en la Q-table con probabilidad 1−ε (explotación).

---

### Visualización de la política

Una vez entrenado el agente, se extrae la política óptima derivada de la Q-table seleccionando la acción de mayor valor en cada estado:

$$\pi^*(s) = \arg\max_a Q(s, a)$$

La política se muestra como una cuadrícula 4×4 con símbolos de dirección (← ↓ → ↑).

---

### Mapa de calor de la Q-table

Se visualiza el valor máximo aprendido por estado (`max Q(s, a)`) como un mapa de calor 4×4, donde los estados más cercanos al Goal presentan los valores más altos, mientras que los Holes y estados alejados tienen valores cercanos a cero.

