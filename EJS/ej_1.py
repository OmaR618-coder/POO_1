class Ejercicio_1():

    import math
    def __init__(self):
        self.x = float(input("x="))
        self.tolerancia = float(input("Tolerancia="))
        self.valorReal = self.math.sin(self.x)
        self.k = 0
        self.aprox = 0

    def code(self):
        while True:
            self.aprox += ((-1)**self.k*self.x**(2*self.k+1))/self.math.factorial(2*self.k+1)
            self.k += 1
            self.error = self.math.fabs((self.valorReal - self.aprox)/self.valorReal) * 100
            if self.error < self.tolerancia:
                break

        print("Valor real = ", self.valorReal)
        print("Aproximación = ", self.aprox)
        print("Error = ",self.error)