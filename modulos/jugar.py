from Tablero import Tablero
from Estado import Estado
from Humano import Humano
from MinMax import MiniMax


def main():
    tablero = Tablero()
    estado = Estado(tablero)

    jugadorHumano = Humano(estado,"X")
    jugadorMiniMax = MiniMax(estado,"O")

    while not estado.terminado():
        tablero.pintar()
        print("\n")
        if estado.turnoJugador:
            print("Turno del jugador Humano (X)")
            jugadorHumano.hacerJugada()
        else:
            print("Turno del jugador MinMax (O)")
            jugadorMiniMax.hacerJugada()


    resultado = estado.comprobar()

    linea=estado.buscarLineaGanadora()
    tablero.pintar(lineaGanadora=linea)

    if resultado=="X":
        print("El jugador 1 (X) ha ganado")
    elif resultado=="O":
        print("El jugador 2 (O) ha ganado")
    else:
        print("Empate")




if __name__ =="__main__":
    main()
