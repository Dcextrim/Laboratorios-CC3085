## Laboratorio #6 - Inteligencia Artificial (CC3085)

### Equipo
- **Dulce Ambrosio** - 231143
- **Daniel Chet** - 231177
- **Gadiel Ocaña** - 231270

### Descripción
Se implementó el juego **Connect Four (Conecta 4)** y un agente basado en **búsqueda adversaria** usando **Minimax** y **Poda Alfa‑Beta**. El agente evalúa estados no terminales con una heurística `evaluate(board)` (ventanas de 4 y preferencia por el centro) y selecciona movimientos óptimos aproximados con profundidad limitada.

### Contenido

- **`Lab6.ipynb`** — Notebook principal con la implementación completa.

---

### Task 2.1 — Diseño del juego (Connect Four)

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

### Task 2.2 — Minimax y Poda Alfa‑Beta

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

### Task 2.3 — Heurística `evaluate(board)`

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

### Ejecución (Notebook)

En `Lab6.ipynb`:

1. Ejecutar las celdas en orden (define tablero, Minimax/Alfa‑Beta y heurística).
2. Se incluye una prueba que imprime nodos visitados por Minimax y por Alfa‑Beta.
3. Al final hay dos partidas:
	- **IA vs Agente Aleatorio** (`play_game(vs_random=True)`)
	- **IA vs Humano** (`play_game(vs_random=False)`), que solicita entradas por consola dentro del notebook.

