##2.1 secuencia de numeros inversa
numero = 20

while numero >=1:
    print(numero)
    numero = numero - 1

##2.2 Algoritmo
Algoritmo = 2

while Algoritmo <= 50:
    print(Algoritmo)
    Algoritmo += 2

##2.3 Contador de vocales
def contador_vocales(frase):
    vocales= "aeiouAEIOU"
    contador=0
    i=0

    while i < len(frase):
        if frase [i] in vocales:
            contador += 1
        i +=1    
    return contador

frase = input("Ingrese una frase:")
numero_vocales=contador_vocales(frase)
print("La frase tiene", numero_vocales, "vocales")

##2.4 Simulacion de dado
import random

def Simulacion_dado():
    tiros=0
    while True:
        resultado =random.randint(1,6)
        tiros +=1
        if resultado == 6:
            break
        return tiros
numero_tiros = Simulacion_dado()
print ("Numero de tiros hasta obtener un 6:",numero_tiros)

##2.5 suma de digitos
def suma_digitos (digitos):
    suma = 0
    while digitos > 0:
        resultado = digitos % 10
        suma += resultado
        digitos //= 10
    return suma
digitos = int(input("Escriba un número:"))
respuesta=suma_digitos(digitos)
print("La suma es:", respuesta)
    