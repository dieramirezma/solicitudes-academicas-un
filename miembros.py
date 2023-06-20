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

def busca_miem(comId):
    cur = conexion.cursor()
    sql = cur.callproc('miembros_del_comite', args=(int('{}'.format(comId).replace("'",'')),))
    for result in cur.stored_results():
        nombreX = result.fetchall()
    conexion.commit()
    cur.close()
    return nombreX 

def llamar_miembros():
    global treeview

    def return_atras():
        messagebox.showinfo("Solicitudes","Redirigiendo a la ventana de comité")
        ventana.destroy()
        
    font = tkfont.Font(family="Segoe UI")
    ventana = Toplevel()
    ventana.wm_title("Registro de Datos en MySQL")
    ventana.config(bg='gray22')
    ventana.geometry('1500x830')
    ventana.configure(background="#A1EFFA")
    
    frame = Frame(ventana,bg="red")
    frame.pack(fill='both', expand=True)

    backgroundimage = PhotoImage(file="imagenes/miembros_fondo.png")
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
    treeview = ttk.Treeview(ventana, columns=("col1", "col2", "col3"), show="headings")
    
    
    # Configurar las columnas
    treeview.heading("col1", text="Nombres")
    treeview.heading("col2", text="Rol")
    treeview.heading("col3", text="Fecha vinculación")

    
    
    solicitudes = busca_miem(1)
    # solicitudes = [
    #     (13, 9, 'SIA', 'Facultad', "(2023, 2, 6)", "None", 'Resuelta', 541918572), 
    #     (14, 31, 'SIA', 'Sede', "(2023, 2, 7)", "None", 'Resuelta', 541918572), 
    #     (66, 1, 'SIA', 'Carrera', "(2023, 6, 12)", 'None', 'Sin resolver', 541918572), 
    #     (67, 2, 'SIA', 'Carrera', "(2023, 6, 12)", 'None', 'Sin resolver', 541918572), 
    #     (68, 2, 'SIA', 'Carrera', "(2023, 6, 12)", 'None', 'Sin resolver', 541918572), 
    #     (69, 2, 'SIA', 'Carrera', "(2023, 6, 12)", 'None', 'Sin resolver', 541918572), 
    #     (77, 1, 'SIA', 'Carrera', "(2023, 6, 13)", 'None', 'Sin resolver', 541918572)
    #   ]
    for row in solicitudes:
        treeview.insert("", "end", values=(row[0],row[1],row[2]))
    
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
    for column in ("col1", "col2", "col3"):
        treeview.column(column, width=100, anchor="center")
        treeview.heading(column, anchor="center")
    
    # Configurar el evento para mostrar la ventana emergente al hacer clic en una fila
    # treeview.bind("<<TreeviewSelect>>", show_table_popup)
    
    # Mostrar la tabla en la interfaz
    treeview.pack()
    treeview.place(x=550,y=250)
    ventana.wait_window(ventana)