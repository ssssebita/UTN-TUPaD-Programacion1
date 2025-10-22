# Semana de integración
# El programa solicita dos valores binarios (0 o 1)
# y muestra el resultado de las operaciones AND, OR y NOT 

print("\n--- Simulador de puertas lógicas ---")
print("------------------------------------")
print("\n--- Alumno: Pablo Cama Vera ---")
print("------------------------------------")

print("Ingrese valores binarios (0 o 1) para mostrarle las salidas AND, OR y NOT de cada combinación")

# Input de datos

a = int(input("Ingrese el primer valor binario: "))
b = int(input("Ingrese el segundo valor binario: "))

# If para asegurarse que los valores de a y b sean binarios 

if -1 < a < 2 and -1 < b < 2:
    pass
else:
    print("Error, ingrese solo valores binarios")
    exit()


# Operaciones lógicas
and_resultado = a and b
or_resultado = a or b
not_a = int(not a)
not_b = int(not b)

# Resultados
print("---Resultados---")
print(f"A AND B = {and_resultado}")
print(f"A OR B = {or_resultado}")
print(f"NOT A = {not_a}")
print(f"NOT B = {not_b}")

print("--- Fin del simulador ---")