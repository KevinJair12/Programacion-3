import random

print("¡Juego de adivinar el número!")
numero_aleatorio = random.randint(1, 10)
intento = int(input("Adivina un número entre 1 y 10: "))

if intento == numero_aleatorio:
    print(f"¡Felicidades! Adivinaste el número {numero_aleatorio}.")
else:
    print(f"Lo siento, no acertaste. El número era {numero_aleatorio}.")
