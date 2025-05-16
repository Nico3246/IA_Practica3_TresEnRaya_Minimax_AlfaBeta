class MiniMax:
    def __init__(self, estado,ficha):
        self.estado = estado
        self.ficha = ficha

    def minimax(self, estado):
        mejorValor=float("-inf")
        mejorJugada=None
        for sucesor,jugada in estado.sucesores():
            valor = self.MIN(sucesor)
            if valor>mejorValor:
                mejorValor=valor
                mejorJugada=jugada
        return mejorJugada


    def MAX(self,estado):
        if estado.terminado():
            return estado.ganador(self.ficha)

        valorMax=float("-inf")
        for sucesor,_ in estado.sucesores():
            valorMax=max(valorMax,self.MIN(sucesor))
        return valorMax


    def MIN(self,estado):
        if estado.terminado():
            return estado.ganador(self.ficha)

        valorMin=float("inf")
        for sucesor,_ in estado.sucesores():
            valorMin=min(valorMin,self.MAX(sucesor))
        return valorMin

    def hacerJugada(self):
        fila,columna=self.minimax(self.estado)
        self.estado.jugadaCoordenadas(fila,columna,self.ficha)
        self.estado.cambiarturno()

