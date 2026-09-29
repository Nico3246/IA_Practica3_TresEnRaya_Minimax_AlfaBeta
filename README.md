# IA - Práctica 3: Minimax y Poda Alfa-Beta en Tres en Raya

Práctica universitaria de **Inteligencia Artificial** desarrollada en **Python**, centrada en la implementación y comparación de algoritmos de búsqueda adversarial mediante el juego del **Tres en Raya**.

El proyecto permite jugar partidas entre personas y agentes inteligentes, además de enfrentar entre sí distintas estrategias para observar su comportamiento y comparar métricas como el número de nodos explorados y el tiempo de cálculo.


---

## Objetivos de la práctica

El proyecto está orientado a trabajar conceptos fundamentales de búsqueda adversarial en Inteligencia Artificial:

- representación de estados;
- generación de sucesores;
- funciones de utilidad;
- árboles de juego;
- algoritmo Minimax;
- poda Alfa-Beta;
- comparación experimental entre algoritmos;
- medición de nodos explorados;
- medición del tiempo de decisión.

---

## Juego implementado

El entorno utilizado es el clásico **Tres en Raya** sobre un tablero de 3 × 3.

Cada jugador utiliza una de las fichas:

```text
X
O
```

Una partida finaliza cuando:

- un jugador consigue tres fichas en línea;
- o el tablero queda completo y se produce un empate.

El sistema comprueba victorias en:

- filas;
- columnas;
- diagonal principal;
- diagonal secundaria.

---

## Modos de juego

Desde el menú principal pueden iniciarse diferentes tipos de partida.

### Humano vs Humano

Permite que dos jugadores introduzcan sus movimientos manualmente por consola.

### Humano vs Minimax

Un jugador humano se enfrenta a un agente controlado por el algoritmo **Minimax**.

El usuario puede elegir jugar con `X` o con `O`.

### Humano vs Alfa-Beta

Un jugador humano se enfrenta a un agente que utiliza **Minimax con poda Alfa-Beta**.

### IA vs IA

También pueden ejecutarse enfrentamientos automáticos entre agentes:

- Minimax vs Minimax;
- Alfa-Beta vs Alfa-Beta;
- Minimax vs Alfa-Beta.

Esto permite observar directamente el comportamiento de ambos métodos sobre el mismo problema.

---

## Minimax

La implementación se encuentra en:

```text
modulos/MinMax.py
```

El algoritmo explora los estados sucesores posibles del juego hasta alcanzar posiciones terminales.

La utilidad utilizada desde el punto de vista del agente es:

```text
 1  -> victoria de la IA
 0  -> empate
-1  -> derrota de la IA
```

Durante la búsqueda se alternan dos funciones:

- `MAX`, que intenta maximizar la utilidad;
- `MIN`, que intenta minimizarla.

El agente selecciona finalmente la jugada asociada al mejor valor encontrado.

---

## Poda Alfa-Beta

La implementación se encuentra en:

```text
modulos/AlfaBeta.py
```

El algoritmo mantiene los límites:

```text
alpha
beta
```

durante el recorrido del árbol de juego.

Cuando una rama ya no puede mejorar el resultado conocido, deja de explorarse.

La finalidad de esta implementación es obtener la misma decisión estratégica que Minimax reduciendo el número de estados que es necesario analizar.

---

## Representación del estado

La clase principal del estado del juego se encuentra en:

```text
modulos/Estado.py
```

Gestiona, entre otras operaciones:

- el jugador al que corresponde el turno;
- la ficha actual;
- detección de victoria;
- detección de empate;
- generación de movimientos válidos;
- generación de estados sucesores;
- copia del tablero;
- función de utilidad;
- aplicación de movimientos.

Cada estado puede producir todos sus posibles sucesores colocando la ficha correspondiente en las casillas disponibles.

---

## Tablero

El tablero se implementa en:

```text
modulos/Tablero.py
```

Se representa mediante una matriz de 3 × 3.

La interfaz es completamente por consola y muestra un tablero similar a:

```text
╔═══╦═══╦═══╗
║ X ║ O ║   ║
╠═══╬═══╬═══╣
║   ║ X ║   ║
╠═══╬═══╬═══╣
║ O ║   ║ X ║
╚═══╩═══╩═══╝
```

Cuando existe una línea ganadora, el programa puede resaltarla mediante códigos ANSI de color.

---

## Jugador humano

La lógica de entrada manual se encuentra en:

```text
modulos/Humano.py
```

El usuario introduce un número entre 1 y 9.

Las posiciones se traducen a coordenadas del tablero siguiendo esta distribución:

