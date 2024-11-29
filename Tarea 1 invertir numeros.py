print("----Versión invertida de un número entero----")

numero = input("Ingrese un número entero: ")

if numero.isdigit() or (numero[0] == '-' and numero[1:].isdigit()):
    
    invertido = numero[::-1]
    
    if numero[0] == '-':
        invertido = '-' + invertido[:-1]

    print(f"La versión invertida del número es: {invertido}")
else:
    print("Entrada no válida. Por favor, ingrese un número entero.")
