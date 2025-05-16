from Tablero import Tablero

class Estado:
    def __init__(self,tablero):
        self.tablero = tablero
        self.turnoJugador=True
        


    def cambiarturno(self):#intercambia los turno
        self.turnoJugador=not self.turnoJugador


    def tableroLleno(self):
        for i in range(3):
            for j in range(3):
                if self.tablero.tablero[i][j]==" ":
                    return False
        return True

    def terminado(self):
        if self.tableroLleno() or self.comprobar()!=False:
            return True
        else:
            return False

    def comprobarHorizontales(self):
        for i in range(3):
            if self.tablero.tablero[i][0]==self.tablero.tablero[i][1]==self.tablero.tablero[i][2] and self.tablero.tablero[i][0]=="O":
                return "O"
            elif self.tablero.tablero[i][0]==self.tablero.tablero[i][1]==self.tablero.tablero[i][2] and self.tablero.tablero[i][0]=="X":
                return "X"

        return False

    def comprobarVerticales(self):
        for i in range(3):
            if self.tablero.tablero[0][i]==self.tablero.tablero[1][i]==self.tablero.tablero[2][i] and self.tablero.tablero[0][i]=="O":
                return "O"
            elif self.tablero.tablero[0][i]==self.tablero.tablero[1][i]==self.tablero.tablero[2][i] and self.tablero.tablero[0][i]=="X":
                return "X"

        return False


    def comprobarDiagonal1(self):
        if self.tablero.tablero[0][0]==self.tablero.tablero[1][1]==self.tablero.tablero[2][2] and self.tablero.tablero[0][0]=="O":
            return "O"
        elif self.tablero.tablero[0][0]==self.tablero.tablero[1][1]==self.tablero.tablero[2][2] and self.tablero.tablero[0][0]=="X":
            return "X"

        return False


    def comprobarDiagonal2(self):
        if self.tablero.tablero[0][2]==self.tablero.tablero[1][1]==self.tablero.tablero[2][0] and self.tablero.tablero[0][2]=="O":
            return "O"
        elif self.tablero.tablero[0][2]==self.tablero.tablero[1][1]==self.tablero.tablero[2][0] and self.tablero.tablero[0][2]=="X":
            return "X"

        return False

    def comprobar(self):
        if(self.comprobarHorizontales()!=False):
            return self.comprobarHorizontales()
        elif(self.comprobarVerticales()!=False):
            return self.comprobarVerticales()
        elif(self.comprobarDiagonal1()!=False):
            return self.comprobarDiagonal1()
        elif(self.comprobarDiagonal2()!=False):
            return self.comprobarDiagonal2()
        else:
            return False

    def ganador(self,fichaIA):
        resultado=self.comprobar()
        if resultado==fichaIA:
            return 1  #gana ia
        elif resultado==False:
            return 0  #empate
        else:
            return -1  #gana oponente


    def movimientosValidos(self):
        movimientos=[]
        for i in range(3):
            for j in range(3):
                if self.tablero.tablero[i][j]==" ":
                    movimientos.append((i,j))
        return movimientos

    def copiarTablero(self):
        tableroCopia=Tablero()
        tableroCopia.tablero=[fila[:] for fila in self.tablero.tablero]#crea una copia del tablero que no modifica el original
        return tableroCopia

    def sucesores(self):
        sucesores=[]
        if(self.turnoJugador):
            ficha="X"
        else:
            ficha="O"

        for i,j in self.movimientosValidos():
            tableroCopia=self.copiarTablero()#creo una copia del tablero
            tableroCopia.tablero[i][j]=ficha#hago el movimiento en la copia

            nuevoEstado=Estado(tableroCopia)#creo un nuevo estado con la posible opcion

            nuevoEstado.cambiarturno()#cambio el turno en el nuevo estado

            sucesores.append((nuevoEstado,(i,j)))#meto el nuevo estado en sucesores y la juagda

        return sucesores



    def comprobarCasilla(self,pos):
        if self.tablero.tablero[pos[0]][pos[1]]==" ":
            return True
        else:
            return False


    def traductor(self,pos):
        fila=(pos - 1) // 3
        columna = (pos - 1) % 3
        return fila, columna


    def jugada(self,pos,jugador):#para humano
        pos=self.traductor(pos)
        if self.comprobarCasilla(pos):
            self.tablero.tablero[pos[0]][pos[1]]=jugador

    def jugadaCoordenadas(self,fila,columna,jugador):#para ia
        if self.comprobarCasilla((fila,columna)):
            self.tablero.tablero[fila][columna]=jugador

    def jugadorActual(self):
        if self.turnoJugador:
            return "X"
        else:
            return "O"

    def buscarLineaGanadora(self):
        for i in range(3):#buscar en horizontales
            if self.tablero.tablero[i][0]==self.tablero.tablero[i][1]==self.tablero.tablero[i][2] and self.tablero.tablero[i][0]!=" ":
                return [(i,0),(i,1),(i,2)]

        for i in range(3):#buscar en verticales
            if self.tablero.tablero[0][i]==self.tablero.tablero[1][i]==self.tablero.tablero[2][i] and self.tablero.tablero[0][i]!=" ":
                return [(0,i),(1,i),(2,i)]

        if self.tablero.tablero[0][0]==self.tablero.tablero[1][1]==self.tablero.tablero[2][2] and self.tablero.tablero[0][0]!=" ":
            return [(0,0),(1,1),(2,2)]

        if self.tablero.tablero[0][2]==self.tablero.tablero[1][1]==self.tablero.tablero[2][0] and self.tablero.tablero[0][2]!=" ":
            return [(0,2),(1,1),(2,0)]

        return None












