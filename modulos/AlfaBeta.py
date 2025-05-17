import time
class AlfaBeta:
    def __init__(self, estado,ficha):
        self.estado = estado
        self.ficha = ficha

    def AlfaBeta(self,estado):
        mejorValor=float("-inf")
        alfa=float("-inf")
        beta=float("inf")
        mejorJugada=None

        for sucesor,jugada in estado.sucesores():
            valor=self.MIN(sucesor,alfa,beta)

            if valor>mejorValor:
                mejorValor=valor
                mejorJugada=jugada
            alfa=max(alfa,mejorValor)

        return mejorJugada

    def MAX(self,estado,alfa,beta):
        if estado.terminado():
            return estado.ganador(self.ficha)

        valor=float("-inf")
        for sucesor,_ in estado.sucesores():
            valor=max(valor,self.MIN(sucesor,alfa,beta))

            if valor>=beta:
                return valor
            alfa=max(alfa,valor)

        return valor

    def MIN(self,estado,alfa,beta):
        if estado.terminado():
            return estado.ganador(self.ficha)

        valor=float("inf")
        for sucesor,_ in estado.sucesores():
            valor=min(valor,self.MAX(sucesor,alfa,beta))

            if valor<=alfa:
                return valor
            beta=min(beta,valor)

        return valor


    def hacerJugada(self):
        time.sleep(0.5)
        fila,columna=self.AlfaBeta(self.estado)
        self.estado.jugadaCoordenadas(fila,columna,self.ficha)
        self.estado.cambiarturno()