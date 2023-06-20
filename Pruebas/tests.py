# array = [(1, 'Inscripción de asignaturas'), (2, 'Homologación'), (3, 'Registro para trabajo de grado'), (4, 'Inscripción sobre el máximo de créditos'), (5, 'Cancelación del periodo académico'), (6, 'Retiro del programa'), (7, 'Doble titulación'), (8, 'Inscripción PAE'), (9, 'Práctica de campo'), (10, 'Estímulos a estudiantes'), (11, 'Recurso de reposición'), (12, 'Reserva de cupo'), (13, 'Cancelación de materias'), (14, 'Traslado de créditos BAPI'), (15, 'Cambio de grupo'), (16, 'Desbloqueo de historia académica'), (17, 'Traslado'), (18, 'Reingreso'), (19, 'Movilidad'), (20, 'Condecoración del trabajo de grado'), (21, 'Cambio del tutor'), (22, 'Propuesta del trabajo final'), (23, 'Paz y salvo'), (24, 'Informe de avance'), (25, 'Nombramiento del evaluador'), (26, 'Cambio del objetivo de trabajo final'), (27, 'Admisión segundo plan de estudios'), (28, 'Excención de pago de derechos académicos'), (29, 'Aceptación del grado individual'), (30, 'Beca de posgrado'), (31, 'Grado póstumo'), (32, 'Vinculación de profesor nuevo'), (33, 'Distinción a docentes'), (34, 'Toma de año sabático'), (35, 'Modificación de programas curriculares'), (36, 'Convenio extranjero')]

# print(array[0][1])

from tkinter import Tk, Button, Toplevel, messagebox, StringVar
from tkinter import ttk

def show_table_popup(event):
    global treeview
    selected_item = treeview.focus()
    values = treeview.item(selected_item)['values']
    
    # Crear la ventana emergente
    popup = Toplevel()
    
    # Crear las variables StringVar para almacenar los valores modificados
    var1 = StringVar(value=values[0])
    var2 = StringVar(value=values[1])
    var3 = StringVar(value=values[2])
    var4 = StringVar(value=values[3])
    var5 = StringVar(value=values[4])
    var6 = StringVar(value=values[5])
    var7 = StringVar(value=values[6])
    var8 = StringVar(value=values[7])

    
    # Mostrar los valores de la fila seleccionada en la ventana emergente
    entry7 = ttk.Entry(popup, textvariable=var7)
    
    entry7.pack(padx=20, pady=5)

    
    def save_changes():
        # Obtener los nuevos valores modificados
        new_value1 = var1.get()
        new_value2 = var2.get()
        new_value3 = var3.get()
        new_value4 = var4.get()
        new_value5 = var5.get()
        new_value6 = var6.get()
        new_value7 = var7.get()
        new_value8 = var8.get()
        
        # Actualizar los valores en la tabla
        treeview.item(selected_item, values=(new_value1, new_value2, new_value3,new_value4,new_value5,new_value6,new_value7,new_value8))
        
        # Cerrar la ventana emergente
        popup.destroy()
        messagebox.showinfo("Éxito", "Los cambios han sido guardados.")
    
    # Botón para guardar los cambios
    save_button = ttk.Button(popup, text="Guardar", command=save_changes)
    save_button.pack(padx=20, pady=10)
    
    # Ejecutar la ventana emergente
    popup.mainloop()

def main():
    # Crear la ventana principal
    global treeview
    root = Tk()
    
    # Crear el botón
    button = Button(root, text="Mostrar Tabla")
    button.pack(pady=10)
    
    # Crear el widget Treeview con estilo 'clam' en la ventana principal
    style = ttk.Style(root)
    style.theme_use('clam')
    treeview = ttk.Treeview(root, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"), show="headings")
    treeview.pack()
    
    # Configurar las columnas
    treeview.heading("col1", text="Columna 1")
    treeview.heading("col2", text="Columna 2")
    treeview.heading("col3", text="Columna 3")
    treeview.heading("col4", text="Columna 4")
    treeview.heading("col5", text="Columna 5")
    treeview.heading("col6", text="Columna 6")
    treeview.heading("col7", text="Columna 7")
    treeview.heading("col8", text="Columna 8")
    
    # Agregar filas de ejemplo
    # data = [
    #     ("Dato 1", "Dato 2", "Dato 3"),
    #     ("Dato 4", "Dato 5", "Dato 6"),
    #     ("Dato 7", "Dato 8", "Dato 9")
    # ]
    
    data = [
        (13, 9, 'SIA', 'Facultad', "(2023, 2, 6)", "None", 'Resuelta', 541918572), 
        (14, 31, 'SIA', 'Sede', "(2023, 2, 7)", "None", 'Resuelta', 541918572), 
        (66, 1, 'SIA', 'Carrera', "(2023, 6, 12)", 'None', 'Sin resolver', 541918572), 
        (67, 2, 'SIA', 'Carrera', "(2023, 6, 12)", 'None', 'Sin resolver', 541918572), 
        (68, 2, 'SIA', 'Carrera', "(2023, 6, 12)", 'None', 'Sin resolver', 541918572), 
        (69, 2, 'SIA', 'Carrera', "(2023, 6, 12)", 'None', 'Sin resolver', 541918572), 
        (77, 1, 'SIA', 'Carrera', "(2023, 6, 13)", 'None', 'Sin resolver', 541918572),
        (13, 9, 'SIA', 'Facultad', "(2023, 2, 6)", "None", 'Resuelta', 541918572), 
        (14, 31, 'SIA', 'Sede', "(2023, 2, 7)", "None", 'Resuelta', 541918572), 
        (66, 1, 'SIA', 'Carrera', "(2023, 6, 12)", 'None', 'Sin resolver', 541918572), 
        (67, 2, 'SIA', 'Carrera', "(2023, 6, 12)", 'None', 'Sin resolver', 541918572), 
        (68, 2, 'SIA', 'Carrera', "(2023, 6, 12)", 'None', 'Sin resolver', 541918572), 
        (69, 2, 'SIA', 'Carrera', "(2023, 6, 12)", 'None', 'Sin resolver', 541918572), 
        (77, 1, 'SIA', 'Carrera', "(2023, 6, 13)", 'None', 'Sin resolver', 541918572)
      ]
    
    for row in data:
        treeview.insert("", "end", values=row)
    
    # Configurar colores de fondo alternados para las filas
    for i, row in enumerate(data):
        if i % 2 == 0:
            treeview.item(treeview.identify_row(i), tags=('evenrow',))
        else:
            treeview.item(treeview.identify_row(i), tags=('oddrow',))
    
    # Configurar estilos para las filas alternadas
    style.configure("evenrow", background="#E8F0FE")
    style.configure("oddrow", background="#FFFFFF")
    
    # Ajustar el tamaño de las columnas automáticamente
    for column in ("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"):
        treeview.column(column, width=100, anchor="center")
        treeview.heading(column, anchor="center")
    
    # Configurar el evento para mostrar la ventana emergente al hacer clic en una fila
    treeview.bind("<<TreeviewSelect>>", show_table_popup)
    
    # Ejecutar la ventana principal
    root.mainloop()

if __name__ == "__main__":
    main()
