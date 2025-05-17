from Tablero import Tablero
from Estado import Estado
from Humano import Humano
from MinMax import MiniMax
from AlfaBeta import AlfaBeta
from Resultados import Contador


def menu1():
    print("\n")
    print("┌" + "────────────────────────────────" + "┐")
    print("│" + "         Tres en Raya           " + "│")
    print("├" + "────────────────────────────────" + "┤")
    print("│" + " 1. Jugar contra otro jugador   " + "│")
    print("│" + " 2. Jugar contra Minimax        " + "│")
    print("│" + " 3. Jugar contra Alfa-Beta      " + "│")
    print("│" + " 4. IA vs IA                    " + "│")
    print("│" + " 5. Mostrar resultados          " + "│")
    print("│" + " 6. Salir                       " + "│")
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
    print("│" + " 3. Volver                      " + "│")
    print("└" + "────────────────────────────────" + "┘")
    opc2 = int(input("Selecciona una opción: "))
    return opc2

def menu3():
    print("\n")
    print("┌" + "────────────────────────────────" + "┐")
    print("│" + "          Elige modo            " + "│")
    print("├" + "────────────────────────────────" + "┤")
    print("│" + " 1. MiniMax vs MiniMAx          " + "│")
    print("│" + " 2. Alfa-Beta vs Alfa-Beta      " + "│")
    print("│" + " 3. MiniMax vs Alfa-Beta        " + "│")
    print("│" + " 4. Volver                      " + "│")
    print("└" + "────────────────────────────────" + "┘")
    opc2 = int(input("Selecciona una opción: "))
    return opc2

def menu4():
    print("\n")
    print("┌" + "────────────────────────────────" + "┐")
    print("│" + "              Menu              " + "│")
    print("├" + "────────────────────────────────" + "┤")
    print("│" + " 1. Jugar                       " + "│")
    print("│" + " 2. Resultados                  " + "│")
    print("│" + " 3. Volver                      " + "│")
    print("└" + "────────────────────────────────" + "┘")
    opc2 = int(input("Selecciona una opción: "))
    return opc2


def opcionesMenu1():
    while True:
        opc=menu1()
        if opc<1 or opc>6:
            print("Seleccion incorrecta.Introduce una opcion entre 1 y 4")
            input("Presiona cualquier tecla para continuar...")
            continue

        if opc==1:
            archivo = "HumanoVSHumano.txt"
            seleccion=menu4()
            if seleccion==1:
                resultado=jugarHumano()
                contador=Contador(archivo)
                contador.resultados(resultado,"X","O")
            elif seleccion==2:
                mostrarResultados(archivo)


        elif opc==2:
            archivo = "HumanoVSMinMax.txt"
            seleccion = menu4()
            if seleccion==1:
                opc2=menu2()

                if opc2==3:
                    continue

                fichaHumano,fichaIA=opcionesMenu2(opc2)
                resultado=jugarMiniMax(fichaHumano,fichaIA)
                contador=Contador(archivo)
                contador.resultados(resultado,fichaHumano,fichaIA)

            elif seleccion==2:
                mostrarResultados(archivo)


        elif opc==3:
            archivo = "HumanoVSAlfaBeta.txt"
            seleccion = menu4()
            if seleccion==1:
                opc2 = menu2()

                if opc2==3:
                    continue

                fichaHumano,fichaIA=opcionesMenu2(opc2)
                resultado=jugarAlfaBeta(fichaHumano,fichaIA)
                contador=Contador(archivo)
                contador.resultados(resultado,fichaHumano,fichaIA)
            elif seleccion==2:
                mostrarResultados(archivo)

        elif opc==4:
            opc3=menu3()
            opcionesMenu3(opc3)

        elif opc==5:
            mostrarResultados("HumanoVSHumano.txt")
            mostrarResultados("HumanoVSMinMax.txt")
            mostrarResultados("HumanoVSAlfaBeta.txt")

        elif opc==6:
            print("Saliendo...")
            break




def opcionesMenu2(opc):
    while True:
        if opc < 1 or opc > 3:
            print("Seleccion incorrecta.Introduce una opcion entre 1 y 4")
            input("Presiona cualquier tecla para continuar...")
            continue

        if opc==1:
            ficha1="X"
            ficha2="O"
            break
        elif opc==2:
            ficha1="O"
            ficha2="X"
            break

    return ficha1,ficha2




def opcionesMenu3(opc):
    while True:
        if opc < 1 or opc > 4:
            print("Seleccion incorrecta.Introduce una opcion entre 1 y 4")
            input("Presiona cualquier tecla para continuar...")
            continue

        if opc==1:
            ficha1="X"
            ficha2="O"
            minMaxVSminMAX(ficha1, ficha2)
            break

        elif opc==2:
            ficha1="X"
            ficha2="O"
            AlfaBetaVSAlfaBeta(ficha1, ficha2)
            break

        elif opc==3:
            ficha1="X"
            ficha2="O"
            MiniMaxVSAlfaBeta(ficha1, ficha2)
            break




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



def main():
    opcionesMenu1()



if __name__ =="__main__":
    main()
