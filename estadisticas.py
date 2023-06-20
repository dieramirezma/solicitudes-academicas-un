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
                                    user = 'estudianteX',
                                    password ='12345678')

cur0 = conexion.cursor()
sql0 = cur0.callproc('cedula_estudiante', args=('{}'.format(username),))
for result in cur0.stored_results():
    cedula = (str(result.fetchone())).replace('(','').replace(',','').replace(')','')
cur0.close()


def llamar_estadisticas():
    def return_atras():
        messagebox.showinfo("Solicitudes","Redirigiendo a la ventana de solicitudes")
        ventana1.destroy()
        
    font = tkfont.Font(family="Segoe UI")
    ventana1 = Toplevel()
    ventana1.wm_title("Registro de Datos en MySQL")
    ventana1.config(bg='gray22')
    ventana1.geometry('1500x830')
    ventana1.configure(background="#A1EFFA")
    
    frame = Frame(ventana1,bg="red")
    frame.pack(fill=Y)

    backgroundimage = PhotoImage(file="imagenes/estadisticas_fondo.png")
    Label(frame, image=backgroundimage).pack()
    
    image = Image.open("imagenes/atras.png")
    photo = ImageTk.PhotoImage(image)

    home = Button(ventana1, image=photo,cursor="hand2", highlightthickness=0, border= 0, command=return_atras, bg='#A1EFFA',highlightcolor='#A1EFFA')
    home.place(x=615,y=555)

    ventana1.wait_window(ventana1)

