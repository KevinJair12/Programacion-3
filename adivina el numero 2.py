import tkinter as tk
import random


class JuegoAdivinarNumero:
    def __init__(self, max_intentos=10, rango=(1, 100)):
        self.max_intentos = max_intentos
        self.intentos_restantes = max_intentos
        self.numero_aleatorio = random.randint(rango[0], rango[1])
        self.rango = rango

    def verificar_intento(self, intento):
        if intento < self.numero_aleatorio:
            return "Demasiado bajo. Intenta con un número más alto."
        elif intento > self.numero_aleatorio:
            return "Demasiado alto. Intenta con un número más bajo."
        else:
            return "¡Correcto! Has adivinado el número."

    def decrementar_intentos(self):
        self.intentos_restantes -= 1

    def restablecer_juego(self):
        self.intentos_restantes = self.max_intentos
        self.numero_aleatorio = random.randint(self.rango[0], self.rango[1])


class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Adivinar Número")
        self.root.geometry("400x300")  
        self.juego = JuegoAdivinarNumero()

        self.root.config(bg="#f0f8ff")  

        self.intentos_label = tk.Label(root, text=f"Intentos restantes: {self.juego.intentos_restantes}", bg="#f0f8ff", font=("Arial", 12))
        self.intentos_label.pack(pady=10)

        self.mensaje_label = tk.Label(root, text="Adivina un número entre 1 y 100", bg="#f0f8ff", font=("Arial", 12))
        self.mensaje_label.pack(pady=10)

        self.intento_entry = tk.Entry(root, font=("Arial", 14), justify="center")
        self.intento_entry.pack(pady=10)

        
        self.adivinar_button = tk.Button(root, text="Adivinar", command=self.adivinar, bg="#4CAF50", fg="white", font=("Arial", 12), relief="raised", bd=3)
        self.adivinar_button.pack(pady=10)

       
        self.reiniciar_button = tk.Button(root, text="Reiniciar", command=self.reiniciar_juego, bg="#FF6347", fg="white", font=("Arial", 12), relief="raised", bd=3)
        self.reiniciar_button.pack(pady=10)

    def adivinar(self):
        try:
            intento = int(self.intento_entry.get())
        except ValueError:
            self.mensaje_label.config(text="Por favor ingresa un número válido.")
            return

        if intento < 1 or intento > 100:
            self.mensaje_label.config(text="El número debe estar entre 1 y 100.")
            return

        self.juego.decrementar_intentos()

        mensaje = self.juego.verificar_intento(intento)
        self.mensaje_label.config(text=mensaje)
        self.intentos_label.config(text=f"Intentos restantes: {self.juego.intentos_restantes}")

        if self.juego.intentos_restantes == 0:
            self.mensaje_label.config(text=f"Has perdido. El número era {self.juego.numero_aleatorio}.")
            self.adivinar_button.config(state=tk.DISABLED)

    def reiniciar_juego(self):
        self.juego.restablecer_juego()
        self.intentos_label.config(text=f"Intentos restantes: {self.juego.intentos_restantes}")
        self.mensaje_label.config(text="Adivina un número entre 1 y 100")
        self.intento_entry.delete(0, tk.END)
        self.adivinar_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
