print("------Números primos del 1 al 50-----")

for num in range(2, 51):
    if all(num % i != 0 for i in range(2, num)):
        print(num, end=", ")
