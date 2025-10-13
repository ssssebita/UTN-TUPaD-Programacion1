# Trabajo Práctico N°3 Estructuras Condicionales
# Objetivo:  Comprender y aplicar las estructuras condicionales en la programación,
# desarrollando algoritmos que involucren tomas de decisiones.

# 1) Escribir un programa que solicite la edad del usuario. 
# Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad=int(input("Escribí tu edad: "))
if edad>=18:
    print("Es mayor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota=int(input("Decime que nota te sacaste: "))
if nota>=6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares.
# Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par";
# en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

num=int(input("Ingresá un número: "))
if num%2==0:
    print("El número es par")
else:
    print("El número es impar")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# Niño/a: menor de 12 años.
# Adolescente: mayor o igual que 12 años y menor que 18 años.
# Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# Adulto/a: mayor o igual que 30 años.

edad=int(input("Decime tu edad: "))

if edad <12:
    print("Eres un niño/a")
elif edad>=12 and edad<18:
    print("Eres un adolescente")
elif edad>=18 and edad<30:
    print("Eres un adulto joven")
else:
    print("Eres un adulto")
    
# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

pwd=input("Ingrese una contraseña que contenga entre 8 y 14 caracteres: ")
if 8<=len(pwd)<=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
# siguiente:
# from statistics import mode, median, mean
# mi_lista = [1,2,5,5,3]
# En la documentación oficial se puede encontrar más información sobre este paquete:
# https://docs.python.org/es/3.8/library/statistics.html.
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.
# Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.
# Sin sesgo: cuando la media, la mediana y la moda son iguales
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
# forma aleatoria.

import random
from statistics import moda, mediana, media
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print(numeros_aleatorios)
try:
    moda = moda(numeros_aleatorios)
except:
    moda = None 
if media == mediana and mediana == moda:
    print("Resultado: La distribución es simétrica")
elif media> mediana and mediana > moda:
    print("Resultado: Sesgo positivo")
elif media < mediana and mediana < moda:
    print("Resultado: Sesgo negativo")

else:
    print("Resultado: El sesgo no es puro")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

vocales="aeiouAEIOU"

palabra=input("Escribime una palabra: ")

if palabra:
    ultima_letra = palabra[-1]
    
    if ultima_letra in vocales:
        oracion_resultante = palabra + "!"
    else:
        oracion_resultante = palabra
else:
    oracion_resultante = "No ingresaste ninguna palabra."

print(oracion_resultante)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Por favor, ingresa tu nombre: ")
print("Opciones de transformación: ")
print("1. Nombre en mayúsculas")
print("2. Nombre en minúsculas")
print("3. Nombre con la primera letra en mayúscula")

try:
    opcion = int(input("Ingresa el número de la opción deseada: "))
except ValueError:
    print("Error: La opción ingresada no es un número válido.")
    exit()

nombre_transformado = ""

if opcion == 1:
    nombre_transformado = nombre.upper()
    
elif opcion == 2:
    nombre_transformado = nombre.lower()
    
elif opcion == 3:
    nombre_transformado = nombre.title()
    
else:
    print("Error: Opción no válida. Por favor, ingresa 1, 2 o 3.")
    exit()

print(f"Nombre original: {nombre}")
print(f"Resultado de la transformación: {nombre_transformado}")

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

print("--- Clasificador de Terremotos (Escala de Richter) ---")
try:
    magnitud = float(input("Por favor, ingresa la magnitud del terremoto: "))
except ValueError:
    print("Error: La entrada no es un número válido.")
    exit()

categoria = ""

if magnitud < 3.0:
    categoria = "Muy leve (imperceptible)."
    
elif magnitud < 4.0:
    categoria = "Leve (ligeramente perceptible)."
    
elif magnitud < 5.0:
    categoria = "Moderado (sentido por personas, pero generalmente no causa daños)."
    
elif magnitud < 6.0:
    categoria = "Fuerte (puede causar daños en estructuras débiles)."
    
elif magnitud < 7.0:
    categoria = "Muy Fuerte (puede causar daños significativos)."
    
else:
    categoria = "Extremo (puede causar graves daños a gran escala)."

print("Resultado")
print(f"Magnitud ingresada: {magnitud}")
print(f"Clasificación: {categoria}")

# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.
# (según cuadro del PDF)

hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").upper()
mes = input("Ingresa el mes del año: ").lower()
try:
    dia = int(input("Ingresa el día del mes: "))
except ValueError:
    print("Error: El día debe ser un número entero.")
    exit()

meses = {
    "diciembre": 12, "enero": 1, "febrero": 2, "marzo": 3,
    "abril": 4, "mayo": 5, "junio": 6, "julio": 7,
    "agosto": 8, "septiembre": 9, "octubre": 10, "noviembre": 11
}

numero_mes = meses.get(mes, 0)

if numero_mes == 0:
    print("Error: Mes ingresado no válido.")
    exit()
if not (1 <= dia <= 31):
    print("Error: Día fuera del rango normal (1-31).")
    exit()
if hemisferio not in ['N', 'S']:
    print("Error: Hemisferio debe ser 'N' o 'S'.")
    exit()

estacion_norte = ""

if (numero_mes == 12 and dia >= 21) or \
   (numero_mes == 1) or \
   (numero_mes == 2) or \
   (numero_mes == 3 and dia <= 20):
    
    estacion_norte = "Invierno"

elif (numero_mes == 3 and dia >= 21) or \
     (numero_mes == 4) or \
     (numero_mes == 5) or \
     (numero_mes == 6 and dia <= 20):
    
    estacion_norte = "Primavera"

elif (numero_mes == 6 and dia >= 21) or \
     (numero_mes == 7) or \
     (numero_mes == 8) or \
     (numero_mes == 9 and dia <= 20):
    
    estacion_norte = "Verano"

else:
    estacion_norte = "Otoño"


estacion_final = ""

if hemisferio == 'N':
    estacion_final = estacion_norte
elif hemisferio == 'S':
    if estacion_norte == "Invierno":
        estacion_final = "Verano"
    elif estacion_norte == "Verano":
        estacion_final = "Invierno"
    elif estacion_norte == "Primavera":
        estacion_final = "Otoño"
    elif estacion_norte == "Otoño":
        estacion_final = "Primavera"


print(f"Usted se encuentra en {estacion_final}.")