def par(num):
    return num % 2 == 0  
numero = int(input("Ingrese un número: "))
resultado = par(numero)
print(f"¿El número {numero} es par? {resultado}")
