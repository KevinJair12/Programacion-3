import math  

def area_circulo(radio):
    return math.pi * radio ** 2

radio = float(input("Ingrese el radio del círculo: "))

resultado = area_circulo(radio)
print(f"El área del círculo con radio {radio} es: {resultado:.2f}")
