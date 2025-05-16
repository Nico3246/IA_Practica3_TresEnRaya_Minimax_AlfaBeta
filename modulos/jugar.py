from Tablero import Tablero
from Estado import Estado
from Humano import Humano
from MinMax import MiniMax


def menu1():
    print("\n")
    print("┌" + "────────────────────────────────" + "┐")
    print("│" + "         Tres en Raya           " + "│")
    print("├" + "────────────────────────────────" + "┤")
    print("│" + " 1. Jugar contra otro jugador   " + "│")
    print("│" + " 2. Jugar contra Minimax        " + "│")
    print("│" + " 3. Jugar contra Alfa-Beta      " + "│")
    print("│" + " 4. Salir                       " + "│")
    print("└" + "────────────────────────────────" + "┘")
    opc1=int(input("Selecciona una opción: "))
    return opc1

def menu2():
    print("\n")
    print("┌" + "────────────────────────────────" + "┐")
    print("│" + "          Elige ficha           " + "│")
    print("├" + "────────────────────────────────" + "┤")
    print("│" + " 1. Usar 'X'                    " + "│")
    print("│" + " 2. Usar 'O'                    " + "│")
    print("└" + "────────────────────────────────" + "┘")
    opc2 = int(input("Selecciona una opción: "))
    return opc2

def opcionesMenu1():
    while True:
        opc=menu1()
        if not str(opc).isdigit():
            print("Entrada incorrecta.Introduce una opcion entre 1 y 4")
            input("Presiona cualquier tecla para continuar...")
            continue
        elif opc<1 or opc>4:
            print("Seleccion incorrecta.Introduce una opcion entre 1 y 4")
            input("Presiona cualquier tecla para continuar...")
            continue

        if opc==1:
            jugarHumano()
            break

        elif opc==2:
            opc2=menu2()
            fichaHumano,fichaIA=opcionesMenu2(opc2)
            jugarMiniMax(fichaHumano,fichaIA)
            break






def opcionesMenu2(opc):
    while True:
        if not str(opc).isdigit():
            print("Entrada incorrecta.Introduce una opcion entre 1 y 4")
            input("Presiona cualquier tecla para continuar...")
            continue
        elif opc < 1 or opc > 4:
            print("Seleccion incorrecta.Introduce una opcion entre 1 y 4")
            input("Presiona cualquier tecla para continuar...")
            continue

        if opc==1:
            fichaHumano="X"
            fichaIA="O"
            break
        elif opc==2:
            fichaHumano="O"
            fichaIA="X"
            break
    return fichaHumano,fichaIA

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
            print("Turno del jugador (" + fichaHumano1 +")")
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


def main():
    opcionesMenu1()



if __name__ =="__main__":
    main()
