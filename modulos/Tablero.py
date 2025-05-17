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












