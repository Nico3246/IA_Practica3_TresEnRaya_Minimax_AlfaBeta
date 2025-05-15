
class Humano:
    def __init__(self,estado):
        self.estado = estado
        self.tablero=estado.tablero


    def hacerJugada(self):
        while True:
            pos=int(input("Introduce un movimiento: "))
            if pos<1 or pos>9:
                print("Movimiento incorrecto debe estar entre 1 y 9")
                continue

            f,c=self.estado.traductor(pos)
            if not self.estado.comprobarCasilla((f,c)):
                print("Casilla ocupada, introduzca otra")
                continue

            if self.estado.jugadorActual()=="X":
                self.estado.jugada(pos,"X")
            else:
                self.estado.jugada(pos,"O")
            self.estado.cambiarturno()
            break





