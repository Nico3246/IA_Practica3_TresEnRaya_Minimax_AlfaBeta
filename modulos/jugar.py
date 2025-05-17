from Tablero import Tablero
from Estado import Estado
from Humano import Humano
from MinMax import MiniMax
from AlfaBeta import AlfaBeta
from Resultados import Contador

def jugarHumano():
    tablero = Tablero()
    estado = Estado(tablero)

    fichaHumano1 = "X"
    fichaHumano2 = "O"

    jugadorHumano1 = Humano(estado, fichaHumano1)
    jugadorHumano2 = Humano(estado, fichaHumano2)

    while not estado.terminado():
        tablero.pintar()
        print("\n")
        if estado.turnoJugador:
            print("Turno del jugador (" + fichaHumano1 +")")
            jugadorHumano1.hacerJugada()
        else:
            print("Turno del jugador (" + fichaHumano2 +")")
            jugadorHumano2.hacerJugada()

    resultado = estado.comprobar()

    linea = estado.buscarLineaGanadora()
    tablero.pintar(lineaGanadora=linea)

    if resultado == "X":
        print("El jugador 1 (X) ha ganado")

    elif resultado == "O":
        print("El jugador 2 (O) ha ganado")
    else:
        print("Empate")

    return resultado





def jugarMiniMax(fichaHumano,fichaIA):
    tablero = Tablero()
    estado = Estado(tablero)


    if fichaHumano == "X":
        estado.turnoJugador = True
    else:
        estado.turnoJugador = False

    jugadorHumano = Humano(estado, fichaHumano)
    jugadorMiniMax = MiniMax(estado, fichaIA)

    while not estado.terminado():
        tablero.pintar()
        print("\n")
        if estado.turnoJugador:
            print("Turno del jugador Humano " + fichaHumano)
            jugadorHumano.hacerJugada()
        else:
            print("Turno del jugador MinMax " + fichaIA)
            jugadorMiniMax.hacerJugada()

    resultado = estado.comprobar()

    linea = estado.buscarLineaGanadora()
    tablero.pintar(lineaGanadora=linea)

    if resultado == "X":
        print("El jugador 1 (X) ha ganado")
    elif resultado == "O":
        print("El jugador 2 (O) ha ganado")
    else:
        print("Empate")

    return resultado



def jugarAlfaBeta(fichaHumano,fichaIA):
    tablero = Tablero()
    estado = Estado(tablero)

    if fichaHumano == "X":
        estado.turnoJugador = True
    else:
        estado.turnoJugador = False

    jugadorHumano = Humano(estado, fichaHumano)
    jugadorAlfaBeta = AlfaBeta(estado, fichaIA)

    while not estado.terminado():
        tablero.pintar()
        print("\n")
        if estado.turnoJugador:
            print("Turno del jugador Humano " + fichaHumano)
            jugadorHumano.hacerJugada()
        else:
            print("Turno del jugador AlfaBeta " + fichaIA)
            jugadorAlfaBeta.hacerJugada()

    resultado = estado.comprobar()

    linea = estado.buscarLineaGanadora()
    tablero.pintar(lineaGanadora=linea)

    if resultado == "X":
        print("El jugador 1 (X) ha ganado")
    elif resultado == "O":
        print("El jugador 2 (O) ha ganado")
    else:
        print("Empate")

    return resultado



def minMaxVSminMAX(fichaIA1,fichaIA2):
    tablero = Tablero()
    estado = Estado(tablero)

    if fichaIA1 == "X":
        estado.turnoJugador = True
    else:
        estado.turnoJugador = False

    jugador1 = MiniMax(estado, fichaIA1)
    jugador2 = MiniMax(estado, fichaIA2)

    while not estado.terminado():
        tablero.pintar()
        print("\n")
        if estado.turnoJugador:
            print("Turno del jugador MinMax1 (" + fichaIA1 + ")")
            jugador1.hacerJugada()
        else:
            print("Turno del jugador MinMax2 (" + fichaIA2 + ")")
            jugador2.hacerJugada()

    resultado = estado.comprobar()

    linea = estado.buscarLineaGanadora()
    tablero.pintar(lineaGanadora=linea)

    if resultado == "X":
        print("El jugador 1 (X) ha ganado")
    elif resultado == "O":
        print("El jugador 2 (O) ha ganado")
    else:
        print("Empate")





def AlfaBetaVSAlfaBeta(fichaIA1,fichaIA2):
    tablero = Tablero()
    estado = Estado(tablero)

    if fichaIA1 == "X":
        estado.turnoJugador = True
    else:
        estado.turnoJugador = False

    jugador1 = AlfaBeta(estado, fichaIA1)
    jugador2 = AlfaBeta(estado, fichaIA2)

    while not estado.terminado():
        tablero.pintar()
        print("\n")
        if estado.turnoJugador:
            print("Turno del jugador Alfa-Beta 1 (" + fichaIA1 + ")")
            jugador1.hacerJugada()
        else:
            print("Turno del jugador Alfa-Beta 2 (" + fichaIA2 + ")")
            jugador2.hacerJugada()

    resultado = estado.comprobar()

    linea = estado.buscarLineaGanadora()
    tablero.pintar(lineaGanadora=linea)

    if resultado == "X":
        print("El jugador 1 (X) ha ganado")
    elif resultado == "O":
        print("El jugador 2 (O) ha ganado")
    else:
        print("Empate")





def MiniMaxVSAlfaBeta(fichaIA1,fichaIA2):
    tablero = Tablero()
    estado = Estado(tablero)

    if fichaIA1 == "X":
        estado.turnoJugador = True
    else:
        estado.turnoJugador = False

    jugador1 = MiniMax(estado, fichaIA1)
    jugador2 = AlfaBeta(estado, fichaIA2)

    while not estado.terminado():
        tablero.pintar()
        print("\n")
        if estado.turnoJugador:
            print("Turno del jugador MinMax (" + fichaIA1 + ")")
            jugador1.hacerJugada()
        else:
            print("Turno del jugador Alfa-Beta (" + fichaIA2 + ")")
            jugador2.hacerJugada()

    resultado = estado.comprobar()

    linea = estado.buscarLineaGanadora()
    tablero.pintar(lineaGanadora=linea)

    if resultado == "X":
        print("El jugador 1 (X) ha ganado")
    elif resultado == "O":
        print("El jugador 2 (O) ha ganado")
    else:
        print("Empate")

def mostrarResultados(archivo):
    contador=Contador(archivo)
    contador.mostrarResultados()


