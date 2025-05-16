import tkinter as tk
from tkinter import messagebox, ttk

def validar(valor):
    try:
        return float(valor)
    except:
        messagebox.showerror("Error", "Debes ingresar un número válido.")
        return None

def metros_a_km(x): return x / 1000
def pulgadas_a_metros(x): return x * 0.0254
def kg_a_gramos(x): return x * 1000
def libras_a_kg(x): return x * 0.453592
def segundos_a_minutos(x): return x / 60
def horas_a_dias(x): return x / 24

def crear_ventana_conversion(titulo, conversiones):
    ventana = tk.Toplevel()
    ventana.title(titulo)
    ventana.configure(bg="#E0F7FA")

    tk.Label(ventana, text="Selecciona tipo de conversión:", bg="#E0F7FA", font=("Arial", 14)).pack(pady=5)

    opciones = [nombre for nombre, _ in conversiones]
    combo = ttk.Combobox(ventana, values=opciones, state="readonly", font=("Arial", 12))
    combo.current(0)
    combo.pack(pady=5)

    tk.Label(ventana, text="Valor a convertir:", bg="#E0F7FA", font=("Arial", 14)).pack(pady=5)
    entrada = tk.Entry(ventana, font=("Arial", 14))
    entrada.pack(pady=5)

    resultado_label = tk.Label(ventana, text="Resultado:", bg="#E0F7FA", font=("Arial", 14))
    resultado_label.pack(pady=5)

    def convertir():
        valor = validar(entrada.get())
        if valor is not None:
            _, funcion = conversiones[combo.current()]
            resultado = funcion(valor)
            resultado_label.config(text=f"Resultado: {resultado}")

    tk.Button(ventana, text="Convertir", bg="#007ACC", fg="white", font=("Arial", 14), command=convertir).pack(pady=10)

def menu_principal():
    root = tk.Tk()
    root.title("Menú de Conversiones")
    root.configure(bg="#E0F7FA")

    tk.Label(root, text="Selecciona una opción:", bg="#E0F7FA", font=("Arial", 18, "bold")).pack(pady=10)

    tk.Button(root, text="Conversión de Longitud", bg="#007ACC", fg="white", font=("Arial", 14),
              command=lambda: crear_ventana_conversion("Conversión de Longitud",
                                                       [("Metros a Kilómetros", metros_a_km),
                                                        ("Pulgadas a Metros", pulgadas_a_metros)])).pack(pady=5)

    tk.Button(root, text="Conversión de Masa", bg="#007ACC", fg="white", font=("Arial", 14),
              command=lambda: crear_ventana_conversion("Conversión de Masa",
                                                       [("Kilogramos a Gramos", kg_a_gramos),
                                                        ("Libras a Kilogramos", libras_a_kg)])).pack(pady=5)

    tk.Button(root, text="Conversión de Tiempo", bg="#007ACC", fg="white", font=("Arial", 14),
              command=lambda: crear_ventana_conversion("Conversión de Tiempo",
                                                       [("Segundos a Minutos", segundos_a_minutos),
                                                        ("Horas a Días", horas_a_dias)])).pack(pady=5)

    root.mainloop()

menu_principal()
