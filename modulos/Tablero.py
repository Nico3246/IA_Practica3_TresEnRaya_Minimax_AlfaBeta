from fileinput import close


def red(texto):
    ROJO = "\033[31m"
    RESET = "\033[0m"
    return ROJO + texto + RESET

class Tablero:
    def __init__(self):
        self.tablero = [[" " for _ in range(3)] for _ in range(3)]

    def pintar(self,lineaGanadora=None):
        print("╔═══╦═══╦═══╗")
        for i in range(3):
            print("║ ", end="")
            for j in range(3):
                if lineaGanadora is not None and (i,j) in lineaGanadora:
                    print(red(self.tablero[i][j]), end="")
                else:
                    print(self.tablero[i][j], end="")
                if j<2:
                    print(" ║ ", end="")
                else:
                    print(" ║")
            if i<2:
                print("╠═══╬═══╬═══╣")
        print("╚═══╩═══╩═══╝")


    def iniciarPartida(self):
        print("Jugador 1: X")
        print("Jugador 2: O")

        self.pintar()


    def fin(self, jugador):
        if(jugador!=-1):
            print("Jugador " + str(jugador) + ":")
            self.pintar()
            print("Partida finalizada, Jugador " + str(jugador) + " ha resultado ganador")
        else:
            print("Partida finalizada, Empate")

    def guardarTablero(self):
        f = open("Tablero.txt", "w")
        for i in range(3):
            for j in range(3):
                f.write(self.tablero[i][j])
            f.write("\n")
        f.close()

    def cargarTablero(self):
        archivo="Tablero.txt"
        f = open(archivo, "r")
        lineas = f.readlines()
        close()

        # Crear tabla con el tamaño del fihero
        self.tabla = [[" " for _ in range(3)] for _ in range(3)]

        for i in range(3):
            linea_actual = lineas[i].strip()
            for j in range(3):
                self.tabla[i][j] = linea_actual[j]

        self.iniciarPartida()









