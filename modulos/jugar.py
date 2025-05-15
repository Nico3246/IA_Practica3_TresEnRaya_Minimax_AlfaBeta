from Tablero import Tablero
from Estado import Estado
from Humano import Humano


def main():
    tablero = Tablero()
    estado = Estado(tablero)

    jugador1 = Humano(estado)
    jugador2 = Humano(estado)

    while not estado.terminado():
        tablero.pintar()
        print("\n")
        if estado.turnoJugador:
            print("Turno del jugador 1 (X)")
            jugador1.hacerJugada()
        else:
            print("Turno del jugador 2 (O)")
            jugador2.hacerJugada()

    ganador=estado.ganador()
    if ganador==1:
        tablero.pintar()
        print("El jugador 1 (X) ha ganado")
    elif ganador==-1:
        tablero.pintar()
        print("El jugador 2 (O) ha ganado")
    else:
        print("Empate")




if __name__ =="__main__":
    main()
