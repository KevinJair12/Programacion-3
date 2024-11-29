print("------Mostrar números pares del 1 al 20-----")

for i in range(1, 21):  
    if i % 2 == 0:  
        if i < 20:
            print(i, end=", ")
        else:
            print(i)
