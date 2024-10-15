#1.Ciclo if_else

# ##1.1 Contar letras
def contar_letra (letra):
    letra = letra.lower()
    Med = 'm'

    if letra <= Med:
        return "la letra '{}' esta entre las primeras del alfabeto.".format(letra)
    else:
        return "La letra '{}' esta entre las ultimas del alfabeto.".format(letra)

ingresar_letra=input("Escriba una letra: ")    
resultado1= contar_letra(ingresar_letra)
print(resultado1)

##1.2 Valor de angulos
def cuadrante (angulo):
    
    if angulo < 0:
        angulo += 360
     
    if  0 < angulo < 90:
        return "El ángulo está en el cuadrante 1."
    elif 90 < angulo < 180:
        return "El ángulo está en el cuadrante 2."
    elif 180 < angulo < 270:
        return "El ángulo está en el cuadrante 3."
    else:
        return "El ángulo está en el cuadrante 4."

angulo = float(input("Valor del angulo (°): "))
resultado2 = cuadrante(angulo)
print(resultado2)

##1.3 Rendimiento estudiantes
def Rendimiento_estudiantes(calificacion):
    
    if calificacion > 4.5 :
        return "Excelente"
    elif calificacion >= 3.5 :
        return "Bueno"
    elif calificacion >= 3:
        return "Regular"
    else:
        return "Insuficiente"
 
calificacion_estudiante = float(input ("Ingrese calificacion: "))

resultado3 = Rendimiento_estudiantes(calificacion_estudiante)

print("El rendimiento del estudiantes es:",resultado3)

##1.4 Temperatura
def Clasificacion_temperatura (temperatura):
    
    if temperatura < 18:
        return "Frio"
    elif temperatura <=30:
        return "Templado"
    else:
        return "Cálido"

temperatura = float(input ("Escriba la temperatura en centigrados: "))

resultado4= Clasificacion_temperatura(temperatura)
print("La temperatura es:",resultado4)

##1.5 palabra jengibre
jengibre= input("ingrese la palabra 'Jengibre':")

if jengibre.lower()=="jengibre":
    if jengibre.istitle():
        print("Si, ¡El Jengibre es la mejor planta de todos los tiempos!")
    else:
        print ("No, ¡quiero un gran Jengibre!")
else:
    print("¡Jengibre! No",jengibre)