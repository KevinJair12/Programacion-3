
print("Oferta del 20% de descuento por gastos superior a 100$")

gasto = int (input("¿Cual fue el valor de su gasto en la compra?: "))

if gasto > 100:
    descuento = (gasto*0.2)
    total = gasto - descuento
    print("Su gasto es: $", gasto, "\nSu descuento es: $" , descuento ,"\nEl total a pagar es: $", total)
    print("¡Gracias por su compra!")
else:
    print("Su gasto no aplica el descuento, ¡Gracias por su compra!")    
             
