##4.1 Suma de dos numeros
suma = lambda x, y: x + y
numero1 = float(input("Número 1:"))
numero2= float(input("Número 2:"))
resultado = suma(numero1, numero2)
print (resultado)

##4.2 numero par
par=lambda x: x % 2 == 0
numero=float(input("Ingrese número:"))
print(par(numero))

##4.3 tuplas
lista_tuplas = [(2,3),(6,5),(8,7),(8,9),(1,8)]
tuplas_ordenadas = sorted(lista_tuplas, key=lambda x: x[1])
print(tuplas_ordenadas)

##4.4 filtro de numeros
lista_numeros = [1,12,34,4,23,8,6,7,13,54]
numeros_mayores_10=list(filter(lambda x: x>10,lista_numeros))
print(numeros_mayores_10)

##4.5 Cuadrado de numeros
lista=[4,6,8,1,4,6,10,9]
cuadrados=list(map(lambda x : x**2, lista))
print(cuadrados)
