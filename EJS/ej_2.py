class Ejercicio_2():
    def __init__(self):

        self.password = "lunes"
        self.intentos = 0
        self.palabra = ""
    
    def code(self):
        while self.palabra != self.password:
            self.palabra = input("Contraseña:")
            self.intentos += 1
            if self.intentos == 5:
                print("Excediste las oportunidades")
                break