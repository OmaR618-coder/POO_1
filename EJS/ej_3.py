class Ejercicio_3(): 
    def __init__(self):
        self.palabra = ""

    def code(self):
        while self.palabra != "salir":
            self.palabra = input("Palabra:")
            print(self.palabra)
            print("Para salir escribe --> salir <--")