```text
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

El programa valida:

- que el movimiento esté dentro del rango;
- que la casilla seleccionada esté libre.

---

## Comparación de rendimiento

Tanto Minimax como Alfa-Beta registran información sobre sus decisiones.

Durante una partida se muestran:

- nodos explorados;
- tiempo empleado para calcular una jugada;
- número total de nodos procesados;
- tiempo total acumulado.

El tiempo se mide mediante:

```python
time.perf_counter_ns()
```

Estas métricas permiten comparar experimentalmente el coste de explorar el árbol completo con Minimax frente al uso de poda Alfa-Beta.

---

## Resultados de partidas

El proyecto incluye un pequeño sistema para registrar resultados de enfrentamientos humano contra IA.

Los archivos utilizados son:

```text
modulos/HumanoVSMinMax.txt
modulos/HumanoVSAlfaBeta.txt
```

La clase responsable se encuentra en:

```text
modulos/Resultados.py
```

y mantiene contadores de:

- victorias humanas;
- victorias de la IA;
- empates.

Al iniciar el programa, `main.py` reinicia estos contadores para comenzar una nueva ejecución desde cero.

---

## Estructura del proyecto

```text
IA_Practica3/
├── modulos/
│   ├── AlfaBeta.py
│   ├── Estado.py
│   ├── Humano.py
│   ├── MinMax.py
│   ├── Resultados.py
│   ├── Tablero.py
│   ├── jugar.py
│   ├── main.py
│   ├── menus.py
│   ├── HumanoVSAlfaBeta.txt
│   ├── HumanoVSMinMax.txt
│   └── __init__.py
├── .gitignore
└── README.md
```

### `main.py`

Punto de entrada del programa. Inicializa los resultados y abre el menú principal.

### `menus.py`

Gestiona los diferentes menús de selección:

- modo de juego;
- ficha;
- enfrentamientos entre IAs;
- consulta de resultados.

### `jugar.py`

Coordina las partidas y conecta el tablero, los estados y los distintos tipos de jugador.

### `Estado.py`

Contiene la lógica del juego y la generación del árbol de estados.

### `MinMax.py`

Implementación del algoritmo Minimax.

### `AlfaBeta.py`

Implementación del algoritmo Minimax con poda Alfa-Beta.

### `Tablero.py`

Representación y visualización del tablero.

### `Humano.py`

Gestión de movimientos introducidos por el usuario.

### `Resultados.py`

Registro y visualización de los resultados de las partidas humano contra IA.

---

## Tecnologías

- **Python**
- programación orientada a objetos;
- recursividad;
- árboles de estados;
- biblioteca estándar `time`;
- entrada y salida por consola;
- persistencia básica mediante archivos de texto.

No se necesitan bibliotecas externas para ejecutar el proyecto.

---

## Ejecución

Debido a que los módulos y los archivos de resultados utilizan rutas relativas, la forma más sencilla de ejecutar el programa es entrar en la carpeta `modulos`:

```bash
cd modulos
python main.py
```

En Windows también puede utilizarse:

```powershell
cd modulos
py main.py
```

---

## Flujo de uso

Un flujo típico es:

1. ejecutar `main.py`;
2. seleccionar un modo de juego;
3. elegir ficha cuando corresponda;
4. jugar o ejecutar el enfrentamiento entre IAs;
5. observar el resultado;
6. comparar nodos explorados y tiempos entre Minimax y Alfa-Beta.

---

## Estado del proyecto

El repositorio contiene una implementación académica enfocada en estudiar búsqueda adversarial.

El diseño está deliberadamente adaptado a un juego pequeño como Tres en Raya, donde es posible explorar el árbol de estados completo.

Entre sus características se encuentran:

- interfaz por consola;
- tablero fijo de 3 × 3;
- función de utilidad simple;
- exploración exhaustiva con Minimax;
- optimización mediante poda Alfa-Beta;
- estadísticas básicas de ejecución;
- persistencia sencilla de resultados en archivos de texto.

No está planteado como un motor genérico de juegos ni como una aplicación final de producción.

---

## Conceptos trabajados

Esta práctica permite trabajar directamente con:

- búsqueda adversarial;
- juegos de suma cero;
- árboles de juego;
- estados terminales;
- funciones de utilidad;
- Minimax;
- poda Alfa-Beta;
- generación de sucesores;
- recursividad;
- comparación de rendimiento;
- medición experimental de algoritmos.

---

## Contexto académico

Proyecto desarrollado como **Práctica 3 de Inteligencia Artificial**.

Su finalidad principal es implementar y comparar **Minimax** y **poda Alfa-Beta** mediante un entorno sencillo y completamente observable como el Tres en Raya.
