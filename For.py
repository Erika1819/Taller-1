##3.1 Suma de cubos
suma_cubos= 0

for numero in range(1, 51):
    cubo = numero ** 3
    suma_cubos += cubo

print("La suma de los cubos es:", suma_cubos)

##3.2 piramide
def piramide ():
    filas = int(input("Escriba número de filas:"))

    for i in range (filas):
        for j in range (filas - i -1):
            print(" ", end="")
        for k in range(2* i -1):
            print("*", end="")

        print()    
piramide()

##3.3 tablero de ajedrez
def tablero_ajedrez():
    q = int(input("Escriba el tamaño del tablero:"))

    for i in range (q):
        for j in range (q):
            if (i+j) % 2 == 0:
                print ("⬛", end="")
            else:
                print ("⬜", end="")   
        print()
tablero_ajedrez()

#3.4 cadena invertida
def cadena_invertida():
    cadena = input("Ingrese cadena:")
    invertir= ""    
    for i in range (len(cadena) -1, -1, -1):
        invertir += cadena[i]
    return invertir

print(cadena_invertida())

##3.5 algoritmo de busqueda
def algoritmo_busqueda():
    lista_caracteres= input("Ingrese los caracteres :")
    lista_caracteres = lista_caracteres.split()
    
    elemento= input("Ingrese el elemento a buscar:")

    for i in range (len(lista_caracteres)):
        if lista_caracteres[i]==elemento:
            return i 
    return -1
Buscador= algoritmo_busqueda()
if Buscador !=-1:
    print ("El elemento se encuentra en la posición:", Buscador)
else:
    print("El elemento no se encontró")    

