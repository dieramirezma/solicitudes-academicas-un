import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()

# Crear el Treeview
tree = ttk.Treeview(root)

# Definir las columnas de la tabla
tree['columns'] = ('Nombre', 'Edad')

# Formatear las columnas
tree.column('#0', width=0, stretch=tk.NO)  # Columna invisible
tree.column('Nombre', anchor=tk.CENTER, width=100)
tree.column('Edad', anchor=tk.CENTER, width=100)

# Encabezados de las columnas
tree.heading('#0', text='', anchor=tk.CENTER)
tree.heading('Nombre', text='Nombre', anchor=tk.CENTER)
tree.heading('Edad', text='Edad', anchor=tk.CENTER)

# Insertar datos en la tabla
tree.insert('', 'end', text='1', values=('John Doe', '25'))
tree.insert('', 'end', text='2', values=('Jane Smith', '30'))

# Empacar el Treeview
tree.pack()

# Ejecutar la ventana principal
root.mainloop()
