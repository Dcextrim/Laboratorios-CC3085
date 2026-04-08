## Laboratorio #8 - Inteligencia Artificial (CC3085)

### Integrantes
- **Dulce Ambrosio** - 231143
- **Daniel Chet** - 231177
- **Gadiel Ocaña** - 231270

### Descripción
Este laboratorio modela un problema como **CSP (Constraint Satisfaction Problem)**: asignar **8 máquinas** (`M1..M8`) a **3 servidores** (`S1..S3`) cumpliendo restricciones.

Se implementan y comparan tres enfoques de búsqueda:

- **Búsqueda exacta**: **Backtracking Search** (DFS) con validación de restricciones y **forward checking** (lookahead).
- **Búsqueda aproximada**: **Beam Search** con una función heurística de “peso” basada en el número de violaciones.
- **Búsqueda local**: **ICM (Iterated Conditional Modes)**, iniciando desde una asignación aleatoria y mejorando iterativamente.

Finalmente, se realiza un **benchmarking** simple midiendo tiempos y verificando validez de las soluciones.

### Contenido
- **`Lab8.ipynb`** — Notebook principal con la implementación completa (CSP + Backtracking + Beam Search + Local Search/ICM + benchmarking).

---

## Parte A — Definición del CSP

El problema se representa con:

- **Variables**: máquinas `M1..M8`.
- **Dominios**: servidores posibles `S1`, `S2`, `S3` para cada máquina.
- **Restricciones**:
  - **Capacidad**: cada servidor puede alojar **máximo 3 máquinas**.
  - **Anti-afinidad**: ciertos pares no pueden quedar en el mismo servidor:
    - (`M1`, `M2`), (`M3`, `M4`), (`M5`, `M6`), (`M1`, `M5`).

La consistencia de una asignación parcial se valida con `is_valid(assignment, var, value)`.

---

## Parte B — Algoritmos

### Task 2.1 — Backtracking Search

Se implementa `backtracking(assignment, domains)` con el patrón:

1. Elegir la siguiente variable no asignada.
2. Probar valores del dominio.
3. Verificar restricciones (capacidad + anti-afinidad).
4. Aplicar **forward checking** (`forward_check`) para podar dominios futuros.
5. Recursión DFS y backtrack cuando no hay extensiones válidas.

Este enfoque es **exacto** (si existe solución, la encuentra), pero su costo puede crecer exponencialmente.

### Task 2.2 — Beam Search

Se implementa `beam_search(K)` manteniendo un conjunto (beam) de hasta `K` asignaciones parciales en cada paso:

- **EXTEND**: generar candidatos extendiendo las asignaciones actuales.
- **PRUNE**: ordenar por `compute_weight` y quedarse con los mejores `K`.

La función `compute_weight(assignment)` penaliza violaciones a capacidad y anti-afinidad (menos violaciones → mayor peso).

### Task 2.3 — Local Search (ICM)

Se implementa `local_search_icm(max_iters)`:

- Inicia desde una asignación completa aleatoria (`random_assignment`).
- Recorre variable por variable, eligiendo el valor del dominio que **maximiza** el peso (`compute_weight`).
- Solo acepta cambios que mejoren la solución, por lo que converge (pero puede caer en óptimos locales).

---

## Parte C — Benchmarking y conclusiones

Se mide el tiempo de ejecución de:

- Backtracking
- Beam Search (con `K=3`)
- ICM (con un límite de iteraciones)

Además, se valida la solución final con `is_solution_valid(solution)` para comparar enfoques exactos vs aproximados.

---

## Ejecución (Notebook)

En `Lab8.ipynb`:

1. Ejecutar celdas en orden (definición de CSP y restricciones).
2. Ejecutar **Task 2.1** para obtener una solución por Backtracking.
3. Ejecutar **Task 2.2** para obtener una solución por Beam Search.
4. Ejecutar **Task 2.3** para obtener una solución por ICM.
5. Ejecutar **Task 2.4** para correr el benchmarking (tiempos + validez + peso).

