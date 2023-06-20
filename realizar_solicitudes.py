# Registro de datos en MySQL desde una GUI en TkInter
# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren

from tkinter import Toplevel, Entry, messagebox, Label, Frame, Tk, Button,ttk, Scrollbar, VERTICAL, HORIZONTAL,StringVar,END
import mysql.connector  #pip install mysql-connector-python
from datetime import date
import tkinter.font as tkfont 
from tkinter import *
from PIL import Image, ImageTk
import ver_solicitudes
import crear_solicitudes

with open("username.txt", "r") as file:
    username = file.read()

conexion = mysql.connector.connect( host='localhost',
                                    database ='solicitudes_consejo', 
                                    user = 'estudianteX',
                                    password ='12345678')

cur0 = conexion.cursor()
sql0 = cur0.callproc('cedula_estudiante', args=('{}'.format(username),))
for result in cur0.stored_results():
    cedula = (str(result.fetchone())).replace('(','').replace(',','').replace(')','')
cur0.close()

def inserta_producto(perCedulaEstudiante,nomId,solMedio,solComentarios):
    cur = conexion.cursor()
    try:
        sql = cur.callproc('estudiante_crear_solicitud', args=('{}'.format(perCedulaEstudiante),'{}'.format(nomId),'{}'.format(solMedio),'{}'.format(solComentarios)))
    except mysql.connector.Error as error:
        print("Error al ejecutar la consulta: {}".format(error))
    conexion.commit()
    cur.close()

def busca_producto(cedula):
    cur = conexion.cursor()
    sql = cur.callproc('estudiante_ver_solicitud', args=(int('{}'.format(cedula).replace("'",'')),))
    for result in cur.stored_results():
        nombreX = result.fetchall()
    cur.close()
    return nombreX 

def nombres():
    cur = conexion.cursor()
    sql = cur.callproc('solicitudes_nombres')
    for result in cur.stored_results():
        nombreX = result.fetchall()
    cur.close()
    return nombreX 

def requisitos(nombre):
    cur = conexion.cursor()
    sql = cur.callproc('solicitudes_requisitos', args=(int('{}'.format(nombre).replace("'",'')),))
    for result in cur.stored_results():
        nombreX = result.fetchall()
    cur.close()
    return nombreX 

    # def agregar_datos(self):
    #     self.tabla.get_children()
    #     nomId = self.nomId.get()
    #     solMedio = self.solMedio.get()
    #     solComentarios = self.solComentarios.get()
    #     perCedulaEstudiante = cedula
    #     if nomId and solMedio !='':        
    #         inserta_producto(perCedulaEstudiante,nomId,solMedio,solComentarios)
    #         self.buscar()


    # def limpiar_datos(self):
    #     self.tabla.delete(*self.tabla.get_children())
    #     self.nomId.set('')
    #     self.solMedio.set('')
    #     self.solComentarios.set('None')

    # def buscar(self):
    #     nombre_producto = cedula
    #     nombre_producto = str("'" + nombre_producto + "'")
    #     nombre_buscado = busca_producto(nombre_producto)
    #     self.tabla.delete(*self.tabla.get_children())
    #     i = -1
    #     for dato in nombre_buscado:
    #         i= i+1                       
    #         self.tabla.insert('',i, text = nombre_buscado[i][0:1], values=nombre_buscado[i][1:9])
    
    # def buscarnombre(self):
    #     nombres_buscados = nombres()
    #     self.tablanom.delete(*self.tablanom.get_children())
    #     i = -1
    #     for dato in nombres_buscados:
    #         i= i+1                       
    #         self.tablanom.insert('',i, text = nombres_buscados[i][0:1], values=nombres_buscados[i][1:2])

    # def buscarreq(self):
    #     nombre_producto = self.nombresol.get()
    #     nombre_producto = str("'" + nombre_producto + "'")
    #     nombre_buscado = requisitos(nombre_producto)
    #     self.tablareq.delete(*self.tablareq.get_children())
    #     i = -1
    #     for dato in nombre_buscado:
    #         i= i+1                       
    #         self.tablareq.insert('',i, text = nombre_buscado[i][0:1], values=nombre_buscado[i][1:3])



def llamar_interfaz_estudiante():
    def return_home():
        messagebox.showinfo("Principal","Redirigiendo a la ventana principal")
        ventana.destroy()
    def ir_ver_solicitudes():
        messagebox.showinfo("Solicitudes","Redirigiendo a la ventana ver solicitudes")
        ver_solicitudes.llamar_ver_solicitudes()
        
    def ir_crear_solicitudes():
        messagebox.showinfo("Solicitudes","Redirigiendo a la ventana ver solicitudes")
        crear_solicitudes.llamar_crear_solicitudes()
        
    
    font = tkfont.Font(family="Segoe UI")
    ventana = Toplevel()
    ventana.wm_title("Registro de Datos en MySQL")
    ventana.config(bg='gray22')
    ventana.geometry('1500x830')
    ventana.configure(background="#A1EFFA")
    
    frame = Frame(ventana,bg="red")
    frame.pack(fill=Y)

    backgroundimage = PhotoImage(file="imagenes/solicitudes.png")
    Label(frame, image=backgroundimage).pack()
    
    image = Image.open("imagenes/btnprincipal.png")
    photo = ImageTk.PhotoImage(image)
    image2 = Image.open("imagenes/ver_sol.png")
    photo2 = ImageTk.PhotoImage(image2)
    image3 = Image.open("imagenes/crear_sol.png")
    photo3 = ImageTk.PhotoImage(image3)

    home = Button(ventana, image=photo,cursor="hand2", highlightthickness=0, border= 0, command=return_home, bg='#A1EFFA',highlightcolor='#A1EFFA')
    home.place(x=625,y=555)
    ver_sol = Button(ventana, image=photo2,cursor="hand2", highlightthickness=0, border= 0, command=ir_ver_solicitudes, bg='#A1EFFA',highlightcolor='#A1EFFA')
    ver_sol.place(x=450,y=340)
    crear_sol = Button(ventana, image=photo3,cursor="hand2", highlightthickness=0, border= 0, command=ir_crear_solicitudes, bg='#A1EFFA',highlightcolor='#A1EFFA')
    crear_sol.place(x=740,y=340)

    ventana.wait_window(ventana)

