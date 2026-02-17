from EJS.ej_2 import Ejercicio_2
from EJS.ej_3 import Ejercicio_3

def menu_principal():
    while True:
        print("Menú Principal")
        print("1)  Ejercicio 2")
        print("2)  Ejercicio 3")
        print("3)  Salir")
        op = int(input("Eliga opción: "))
        match(op):
            case 1:
                test = Ejercicio_2()
                test.code()
            case 2:
                test = Ejercicio_3()
                test.code()
            case 3:
                break
            case _:
                print("Opción no válida")