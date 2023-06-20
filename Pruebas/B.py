import tkinter as tk

def show_popup():
    def get_text():
        nonlocal text
        text = entry.get()
        root.destroy()

    text = ""  # Variable para almacenar el texto ingresado

    root = tk.Toplevel()
    label = tk.Label(root, text="Ingrese un texto:")
    label.pack()
    entry = tk.Entry(root)
    entry.pack()
    button = tk.Button(root, text="Aceptar", command=get_text)
    button.pack()

    root.wait_window(root)
    return text
