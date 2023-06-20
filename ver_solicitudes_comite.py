# Registro de datos en MySQL desde una GUI en TkInter
# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren

from tkinter import Toplevel, Entry, messagebox, Label, Frame, Tk, Button,ttk, Scrollbar, VERTICAL, HORIZONTAL,StringVar,END
import mysql.connector  #pip install mysql-connector-python
from datetime import date
import tkinter.font as tkfont 
from tkinter import *
from PIL import Image, ImageTk


with open("username.txt", "r") as file:
    username = file.read()

conexion = mysql.connector.connect( host='localhost',
                                    database ='solicitudes_consejo', 
                                    user = 'comite_sede',
                                    password ='87654321')

def mostrar_sol():
    cur = conexion.cursor()
    sql = cur.callproc('vista_del_comite')
    for result in cur.stored_results():
        nombreX = result.fetchall()
    conexion.commit()
    cur.close()
    return nombreX 

def update(solId, nEstado):
    cur = conexion.cursor()
    sql = cur.callproc('update_estado', args=(int('{}'.format(solId).replace("'",'')),'{}'.format(nEstado)))
    conexion.commit()
    cur.close()

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


    # Mostrar los valores de la fila seleccionada en la ventana emergente
    entry4 = ttk.Entry(popup, textvariable=var4)
    
    entry4.pack(padx=20, pady=5)


    def save_changes():
        global solId
        # Obtener los nuevos valores modificados
        new_value1 = var1.get()
        new_value2 = var2.get()
        new_value3 = var3.get()
        new_value4 = var4.get()

        # Actualizar los valores en la tabla
        treeview.item(selected_item, values=(new_value1, new_value2, new_value3,new_value4))
        
        # Cerrar la ventana emergente
        update(solId, new_value4)
        popup.destroy()
        messagebox.showinfo("Éxito", "Los cambios han sido guardados.")
    
    # Botón para guardar los cambios
    save_button = ttk.Button(popup, text="Guardar", command=save_changes)
    save_button.pack(padx=20, pady=10)
    # save_button.place(x=615, y=300)
    # Ejecutar la ventana emergente
    popup.mainloop()

def llamar_ver_solicitudes_comite():
    global treeview, solId
    solId = 0
    def return_atras():
        messagebox.showinfo("Solicitudes","Redirigiendo a la ventana de solicitudes")
        ventana.destroy()

    def seleccionar_fila(event):
        global solId
        seleccion = treeview.focus()  # Obtener el índice de la fila seleccionada
        valores = treeview.item(seleccion, "values")  # Obtener los valores de la fila seleccionada
        if valores:
            solId = valores[0]  # Obtener el valor de la primera celda (celda 0)
            print(solId)
            # Hacer lo que necesites con el valor de la celda
            
    font = tkfont.Font(family="Segoe UI")
    ventana = Toplevel()
    ventana.wm_title("Registro de Datos en MySQL")
    ventana.config(bg='gray22')
    ventana.geometry('1500x830')
    ventana.configure(background="#A1EFFA")
    
    frame = Frame(ventana,bg="red")
    frame.pack(fill='both', expand=True)

    backgroundimage = PhotoImage(file="imagenes/ver_sol_com_fondo.png")
    Label(frame, image=backgroundimage).pack()
    
    image = Image.open("imagenes/atras.png")
    photo = ImageTk.PhotoImage(image)

    home = Button(ventana, image=photo,cursor="hand2", highlightthickness=0, border= 0, command=return_atras, bg='#A1EFFA',highlightcolor='#A1EFFA')
    home.place(x=615,y=555)

    # Crear el Treeview
    button = Button(ventana, image=photo, text="Mostrar Tabla", bg='#A1EFFA',highlightcolor='#A1EFFA')
    
    
    # Crear el widget Treeview con estilo 'clam' en la ventana principal
    style = ttk.Style(ventana)
    style.theme_use('clam')
    treeview = ttk.Treeview(ventana, columns=("col1", "col2", "col3", "col4"), show="headings")
    
    
    # Configurar las columnas
    treeview.heading("col1", text="Num solicitud")
    treeview.heading("col2", text="Cedula estudiante")
    treeview.heading("col3", text="Tipo")
    treeview.heading("col4", text="Estado")

    solicitudes = mostrar_sol()
    for row in solicitudes:
        treeview.insert("", "end", values=(row[0],row[1],row[2],row[3]))
    
    # Configurar colores de fondo alternados para las filas
    for i, row in enumerate(solicitudes):
        if i % 2 == 0:
            treeview.item(treeview.identify_row(i), tags=('evenrow',))
        else:
            treeview.item(treeview.identify_row(i), tags=('oddrow',))
    
    # Configurar estilos para las filas alternadas
    style.configure("evenrow", background="#E8F0FE")
    style.configure("oddrow", background="#FFFFFF")
    
    # Ajustar el tamaño de las columnas automáticamente
    for column in ("col1", "col2", "col3", "col4"):
        treeview.column(column, width=100, anchor="center")
        treeview.heading(column, anchor="center")
    
    # Configurar el evento para mostrar la ventana emergente al hacer clic en una fila
    treeview.bind("<<TreeviewSelect>>", show_table_popup)
    treeview.bind("<ButtonRelease-1>", seleccionar_fila)
    # Mostrar la tabla en la interfaz
    treeview.pack()
    treeview.place(x=480,y=250)
    ventana.wait_window(ventana)

