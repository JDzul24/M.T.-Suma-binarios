import tkinter as tk
from tkinter import messagebox, ttk

def sumar_binarios(bin1, bin2):
    try:
        suma = bin(int(bin1, 2) + int(bin2, 2))[2:]
        return suma
    except ValueError:
        return "Error: Entrada no válida."


def calcular_suma_acumulada():
    # Limpiar tabla
    for row in tabla.get_children():
        tabla.delete(row)

    # Obtener entradas
    input_completo = entry_binarios_iniciales.get()
    binarios_adicionales = entry_binarios_adicionales.get()

    # Validación del formato de los binarios iniciales
    if len(input_completo) > 2:
        messagebox.showerror("Error", "Los primeros dos números binarios deben tener un máximo de 2 digitos.")
        return
    
    if not input_completo.isdigit() :
        messagebox.showerror("Error", "Los primeros dos números binarios deben ser números.")
        return


    # Validación de entrada de binarios adicionales
    if not binarios_adicionales :
        messagebox.showerror("Error", "Por favor, ingresa los números binarios adicionales.")
        return


    
    try:
      bin1 = input_completo[:1] # Toma primer caracter
      bin2 = input_completo[1:] # Toma segundo caracter
    except IndexError:
        messagebox.showerror("Error", "Ingrese exactamente 2 digitos")
        return



    if not all(bit in '01' for bit in bin1 + bin2):
        messagebox.showerror("Error", "Los primeros dos números binarios deben ser binarios.")
        return


    # Calcular suma y formatear resultado
    resultado = sumar_binarios(bin1, bin2)


    if isinstance(resultado, str) and resultado.startswith("Error"):
        messagebox.showerror("Error", resultado)
        return

    resultado_final = sumar_binarios(str(f"{bin1}{bin2}"), binarios_adicionales)
    if isinstance(resultado_final, str) and resultado_final.startswith("Error"):
        messagebox.showerror("Error", resultado_final)
        return

    # Insertar en la tabla
    tabla.insert("", "end", values=(f"{bin1}{bin2}+{binarios_adicionales}", resultado_final))
    messagebox.showinfo("Resultado", "Suma calculada correctamente")


# Interfaz gráfica
root = tk.Tk()
root.title("Máquina de Sunflower")
root.geometry("500x400")

label_binarios_iniciales = tk.Label(root, text="Primeros dos números binarios:")
label_binarios_iniciales.pack(pady=5)
entry_binarios_iniciales = tk.Entry(root, width=10)
entry_binarios_iniciales.pack(pady=5)


label_binarios_adicionales = tk.Label(root, text="Números binarios adicionales:")
label_binarios_adicionales.pack(pady=5)
entry_binarios_adicionales = tk.Entry(root, width=25)
entry_binarios_adicionales.pack(pady=5)


btn_calcular = tk.Button(root, text="Calcular Suma Acumulativa", command=calcular_suma_acumulada)
btn_calcular.pack(pady=10)

tabla = ttk.Treeview(root, columns=("Input", "Suma Acumulada"), show="headings", height=10)
tabla.heading("Input", text="Input")
tabla.heading("Suma Acumulada", text="Suma Acumulada")
tabla.pack(pady=10)

root.mainloop()