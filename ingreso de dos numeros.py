import tkinter as tk
from tkinter import messagebox


def sumar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 + num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese números válidos.")

def restar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 - num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese números válidos.")

def multiplicar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 * num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese números válidos.")

def dividir():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 == 0:
            messagebox.showerror("Error", "No se puede dividir entre 0.")
        else:
            resultado = num1 / num2
            label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese números válidos.")


ventana = tk.Tk()
ventana.title("Calculadora")


ventana.config(bg="#A3C9E2")


label_num1 = tk.Label(ventana, text="Ingresa el primer número:", bg="#A3C9E2")
label_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num1 = tk.Entry(ventana)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = tk.Label(ventana, text="Ingresa el segundo número:", bg="#A3C9E2")
label_num2.grid(row=1, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(ventana)
entry_num2.grid(row=1, column=1, padx=10, pady=10)


boton_sumar = tk.Button(ventana, text="Sumar", command=sumar, bg="#88D8B0", font=("Arial", 12, "bold"))
boton_sumar.grid(row=2, column=0, padx=10, pady=10)

boton_rest = tk.Button(ventana, text="Restar", command=restar, bg="#FFABAB", font=("Arial", 12, "bold"))
boton_rest.grid(row=2, column=1, padx=10, pady=10)

boton_multiplicar = tk.Button(ventana, text="Multiplicar", command=multiplicar, bg="#F7D06B", font=("Arial", 12, "bold"))
boton_multiplicar.grid(row=3, column=0, padx=10, pady=10)

boton_dividir = tk.Button(ventana, text="Dividir", command=dividir, bg="#A7D8E8", font=("Arial", 12, "bold"))
boton_dividir.grid(row=3, column=1, padx=10, pady=10)


label_resultado = tk.Label(ventana, text="Resultado: ", bg="#A3C9E2")
label_resultado.grid(row=4, column=0, columnspan=2, pady=20)


ventana.mainloop()
