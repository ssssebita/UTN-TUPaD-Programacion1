# 1

for i in range (0, 101):
    print(i)

# 2

num = input("Ingresa un número entero y te digo cuantos dígitos tiene: ")
#Esto es para sacar el signo y además trabajar con un string
num_abs_str = num.lstrip("-")

if num_abs_str.isdigit():
    digitos = len(num_abs_str)
    print(f"El número {num} tiene {digitos} dígito(s)")
else:
    print("Error: Entrada no válida. Tenés que ingresar un número entero")

#3

try:
    num1 = int(input("Ingresa el primero número entero: "))
    num2 = int(input("Ingresa el segundo número entero: "))
except ValueError:
    print("Error: Ingresá solo números enteros")
    exit()

if num1 < num2:
    num_inicio = num1
    num_fin = num2
else:
    num_inicio = num2
    num_fin = num1

suma_total = 0

for numero in range(num_inicio + 1, num_fin):
    suma_total += numero

print (f"Los números a sumar están entre {num_inicio} y {num_fin} (excluidos).")
print(f"La suma de los números enteros comprendidos es: {suma_total}")

#4

suma_total = 0
print("---Sumador de secuencia (Escribí 0 para detener)---")

while True:
    try:
        entrada = input("Ingresá un número entero (o 0 para ver el total)")
        numero = int(entrada)

        if numero == 0:
            break
        suma_total += numero
        print(f"Número añadido, la suma hasta ahora es: {suma_total}")
    except ValueError:
        print("Error: Escribí solo números enteros")
        continue
print("\n---Fin del cálculo---")
print(f"Se ingresó 0. La suma total acumulada es: {suma_total}")

#5

import random
#Acá genero un número aleatorio entre 0 y 9
numero_secreto = random.randint(0, 9)
intentos = 0
adivinanza = -1 #Para inicializar con un valor que no sea el secreto

print("Adiviná el número")
print("Estoy pensando un número entre 0 y 9, cuál pensás que es?")

while adivinanza != numero_secreto:
    try:
        adivinanza = int(input("Ingresá tu adivinanza: "))
        intentos += 1

        if adivinanza < numero_secreto:
            print("\X\Demasiado bajo, es más")
        elif adivinanza > numero_secreto:
            print("\X\Demasiado alto, bajá un poco")
    except ValueError:
        print("Error: Ingresá solo números enteros")
print("Felicidades, adivinaste el número!!")
print(f"El número secreto era {numero_secreto}!")
print(f"Te tomó {intentos} intentos :))")

#6

for i in range (100, 0, -2):
    print(i)

#7

try:
    limite = int(input("Decime un número entero positivo: "))
except ValueError:
    print("Error, ingresá un número entero positivo")
    exit()

if limite < 0:
    print("Error: El programa requiere de un número entero positvo")
    exit()

suma_total = 0

for i in range(limite + 1):
    suma_total += i

print(f"La suma de todos los números desde 0 hasta {limite} es {suma_total}")

#8

cantidad_a_ingresar = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Clasificador de {cantidad_a_ingresar} numeros")
print("Ingresá 0 para el neutro")

for i in range(cantidad_a_ingresar):
    while True:
        try:
            entrada = input(f"Ingresá el úmero {i + 1} de {cantidad_a_ingresar}: ")
            numero = int(entrada)
            break
        except ValueError:
            print("Error: Ingresá solo números enteros válidos")

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("--- RESUMEN DE CLASIFICACIÓN ---")
print(f"Números ingresados: {cantidad_a_ingresar}")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

#9

cantidad_a_ingresar = 5

suma_total = 0

print(f"---Calculadora de media de {cantidad_a_ingresar} números")

for i in range(cantidad_a_ingresar):
    while True:
        try:
            entrada = input(f"Ingresá el número {i + 1} de {cantidad_a_ingresar}: ")
            numero = int(entrada)
            suma_total += numero
            break
        except ValueError:
            print("Error: Ingresá números enteros válidos")

media = suma_total / cantidad_a_ingresar

print("---RESULTADO---")
print(f"Suma total de los números: {suma_total}")
print(f"Cantidad de números ingresados {cantidad_a_ingresar}")
print(f"La media (promedio) de los valores es de: {media:.2f}")

#10

cantidad_a_ingresar = 5

suma_total = 0

print(f"---Calculadora de media de {cantidad_a_ingresar} números")

for i in range(cantidad_a_ingresar):
    while True:
        try:
            entrada = input(f"Ingresá el número {i + 1} de {cantidad_a_ingresar}: ")
            numero = int(entrada)
            suma_total += numero
            break
        except ValueError:
            print("Error: Ingresá números enteros válidos")

media = suma_total / cantidad_a_ingresar

print("---RESULTADO---")
print(f"Suma total de los números: {suma_total}")
print(f"Cantidad de números ingresados {cantidad_a_ingresar}")
print(f"La media (promedio) de los valores es de: {media:.2f}")