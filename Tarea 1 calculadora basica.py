print("Calculadora básica de dos números")
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
signo = input("Ingrese un signo de operación (+, -, /, *): ")

if signo == '+':
    suma = n1 + n2
    print("La suma de los dos números es:", suma)
elif signo == '-':
    resta = n1 - n2
    print("La resta de los dos números es:", resta)
elif signo == '/':
    if n2 != 0:
        div = n1 / n2
        print("La división de los dos números es:", div)
    else:
        print("Error: No se puede dividir entre cero.")
elif signo == '*':
    prod = n1 * n2
    print("El producto de los dos números es:", prod)
else:
    print("Operador inválido. Intente de nuevo *")
