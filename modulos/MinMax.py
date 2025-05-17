import time
class MiniMax:
    def __init__(self, estado,ficha):
        self.estado = estado
        self.ficha = ficha
        self.nodos=0
        self.nodosTotal = 0
        self.tiempoTotal = 0

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
        self.nodos+=1
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
        self.nodos += 1
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


    def reiniciarNodos(self):
        self.nodos=0

    def hacerJugada(self):
        time.sleep(0.5)
        self.reiniciarNodos()
        inicio = time.perf_counter_ns()
        fila,columna=self.minimax(self.estado)
        fin = time.perf_counter_ns()
        duracion=(fin-inicio)/1000

        print("Nodos explorados: " + str(self.nodos))
        print("Tiempo empleado: " + str(duracion))

        self.nodos+=self.nodos
        self.tiempoTotal+=duracion

        self.estado.jugadaCoordenadas(fila,columna,self.ficha)
        self.estado.cambiarturno()

