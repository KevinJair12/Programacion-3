print("------Factorial de un número-----")

while True:
    try:
        numero = int(input("Ingrese un número entero positivo para mostrar su factorial: "))
        if numero < 0:
            print("Por favor, ingrese un número positivo.")
        else:
            break  
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")

fac = 1
for i in range(1, numero + 1):
    fac *= i

print(f"El factorial de {numero} es: {fac}")
