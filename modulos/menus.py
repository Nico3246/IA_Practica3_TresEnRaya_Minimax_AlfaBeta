from jugar import jugarHumano,jugarAlfaBeta,jugarMiniMax,minMaxVSminMAX,AlfaBetaVSAlfaBeta,MiniMaxVSAlfaBeta,mostrarResultados
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
            jugarHumano()


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