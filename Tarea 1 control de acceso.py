print("------------Control de acceso------------")
usuario = input("Ingrese nombre de usuario: ")
if usuario == 'admin':
    contra = input("Ingrese la contraseña: ")
    if contra == '1234':
        print("Bienvenido, ", usuario)
    else:
        print("Contraseña incorrecta, intente nuevamente")
else:
    print("Usuario incorrecto, intente nuevamente")
    
