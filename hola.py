import tkinter as tk
from tkinter import messagebox

# Función para validar que el usuario ingrese un número
def validar(valor):
    try:
        return float(valor)
    except:
        messagebox.showerror("Error", "Escribe un número válido.")
        return None

# Funciones para las conversiones
def metros_a_km(x):
    return x / 1000

def pulgadas_a_metros(x):
    return x * 0.0254

def kg_a_gramos(x):
    return x * 1000

def libras_a_kg(x):
    return x * 0.453592

def segundos_a_minutos(x):
    return x / 60

def horas_a_dias(x):
    return x / 24

# Ventana para cada conversión
def ventana_conversion(titulo, texto, funcion):
    v = tk.Toplevel()
    v.title(titulo)

    etiqueta = tk.Label(v, text=texto)
    etiqueta.pack()

    entrada = tk.Entry(v)
    entrada.pack()

    resultado = tk.Label(v, text="")
    resultado.pack()

    def convertir():
        valor = validar(entrada.get())
        if valor is not None:
            r = funcion(valor)
            resultado.config(text=f"Resultado: {r}")

    boton = tk.Button(v, text="Convertir", command=convertir)
    boton.pack()
