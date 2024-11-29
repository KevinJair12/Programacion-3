suma = 0  

for numero in range(1, 11):
    if numero < 10:
        print(numero, end=", ")
    else:
        print(numero)
    
    suma += numero  

print("La suma de los 10 primeros números es:", suma)
