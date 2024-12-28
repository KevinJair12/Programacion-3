import tkinter as tk
from tkinter import ttk, messagebox
import time
from datetime import datetime

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Básica")
        self.geometry("400x600")
        self.configure(bg="#34495E")  # Fondo general de la ventana

        self.numero_actual = ""
        self.numero_anterior = ""
        self.operador = ""
        self.resultado_mostrado = False

        self.crear_widgets()
        self.actualizar_saludo()
        self.actualizar_reloj()

        # Vincular eventos del teclado
        self.bind("<Key>", self.manejar_teclado)
        self.bind("<BackSpace>", lambda event: self.manejar_click("C"))
        self.bind("<Delete>", lambda event: self.manejar_click("Limpiar Historial"))

    def crear_widgets(self):
        # Etiqueta de saludo
        self.bienvenida = tk.Label(self, text="", font=("Arial", 24, "bold"), fg="#1ABC9C", bg="#34495E")
        self.bienvenida.pack(pady=15)

        # Campo de texto para el historial
        self.historial = tk.Text(self, height=5, font=("Arial", 12), bg="#ECF0F1", fg="#34495E", wrap=tk.WORD, relief=tk.GROOVE, bd=2)
        self.historial.pack(pady=10, padx=10, fill=tk.X)
        self.historial.config(state=tk.DISABLED)

        # Campo de texto para el resultado
        self.resultado = tk.Entry(self, font=("Arial", 28), bg="#D5D8DC", fg="#2C3E50", justify="right", relief=tk.SOLID, bd=2)
        self.resultado.pack(pady=10, padx=10, fill=tk.X)
        self.resultado.config(state=tk.DISABLED)

        # Botones
        botones = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('÷', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('×', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('C', 3, 0), ('0', 3, 1), ('.', 3, 2), ('+', 3, 3),
            ('=', 4, 3), ('Limpiar Historial', 4, 0)
        ]

        boton_frame = tk.Frame(self, bg="#34495E")
        boton_frame.pack(pady=15, padx=10, fill=tk.BOTH, expand=True)

        for texto, fila, columna in botones:
            boton = ttk.Button(boton_frame, text=texto, command=lambda t=texto: self.manejar_click(t))
            boton.grid(row=fila, column=columna, padx=8, pady=8, sticky="nsew")

        for i in range(5):
            boton_frame.rowconfigure(i, weight=1)
            boton_frame.columnconfigure(i, weight=1)

        # Etiqueta del reloj
        self.reloj = tk.Label(self, font=("Courier", 16), fg="#1ABC9C", bg="#34495E")
        self.reloj.pack(pady=10)

        # Etiqueta del crédito
        credito = tk.Label(self, text="By: Kevin Intriago", font=("Arial", 10), fg="#ECF0F1", bg="#34495E")
        credito.pack(anchor="w", padx=10, pady=10)

    def manejar_click(self, texto):
        if texto.isdigit() or texto == '.':
            if self.resultado_mostrado:
                self.numero_actual = ""
                self.resultado_mostrado = False
            if texto == '.' and '.' in self.numero_actual:
                return  # Evitar más de un punto decimal
            self.numero_actual += texto
            self.actualizar_resultado(self.numero_actual)
        elif texto in ['+', '-', '×', '÷']:
            if self.numero_actual:
                self.numero_anterior = self.numero_actual
                self.numero_actual = ""
                self.operador = texto
                self.resultado_mostrado = False
        elif texto == '=':
            if self.numero_anterior and self.numero_actual and self.operador:
                try:
                    num1 = float(self.numero_anterior)
                    num2 = float(self.numero_actual)
                    if self.operador == '+':
                        resultado = num1 + num2
                    elif self.operador == '-':
                        resultado = num1 - num2
                    elif self.operador == '×':
                        resultado = num1 * num2
                    elif self.operador == '÷':
                        if num2 == 0:
                            messagebox.showerror("Error", "División por cero no permitida.")
                            self.limpiar()
                            return
                        resultado = num1 / num2
                    self.actualizar_resultado(str(round(resultado, 2)))
                    self.actualizar_historial(f"{self.numero_anterior} {self.operador} {self.numero_actual} = {round(resultado, 2)}")
                    self.numero_actual = str(resultado)
                    self.numero_anterior = ""
                    self.operador = ""
                    self.resultado_mostrado = True
                except Exception as e:
                    messagebox.showerror("Error", f"Ocurrió un error: {e}")
                    self.limpiar()
        elif texto == 'C':
            self.limpiar()
        elif texto == 'Limpiar Historial':
            self.historial.config(state=tk.NORMAL)
            self.historial.delete(1.0, tk.END)
            self.historial.config(state=tk.DISABLED)

    def manejar_teclado(self, event):
        tecla = event.char
        if tecla.isdigit() or tecla == '.':
            self.manejar_click(tecla)
        elif tecla in '+-*/':
            operadores = {'+': '+', '-': '-', '*': '×', '/': '÷'}
            self.manejar_click(operadores[tecla])
        elif tecla == '=' or event.keysym == 'Return':
            self.manejar_click('=')

    def actualizar_resultado(self, texto):
        self.resultado.config(state=tk.NORMAL)
        self.resultado.delete(0, tk.END)
        self.resultado.insert(0, texto)
        self.resultado.config(state=tk.DISABLED)

    def actualizar_historial(self, texto):
        self.historial.config(state=tk.NORMAL)
        self.historial.insert(tk.END, texto + '\n')
        self.historial.config(state=tk.DISABLED)

    def limpiar(self):
        self.numero_actual = ""
        self.numero_anterior = ""
        self.operador = ""
        self.actualizar_resultado("")
        self.resultado_mostrado = False

    def actualizar_reloj(self):
        hora_actual = time.strftime("%H:%M:%S")
        self.reloj.config(text=hora_actual)
        self.after(1000, self.actualizar_reloj)

    def actualizar_saludo(self):
        hora_actual = datetime.now().hour
        if hora_actual < 12:
            saludo = "BUENOS DÍAS"
        elif 12 <= hora_actual < 18:
            saludo = "BUENAS TARDES"
        else:
            saludo = "BUENAS NOCHES"
        self.bienvenida.config(text=saludo)

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
