print("Descubre tu signo zodiacal")
dia = int(input("Ingresa solo tu dia de nacimiento: "))
mes = input("Ingresa solo tu mes de nacimiento: ").lower()  

if (21 <= dia <= 31 and mes == 'marzo') or (1 <= dia <= 19 and mes == 'abril'):
    print("Tu signo es Aries")
elif (20 <= dia <= 30 and mes == 'abril') or (1 <= dia <= 20 and mes == 'mayo'):
    print("Tu signo es Tauro")
elif (21 <= dia <= 31 and mes == 'mayo') or (1 <= dia <= 20 and mes == 'junio'):
    print("Tu signo es Géminis")
elif (21 <= dia <= 30 and mes == 'junio') or (1 <= dia <= 22 and mes == 'julio'):
    print("Tu signo es Cáncer")
elif (23 <= dia <= 31 and mes == 'julio') or (1 <= dia <= 20 and mes == 'agosto'):
    print("Tu signo es Leo")
elif (23 <= dia <= 30 and mes == 'agosto') or (1 <= dia <= 20 and mes == 'septiembre'):
    print("Tu signo es Virgo")
elif (23 <= dia <= 31 and mes == 'septiembre') or (1 <= dia <= 20 and mes == 'octubre'):
    print("Tu signo es Libra")
elif (23 <= dia <= 30 and mes == 'octubre') or (1 <= dia <= 20 and mes == 'noviembre'):
    print("Tu signo es Escorpio")
elif (22 <= dia <= 31 and mes == 'noviembre') or (1 <= dia <= 20 and mes == 'diciembre'):
    print("Tu signo es Sagitario")
elif (22 <= dia <= 30 and mes == 'diciembre') or (1 <= dia <= 20 and mes == 'enero'):
    print("Tu signo es Capricornio")
elif (20 <= dia <= 31 and mes == 'enero') or (1 <= dia <= 20 and mes == 'febrero'):
    print("Tu signo es Acuario")
elif (19 <= dia <= 29 and mes == 'febrero') or (1 <= dia <= 20 and mes == 'marzo'):
    print("Tu signo es Piscis")
else:
    print("Fecha incorrecta")
