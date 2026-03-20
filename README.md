## Laboratorio #7 - Inteligencia Artificial (CC3085)

### Equipo
- **Dulce Ambrosio** - 231143
- **Daniel Chet** - 231177
- **Gadiel Ocaña** - 231270

### Descripción
Se utiliza **Connect Four (Conecta 4)** como entorno y se integran dos enfoques de IA:

- **Búsqueda adversaria**: **Minimax** y **poda Alfa‑Beta**, con heurística `evaluate(board, piece)` (ventanas de 4 + preferencia por el centro).
- **Aprendizaje por refuerzo (TD Learning)**: agente **Q-Learning** (ε-greedy) entrenado contra un oponente aleatorio.

Además, se ejecuta una **competencia** entre agentes (TD vs Minimax, TD vs Alfa‑Beta, Minimax vs Alfa‑Beta), se muestran **partidas representativas** de forma visual y se genera una **gráfica** de resultados.

### Contenido

- **`Lab7.ipynb`** — Notebook principal con la implementación completa (Connect Four + Minimax/Alfa‑Beta + Q‑Learning + competencia + gráfica).

---

## Parte A — Base del juego (Connect Four) + búsqueda adversaria

### Task 2.1 (Lab6) — Diseño del juego (Connect Four)

Se modela el juego Conecta 4 en un tablero de **6×7** usando una matriz (`numpy`) con las siguientes constantes:

- `EMPTY = 0`
- `PLAYER = 1` (agente aleatorio o humano)
- `AI = 2` (agente que usa Alfa‑Beta)

**Representación y dinámica (MDP/juego adversario):**

| Componente | Descripción |
|---|---|
| **Estados** | Configuraciones del tablero `board` de tamaño 6×7 |
| **Acciones** | Elegir una columna válida `col ∈ {0..6}` donde la casilla superior esté vacía |
| **Transición** | `drop_piece(board, col, piece)` coloca la ficha en la fila disponible más baja |
| **Terminal** | `is_terminal(board)` cuando hay 4 en línea (jugador o IA) o no hay movimientos |
| **Recompensa** | Implícita vía función de utilidad: victoria/derrota/empate; no terminal via heurística |

La condición de victoria se detecta con `winning_move(board, piece)` revisando patrones:

- Horizontal
- Vertical
- Diagonales positiva y negativa

---

### Task 2.2 (Lab6) — Minimax y Poda Alfa‑Beta

Se implementan dos versiones para comparar:

- `minimax(board, depth, maximizing)`: Minimax clásico sin poda.
- `alphabeta(board, depth, alpha, beta, maximizing)`: Minimax optimizado con **poda Alfa‑Beta**.

Se contabiliza el número de nodos visitados (`nodes_minimax`, `nodes_alphabeta`) para evidenciar la reducción lograda por la poda.

**Idea clave de Alfa‑Beta:**

- `alpha`: mejor valor garantizado para MAX.
- `beta`: mejor valor garantizado para MIN.
- Si `alpha >= beta`, la rama se puede podar.

Cuando se llega a profundidad 0 o a un estado terminal, el algoritmo retorna una utilidad alta (victoria), baja (derrota), 0 (empate) o una estimación heurística del tablero.

---

### Task 2.3 (Lab6) — Heurística `evaluate(board, piece)`

Para estados no terminales, se define `evaluate(board, piece)` basada en:

- **Preferencia por el centro:** se bonifican fichas en la columna central.
- **Ventanas de 4:** se recorre el tablero (horizontal, vertical y diagonales) y se evalúa cada “window” con `evaluate_window(window, piece)`.

La ventana se puntúa (de forma resumida) así:

- 4 propias: +100
- 3 propias + 1 vacía: +5
- 2 propias + 2 vacías: +2
- 3 del oponente + 1 vacía: −4

Esta heurística guía la búsqueda con profundidad limitada para escoger una buena columna aun cuando no se alcance un estado terminal en el horizonte de búsqueda.

---

## Parte B — Aprendizaje por refuerzo (TD Learning / Q-Learning)

### Task 2.1 (Lab7) — Agente TD Learning (Q-Learning)

Se implementa un agente **Q-Learning** tabular (diccionario) para aprender una política en Conecta 4.

- **Estado**: `get_state(board)` aplana el tablero y lo convierte a `tuple(board.flatten())` para poder usarlo como llave.
- **Acción**: elegir una columna válida (mismo `get_valid_moves(board)`).
- **Selección de acción**: ε-greedy (`choose_action`).
- **Actualización**:
	- `Q(s,a) ← Q(s,a) + α [ r + γ max_a' Q(s',a') − Q(s,a) ]`
- **Recompensa** (`get_reward`) (resumen):
	- Victoria: +100
	- Derrota: −100
	- Empate: +10
	- Paso no terminal: penalización pequeña (−0.1) y bono si juega al centro.

El entrenamiento `train(episodes)` enfrenta al agente (pieza 1) contra un oponente aleatorio (pieza 2) y decae `epsilon` hasta `epsilon_min`.

---

### Task 2.2 (Lab7) — Competencia entre agentes

Se corren partidas automáticas (`play_match`) bajo tres condiciones (por defecto 50 partidas cada una):

- **Condición A**: TD Learning vs Minimax (sin poda)
- **Condición B**: TD Learning vs Minimax + Alfa‑Beta
- **Condición C (control)**: Minimax vs Minimax + Alfa‑Beta

Al final, se grafica la distribución de victorias/empates y se guarda un PDF: **`resultados_lab7.pdf`**.

---

### Task 2.3 (Lab7) — Partidas representativas (para video)

Se incluye una versión visual (`play_visual_match`) que imprime el tablero en cada turno con un `delay`, para grabar una partida representativa por condición:

- TD Learning vs Minimax
- TD Learning vs Alfa‑Beta
- Minimax vs Alfa‑Beta

---

### Ejecución (Notebook)

En `Lab7.ipynb`:

1. Ejecutar celdas en orden para definir el juego, Minimax/Alfa‑Beta y la heurística.
2. (Opcional) Ejecutar la celda de prueba de **nodos visitados** para comparar Minimax vs Alfa‑Beta.
3. Ejecutar el entrenamiento del agente TD (`train(100000)`).
   - Nota: 100,000 episodios puede tardar; se puede reducir para pruebas rápidas.
4. Ejecutar la **competencia** (condiciones A/B/C) y luego la celda de **gráfica** (genera `resultados_lab7.pdf`).
5. (Opcional) Ejecutar las **partidas representativas** con impresión visual para grabación.

