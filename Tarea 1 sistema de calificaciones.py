print("Sistema de calificaciones")
try:
    cal = float(input("Ingrese una calificación: "))
    if 0 <= cal <= 100:
        if 90 <= cal <= 100:
            print("Su calificación es 'A'")
        elif 80 <= cal <= 89:
            print("Su calificación es 'B'")
        elif 70 <= cal <= 79:
            print("Su calificación es 'C'")
        elif 60 <= cal <= 69:
            print("Su calificación es 'D'")
        elif cal < 60:
            print("Su calificación es 'F'")
    else:
        print("Calificación fuera de rango")
except ValueError:
    print("Ingrese un número válido.")
