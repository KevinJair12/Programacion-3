#niño (0-12), adolescente (13-17) o adulto (18+).
print("Clasificacion de edad")
edad = int(input("Ingresa tu edad: "))

if edad>=0:
    if 0<=edad<=12:
        print ("Eres niño/a")
    elif 13<=edad<=17:
        print ("Adolescente")
    else:
        print ("Eres Adulto")
else:
    print ("Edad no valida")
            
