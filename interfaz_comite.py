# Registro de datos en MySQL desde una GUI en TkInter
# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren

from tkinter import Toplevel, Entry, Label, Frame, Tk, Button,ttk, Scrollbar, messagebox, VERTICAL, HORIZONTAL,StringVar,END

import mysql.connector  #pip install mysql-connector-python
import tkinter.font as tkfont 
from tkinter import *
from PIL import Image, ImageTk
import ver_solicitudes_comite
import miembros
import estadisticas
conexion = mysql.connector.connect( host='localhost',
                                    database ='solicitudes_consejo', 
                                    user = 'comite_sede',
                                    password ='87654321')

def mostrar_productos():
    cur = conexion.cursor()
    sql = cur.callproc('vista_del_comite')
    for result in cur.stored_results():
        nombreX = result.fetchall()
    cur.close()
    return nombreX 

def update(solId):
    cur = conexion.cursor()
    sql = cur.callproc('update_estado', args=(int('{}'.format(solId).replace("'",'')),))
    conexion.commit()
    cur.close()

    # def mostrar_todo(self):
    #     self.tabla.delete(*self.tabla.get_children())
    #     registro = mostrar_productos()
    #     i = -1
    #     for dato in registro:
    #         i= i+1                       
    #         self.tabla.insert('',i, text = registro[i][0:1], values=registro[i][1:9])


    # def eliminar_fila(self):
    #     nombre = ("'"+ str(self.solId.get()) + "'")       
    #     update(nombre)
    #     self.mostrar_todo()



def llamar_interfaz_comite():
    def return_home():
        messagebox.showinfo("Principal","Redirigiendo a la ventana principal")
        ventana.destroy()

    def ir_ver_solicitudes():
        messagebox.showinfo("Solicitudes","Redirigiendo a la ventana ver solicitudes")
        ver_solicitudes_comite.llamar_ver_solicitudes_comite()
        
    def ir_miembros():
        messagebox.showinfo("Solicitudes","Redirigiendo a la ventana miembros")
        miembros.llamar_miembros()
    
    def ir_estadisticas():
        messagebox.showinfo("Solicitudes","Redirigiendo a la ventana estadisticas")
        estadisticas.llamar_estadisticas()

    font = tkfont.Font(family="Segoe UI")
    ventana = Toplevel()
    ventana.wm_title("Registro de Datos en MySQL")
    ventana.config(bg='gray22')
    ventana.geometry('1500x830')
    ventana.configure(background="#A1EFFA")

    frame = Frame(ventana,bg="red")
    frame.pack(fill=Y)

    backgroundimage = PhotoImage(file="imagenes/comite.png")
    Label(frame, image=backgroundimage).pack()

    image = Image.open("imagenes/btnprincipal.png")
    photo = ImageTk.PhotoImage(image)
    image2 = Image.open("imagenes/ver_sol_comite.png")
    photo2 = ImageTk.PhotoImage(image2)
    image3 = Image.open("imagenes/miembros.png")
    photo3 = ImageTk.PhotoImage(image3)
    image4 = Image.open("imagenes/estadisticas.png")
    photo4 = ImageTk.PhotoImage(image4)
    
    home = Button(ventana, image=photo,cursor="hand2", highlightthickness=0, border= 0, command=return_home, bg='#A1EFFA',highlightcolor='#A1EFFA')
    home.place(x=620,y=555)

    ver_sol = Button(ventana, image=photo2,cursor="hand2", highlightthickness=0, border= 0, command=ir_ver_solicitudes, bg='#A1EFFA',highlightcolor='#A1EFFA')
    ver_sol.place(x=335,y=340)
    
    miembrosB = Button(ventana, image=photo3,cursor="hand2", highlightthickness=0, border= 0, command=ir_miembros, bg='#A1EFFA',highlightcolor='#A1EFFA')
    miembrosB.place(x=590,y=340)

    estadisticasB = Button(ventana, image=photo4,cursor="hand2", highlightthickness=0, border= 0, command=ir_estadisticas, bg='#A1EFFA',highlightcolor='#A1EFFA')
    estadisticasB.place(x=850,y=340)
    ventana.wait_window(ventana)

     