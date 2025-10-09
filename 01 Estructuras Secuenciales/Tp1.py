#Trabajo práctico N°1 Estructuras secuenciales


#Punto 1
print("Hola mundo!")


#Punto 2
nombre=input("Ingrese su nombre: ")
print(f"Hola {nombre}")

#Punto 3
nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
edad=input("Ingrese su edad: ")
nacionalidad=input("Ingrese su nacionalidad: ")
print(f"Mi nombre es {nombre} {apellido}, tengo {edad} años, soy de nacionalidad {nacionalidad}")

#Punto 4
radio=float(input("¿Cuánto vale el radio del círculo?: "))
perimetro=2*3.14*radio
radiocuadrado = radio * radio
area=3.14*radiocuadrado
print(f"El perímetro del círculo es de {perimetro}, mientras que su área es de {area}")

#Punto 5
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas.")

#Punto 6
numero=int(input("Ingrese un número: "))

print(numero, "x 1 =", numero * 1)
print(numero, "x 2 =", numero * 2)
print(numero, "x 3 =", numero * 3)
print(numero, "x 4 =", numero * 4)
print(numero, "x 5 =", numero * 5)
print(numero, "x 6 =", numero * 6)
print(numero, "x 7 =", numero * 7)
print(numero, "x 8 =", numero * 8)
print(numero, "x 9 =", numero * 9)
print(numero, "x 10 =", numero * 10)

#Punto 7
num1 = int(input("Ingrese el primer número (distinto de 0): "))
num2 = int(input("Ingrese el segundo número (distinto de 0): "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

#Punto 8
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura ** 2)
print(f"Su índice de masa corporal es de {imc}")

#Punto 9
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"{celsius} °C equivalen a {fahrenheit} °F.")

#Punto 10
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los tres números es {promedio:}")

#Easter egg, gracias por leer hasta el final
