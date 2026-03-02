## Hoja de Trabajo 2 - Inteligencia Artificial (CC3085)

### Equipo
- **Daniel Chet** - 231177
- **Dulce Ambrosio** - 231143
- **Gadiel Ocaña** - 231270

### Descripción
En el Task 2 se modeló el entorno Frozen Lake como un MDP estocástico, definiendo estados, acciones, función de transición con deslizamiento (1/3 de probabilidad por dirección) y función de recompensa, utilizando un factor de descuento y = 0.9.

Se implementó el algoritmo de Value Iteration para calcular el valor óptimo V*(s) y posteriormente extraer la política óptima 𝜋*(s). El mapa de calor resultante muestra que los estados más cercanos al Goal son los más valiosos, mientras que los estados Hole tienen valor cero, confirmando el correcto funcionamiento del modelo y del algoritmo.

### Contenido

- **`Hoja2.ipynb`** — Notebook principal con la implementación completa.

---

### Task 2.1 — Modelado del MDP

Se implementó la clase `FrozenLakeMDP` que representa el entorno Frozen Lake en una cuadrícula 4×4:

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
| **Acciones** | 4 acciones: Norte (↑), Sur (↓), Este (→), Oeste (←) |
| **Transiciones** | Estocásticas: 1/3 de probabilidad para la acción elegida y cada perpendicular |
| **Recompensa** | +1.0 al llegar al Goal (G), 0.0 en cualquier otro caso |
| **Factor de descuento** | γ = 0.9 |
| **Estados terminales** | Holes (H) y Goal (G) — desde estos no hay transiciones |

La función `get_transitions(state, action)` retorna la lista de `(probabilidad, siguiente_estado)` teniendo en cuenta el deslizamiento del hielo: si la acción elegida es Norte/Sur, las perpendiculares son Este/Oeste, y viceversa.

---

### Task 2.2 — Algoritmo de Iteración de Valores (Value Iteration)

Se implementó Value Iteration partiendo de V₀(s) = 0 para todos los estados, iterando hasta convergencia con ε = 1×10⁻⁶:

$$V^*(s) = \max_a \sum_{s'} P(s' \mid s, a)\left[R(s, a, s') + \gamma V^*(s')\right]$$

Una vez obtenidos los valores óptimos, se extrae la política óptima π*(s) seleccionando la acción de mayor valor esperado para cada estado:

$$\pi^*(s) = \arg\max_a \sum_{s'} P(s' \mid s, a)\left[R(s, a, s') + \gamma V^*(s')\right]$$

**Resultados:**

- La política óptima se visualiza como una cuadrícula 4×4 con las flechas de dirección (↑ ↓ → ←) y las etiquetas H/G en los estados terminales.
- El mapa de calor de V*(s) muestra que los estados más cercanos al Goal acumulan los valores más altos, mientras que los Holes y los estados alejados tienen valores cercanos a cero.

