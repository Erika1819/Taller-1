from if_else import resultado4()
from While import numero_vocales
from For import tablero_ajedrez
from Lambda import resultado

def menu ():
    print("Menu de ejercicios")
    print("1. Clasificaion de temperatura")
    print("2. Contador de vocales")
    print("3. Tablero de ajedrez")
    print("4. Suma de dos números")
    print("5. salir")

def ejercicios_ejecutar (opcion):
     if opcion ==1:
           resultado4
     elif opcion ==2:
           numero_vocales
     elif opcion == 3 :
           tablero_ajedrez()  
     elif opcion == 4 :
           resultado  

if __name__ == "__main__":
        while True:
             menu()
             opcion = int(input("Ingrese una opción:"))
             if opcion == 5 :
                  break
             ejercicios_ejecutar(opcion)
     
      