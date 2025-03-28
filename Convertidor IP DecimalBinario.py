import tkinter as tk
from tkinter import messagebox

# Función para convertir IP decimal a binario
def decimal_a_binario():
    ip_decimal = entrada_decimal.get()
    try:
        octetos = ip_decimal.split('.')
        ip_binaria = '.'.join(format(int(octeto), '08b') for octeto in octetos)
        salida_binaria.set(ip_binaria)
    except ValueError:
        messagebox.showerror("Error", "La IP decimal ingresada no es válida.")

# Función para convertir IP binaria a decimal
def binario_a_decimal():
    ip_binaria = entrada_binaria.get()
    try:
        octetos = ip_binaria.split('.')
        ip_decimal = '.'.join(str(int(octeto, 2)) for octeto in octetos)
        salida_decimal.set(ip_decimal)
    except ValueError:
        messagebox.showerror("Error", "La IP binaria ingresada no es válida.")

# Crear una ventana de conversión para decimal a binario
def ventana_decimal_a_binario():
    nueva_ventana = tk.Toplevel()
    nueva_ventana.title("Convertir IP Decimal a Binario")
    nueva_ventana.geometry("400x200")

    global entrada_decimal, salida_binaria
    entrada_decimal = tk.StringVar()
    salida_binaria = tk.StringVar()

    tk.Label(nueva_ventana, text="Ingrese la IP en Decimal:", font=("Arial", 12)).pack(pady=10)
    tk.Entry(nueva_ventana, textvariable=entrada_decimal, font=("Arial", 12), width=25).pack()
    tk.Button(nueva_ventana, text="Convertir a Binario", command=decimal_a_binario, bg="lightblue").pack(pady=5)
    tk.Entry(nueva_ventana, textvariable=salida_binaria, font=("Arial", 12), width=25, state="readonly").pack()

# Crear una ventana de conversión para binario a decimal
def ventana_binario_a_decimal():
    nueva_ventana = tk.Toplevel()
    nueva_ventana.title("Convertir IP Binaria a Decimal")
    nueva_ventana.geometry("400x200")

    global entrada_binaria, salida_decimal
    entrada_binaria = tk.StringVar()
    salida_decimal = tk.StringVar()

    tk.Label(nueva_ventana, text="Ingrese la IP en Binario:", font=("Arial", 12)).pack(pady=10)
    tk.Entry(nueva_ventana, textvariable=entrada_binaria, font=("Arial", 12), width=25).pack()
    tk.Button(nueva_ventana, text="Convertir a Decimal", command=binario_a_decimal, bg="lightgreen").pack(pady=5)
    tk.Entry(nueva_ventana, textvariable=salida_decimal, font=("Arial", 12), width=25, state="readonly").pack()

# Crear la ventana principal con opciones
def menu_principal():
    ventana = tk.Tk()
    ventana.title("Conversor de IP")
    ventana.geometry("300x200")
    ventana.resizable(False, False)

    tk.Label(ventana, text="Bienvenido al Conversor de IP", font=("Arial", 14)).pack(pady=20)
    tk.Button(ventana, text="IP Decimal a Binario", command=ventana_decimal_a_binario, width=20, bg="lightblue").pack(pady=10)
    tk.Button(ventana, text="IP Binaria a Decimal", command=ventana_binario_a_decimal, width=20, bg="lightgreen").pack(pady=10)
    tk.Button(ventana, text="Salir", command=ventana.quit, width=20, bg="red", fg="white").pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    menu_principal()
