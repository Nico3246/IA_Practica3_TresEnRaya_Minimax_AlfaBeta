import time
class AlfaBeta:
    def __init__(self, estado,ficha):
        self.estado = estado
        self.ficha = ficha
        self.nodos = 0
        self.nodosTotal = 0
        self.tiempoTotal = 0

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
        self.nodos+=1
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
        self.nodos += 1
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
        inicio = time.perf_counter_ns()
        fila,columna=self.AlfaBeta(self.estado)
        fin = time.perf_counter_ns()
        duracion = (fin - inicio) / 1000

        print("Nodos explorados: " + str(self.nodos))
        print("Tiempo empleado: " + str(duracion))

        self.nodosTotal += self.nodos
        self.tiempoTotal += duracion


        self.estado.jugadaCoordenadas(fila,columna,self.ficha)
        self.estado.cambiarturno()