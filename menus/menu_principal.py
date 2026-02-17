from EJS.ej_1 import Ejercicio_1
from EJS.ej_3 import Ejercicio_3
from EJS.ej_2 import Ejercicio_2
from EJS.ej_4 import Ejercicio_4

def menu_principal():
    while True:
        print("Menú Principal")
        print("1)  Ejercicio 1")
        print("2)  Ejercicio 2")
        print("3)  Ejercicio 3")
        print("4)  Ejercicio 4")
        print("5)  Salir")
        op = int(input("Eliga opción: "))
        match(op):
            case 1:
                test = Ejercicio_1()
                test.code()
            case 2:
                test = Ejercicio_2()
                test.code()
            case 3:
                test = Ejercicio_3()
                test.code()
            case 4:
                test = Ejercicio_4()
                test.code()
            case 5:
                break
            case _:
                print("Opción no válida")