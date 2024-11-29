print("----Cálculo del promedio de calificaciones----")

total = 0
cantidad = 0

while True:
    calificacion = float(input("Ingrese una calificación (o -1 para terminar): "))
    
    if calificacion == -1:
        break  
    
    total += calificacion  
    cantidad += 1  

if cantidad > 0:
    promedio = total / cantidad
    print(f"Promedio: {promedio:.2f}")
else:
    print("No se ingresaron calificaciones válidas.")
