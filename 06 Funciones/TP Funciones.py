
# 1

def tabla_multiplicar(num):
    resultados = []
    for i in range(1,11):
        producto = num * i
        resultados.append(producto)
    return resultados


# 2

def suma_pares(lista_enteros):
    suma = 0 
    for numero in lista_enteros:
        if numero % 2 == 0:
            suma += numero
    return suma
#Una de las ventajas de usar una función en lugar de código inline
#es que se simplifica el código, haciéndolo más ligero y fácil de manejar

# 3 

def rectangulo(longitud, anchura):
    area = longitud * anchura
    perimetro = 2 * (longitud + anchura)
    return [area, perimetro] #Tupla, para poder tomar cada resultado por separado más fácil

# Ejemplo de uso
l = 10
a = 5
resultado = rectangulo(l, a)
print(f"Lóngitud: {l}, Anchura: {a}")
print(f"El área es: {resultado[0]}")
print(f"El perímetro es: {resultado[1]}")

# Usé tupla en lugar de lista porque son inmutables, para que no se alteren luego en el código por accidente

# Para validar que las dimensiones sean positivas, puedo agregar una estructura "if" con un raise ValueError

# 4
def convertir_temperatura(celcius, unidad_destino):

    unidad_destino = unidad_destino.upper()

    if unidad_destino == "F":
        fahrenheit = celcius * 9/5 + 32
        return fahrenheit
    elif unidad_destino == "K":
        kelvin = celcius + 273.15
        return kelvin
    else:
        return "Unida de destino no válida. Use 'F' o 'K'."
    
# Si se ingresa una unidad no válida, la ejecución pasa al else del bloque condicional
# para extender esto, usaría estructuras 'elif'

# 5
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % 1 == 0:
            return False
    return True

# Para números grandes, lo que haría es usar range(2, int(numero**0,5)+1) para reducir 
# las iteraciones necesarias

# 6
def promedio_calificaciones(notas):
    if not notas:
        return 0
    suma_total = sum(notas)
    cantidad_notas = len(notas)
    promedio = suma_total / cantidad_notas
    return promedio
notas_ejemplo = [8.5, 9.0, 7.5, 8.0]
print(f"El promedio de {notas_ejemplo} es {promedio_calificaciones(notas_ejemplo)}")
lista_vacia = []
print(f"El promedio de una lista vacía es: {promedio_calificaciones(lista_vacia)}")

# 7
def validar_entrada(numero):
    if not isinstance(numero, int):
        return False, "Error: La entrada debe ser un número entero."
    if numero < 0:
        return False, "Error: El número debe ser no negativo (0 o mayor)"
    return True, " "
def factorial (n):
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1)
        resultado *= i
    
    return resultado
def programa_principal():
    try:
        entrada = input("Introduce un número entero no negativo para calcular su factorial: ")
        num = int(entrada)
    except ValueError:
        print("Error: La entrada no es un número entero válido")
        return

es_valido, mensaje_error = validar_entrada(num)

if es_valido:
    f = factorial(num)
    print(f"El factorial de {num} ({num!} es: {f})")
else:
    print(mensaje_error)

programa_principal()

# 8
def es_divisible(dividendo, divisor):
    if divisor == 0:
        return False
    return dividendo % divisor == 0

def es_plimo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if es_divisible(numero, i):
            return False
    return True
def programa_principal():
    try:
        entrada = input("Introduce un número entero positivo:")
        num = int(entrada)

        if num < 1:
            print("Error: El número debe ser positivo.")
            return
        if es_primo(num):
            print(f"El número {num} es primo.")
        else:
            print(f"El número {num} NO es primo.")
        
    except ValueError:
        print("Error: Entrada no válida. Por favor, introduce un número entero.")
    
    programa_principal()

# 9
def convertir_a_fahrenheit(celcius):
    return celcius * 9/5 + 32
def convertir_a_kelvin(celcius):
    return celcius + 273.15

def menu_conversion():
    print("Unidades de Destino")
    print("1: Fahrenheit (F)")
    print("2: Kelvin (K)")

    opcion = input("Elige la unidad de destino (1 o 2): ")
    return opcion

def programa_principal():
    try:
        temp_celcius = float(input("Introduce la temperatura en Celcius: "))
    except ValueError:
        print("Error: Por favor, introduce un número válido para la temperatura.")
        return
    if opcion_menu == "1":
        resultado = convertir_a_fahrenheit(temp_celcius)
        print(f"\n Resultado: {temp_celcius}°C es {resultado:.2f}°F (Fahrenheit)")
    elif opcion_menu == "2":
        resultado = convertir_a_kelvin(temp_celcius)
        print(f"\ Resultado: {temp_celcius}°C es {resultado: .2f}°K (Kelvin)")
    else:
        print("\n Opción no válida. Por favor, elige '1' o '2'.")
programa_principal()

# 10
def calcular_area(longitud, anchura):
    return longitud * anchura

def calcular_perimetro(longitud, anchura):
    return 2 * (longitud + anchura)

def validar_dimensiones(longitud, anchura):
    if longitud > 0 and anchura > 0:
        return True, ""
    else:
        return False, "Error: Ambas dimensiones deben ser números positivos"
    
def programa_principal():
    print("Calculadora de rectángulo")
    try:
        longitud = float(input("Introduce la longitud: "))
        anchura = float(input("Introduce la anchura: "))
    except ValueError:
        print("Error: Valor incorrecto")
        return
    if es_valido:
        area = calcular_area(longitud, anchura)
        perimetro = calcular_perimetro(longitud, anchura)

        print("\n RESULTADOS")
        print(f"Longitud: {longitud}, Anchura: {anchura}")
        print(f"Área: {area:.2f}")
        print(f"Perímetro: {perimetro:.2f}")
    else:
        print(f"\n {mensaje_error}")
    
programa_principal()