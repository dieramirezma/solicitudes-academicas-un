from tkinter import Tk, Button
from tkinter.ttk import Combobox

def imprimir_opcion_seleccionada():
    opcion_seleccionada = combobox.get()
    print(opcion_seleccionada)

# Crear la ventana principal
ventana = Tk()

# Crear una lista de opciones para el Combobox
opciones = ["Opción 1", "Opción 2", "Opción 3"]

# Crear el Combobox y asociarle la lista de opciones
combobox = Combobox(ventana, values=opciones)

# Establecer un valor por defecto
combobox.set("Seleccione una opción")

# Posicionar el Combobox en la ventana
combobox.pack()

# Crear un botón para imprimir la opción seleccionada
boton_imprimir = Button(ventana, text="Imprimir opción seleccionada", command=imprimir_opcion_seleccionada)
boton_imprimir.pack()

# Iniciar el bucle principal de la ventana
ventana.mainloop()
