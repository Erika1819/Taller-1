import random

def menu():
    print("Menú de Ejercicios:")
    print("1. Ejercicios if-else")
    print("2. Ejercicios while")
    print("3. Ejercicios for")
    print("4. Funciones lambda")
    print("5. Salir")
    opcion = int(input("Ingrese una opción: "))
    return opcion

def ejercicio_if_else(opcion):
    def ejercicio_1_1():
    letra = input("Ingrese una letra: ").lower()
    if letra in 'abcdefg':
        print("Es una de las primeras letras del alfabeto.")
    elif letra in 'xyz':
        print("Es una de las últimas letras del alfabeto.")
    else:
        print("La letra no está al principio ni al final del alfabeto.")
       
def ejercicio_while(opcion):
        if opcion == 2:
        def ejercicio_2_1():
            numero = 20
            while numero >= 1:
                print(numero)
                numero -= 1
        ejercicio_2_1()

def ejercicio_For(opcion):
    if opcion == 3:
        def tablero_ajedrez (q):
            q = int(input("Escriba el tamaño del tablero:"))
            for i in range (q):
                for j in range (q):
                    if (i+j) % 2 == 0:
                        print ("⬛", end="")
                    else:
                        print ("⬜", end="")
                print()
            tablero_ajedrez()

def ejercicio_lambda(opcion):
    if opcion == 4:
        par = lambda x: x % 2 == 0
        numero=float(input("Ingrese número:"))
        resultado = par(numero)
        print(resultado)

if __name__ == "__main__":
    while True:
        opcion_menu = menu()
        if opcion_menu == 1:
            opcion_ejercicio = int(input("Ingrese el número del ejercicio if-else (1-5): "))
            ejercicio_if_else(opcion_ejercicio)
        elif opcion_menu == 2:
            # ...
        # ... y así sucesivamente
        elif opcion_menu == 5:
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")