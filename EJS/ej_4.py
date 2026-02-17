class Ejercicio_4():
    def __init__(self):
        self.n=int(input("Profundidad del pozo(pulg)="))
        self.u=int(input("Energía(pulg/min)="))
        self.d = 1
        self.ascenso=0
        self.tiempo  = 0

    def code(self):
        while True:
            self.ascenso += self.u #desplazamiento hacia arriba
            self.tiempo += 1  #Tiempo de ascenso
            if self.ascenso >= self.n:  #Si llegó a la cima sale del ciclo
                break
            self.ascenso -= self.d #Desplazamiento hacia abajo
            self.tiempo += 1  #Tiempo de descanso

        print("Tiempo en salir:", self.tiempo)