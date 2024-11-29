print("-----Suma de digitos de un numero entero----")
numero = input("Ingrese un número entero: ")

suma = 0

for digito in numero:
    if digito.isdigit(): 
        suma += int(digito)  

print(f"La suma de los dígitos es: {suma}")
