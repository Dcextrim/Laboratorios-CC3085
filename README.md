## Laboratorio #9 - Inteligencia Artificial (CC3085)

### Integrantes
- **Dulce Ambrosio** - 231143
- **Daniel Chet** - 231177
- **Gadiel Ocaña** - 231270

### Descripción
Este laboratorio implementa inferencia básica en una Red Bayesiana usando el ejemplo clásico de Alarma con variables binarias:

- **B**: Robo
- **E**: Terremoto
- **A**: Alarma

Se define el modelo con priors raros usando ε = 0.01 para P(B=1) y P(E=1), y una CPT determinista para la alarma:

- A = B OR E

Luego se construye la distribución conjunta, se calcula inferencia marginal/condicional por marginalización y se demuestra el efecto “Explain Away” comparando probabilidades posteriores.

### Contenido
- **`Lab9.ipynb`** — Notebook principal con la implementación completa (distribución conjunta + inferencia marginal + explain away).

---

## Parte A — Modelo (Red Bayesiana)

- **Estructura**: `B → A ← E` (V-structure)
- **Factorización**: `P(B,E,A) = P(B) · P(E) · P(A|B,E)`
- **Parámetro**: `ε = 0.01` (eventos raros para robo/terremoto)

---

## Parte B — Implementación (Tasks)

### Task 2.1 — Generador de distribución conjunta

Se definen las funciones locales del modelo y la conjunta:

- `p_b(b)` y `p_e(e)` para los priors
- `p_a_dado_be(a, b, e)` para la CPT de `A|B,E`
- `prob_conjunta(b, e, a)` para `P(B,E,A)`

El notebook imprime la tabla completa de `P(B,E,A)` y verifica que la suma total sea `1.0`.

### Task 2.2 — Inferencia marginal

Se implementa `inferencia_marginal(query, evidencia={})` para calcular:

- Marginales (ej. `P(A=1)`) sumando sobre variables ocultas
- Condicionales usando `P(X|Y) = P(X,Y) / P(Y)` cuando hay evidencia

### Task 2.3 — Demostración del efecto “Explain Away”

Se compara:

- `P(B=1 | A=1)` (diagnóstico simple)
- `P(B=1 | A=1, E=1)` (al conocer otra causa)

Mostrando que al observar `E=1`, la probabilidad posterior de `B=1` disminuye, porque `E` “explica” el efecto `A`.

---

## Ejecución (Notebook)

En `Lab9.ipynb`:

1. Ejecutar las celdas en orden (parámetros y definición del modelo).
2. Ejecutar **Task 2.1** para generar e imprimir `P(B,E,A)`.
3. Ejecutar **Task 2.2** para calcular marginales/condicionales (incluye `P(A=1)`).
4. Ejecutar **Task 2.3** para observar y verificar el efecto “Explain Away”.

