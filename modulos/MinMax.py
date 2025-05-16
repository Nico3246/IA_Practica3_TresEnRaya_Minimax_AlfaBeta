class MiniMax:
    def __init__(self, estado,ficha):
        self.estado = estado
        self.ficha = ficha

    def minimax(self, estado):
        if estado.jugadorActual()==self.ficha:
            mejorValor=float("-inf")
        else:
            mejorValor=float("inf")
        mejorJugada=None

        for sucesor,jugada in estado.sucesores():
            if sucesor.jugadorActual() == self.ficha:
                valor = self.MAX(sucesor)
            else:
                valor = self.MIN(sucesor)

            if estado.jugadorActual()==self.ficha:
                if valor>mejorValor:
                    mejorValor=valor
                    mejorJugada=jugada
            else:
                if valor<mejorValor:
                    mejorValor=valor
                    mejorJugada=jugada

        return mejorJugada


    def MAX(self,estado):
        if estado.terminado():
            return estado.ganador(self.ficha)

        valorMax=float("-inf")
        for sucesor,_ in estado.sucesores():
            if sucesor.jugadorActual() == self.ficha:
                valor=self.MAX(sucesor)
            else:
                valor=self.MIN(sucesor)
            valorMax=max(valorMax,valor)
        return valorMax


    def MIN(self,estado):
        if estado.terminado():
            return estado.ganador(self.ficha)

        valorMin=float("inf")
        for sucesor,_ in estado.sucesores():
            if sucesor.jugadorActual() == self.ficha:
                valor=self.MAX(sucesor)
            else:
                valor=self.MIN(sucesor)
            valorMin=min(valorMin,valor)
        return valorMin

    def hacerJugada(self):
        fila,columna=self.minimax(self.estado)
        self.estado.jugadaCoordenadas(fila,columna,self.ficha)
        self.estado.cambiarturno()

