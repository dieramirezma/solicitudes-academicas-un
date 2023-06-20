from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
from tkinter import ttk
import login_comite
import login_admin
import login_estudiantes

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="db12dieramirezma",
            database="solicitudes_consejo"
        )
        print("Conexión exitosa a la base de datos")
        return connection
    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos:", error)


root = Tk()
root.title("Sistema de inicio de sesión")
root.geometry("1366x768")

root.resizable(False, False) 

# Imagen     de fondo
frame = Frame(root,bg="red")
frame.pack(fill=Y)

backgroundimage = PhotoImage(file="imagenes/inicio.png")
Label(frame, image=backgroundimage).pack()

solicitudes_consejo=mysql.connector.connect(host="localhost",user="admin1",password="A12345678",database="solicitudes_consejo")
basedatos = solicitudes_consejo.cursor()


def interfaz_estudiante():
    messagebox.showinfo("Login","Redirigiendo al login para estudiantes")
    hide_window()
    login_estudiantes.llamar_login_estudiante()
    show_window()

def interfaz_admin():
    messagebox.showinfo("Login","Redirigiendo al login para administradores")
    hide_window()
    login_admin.llamar_login_admin()
    show_window()

def interfaz_comite():
    messagebox.showinfo("Login","Redirigiendo al login para comité")
    hide_window()
    login_comite.llamar_login_comite()
    show_window()

def hide_window():
    root.withdraw()

def show_window():
    root.deiconify()
    
image = Image.open("imagenes/btnEst.png")
photo = ImageTk.PhotoImage(image)

image1 = Image.open("imagenes/btnCom.png")
photo1 = ImageTk.PhotoImage(image1)

image2 = Image.open("imagenes/btnAdm.png")
photo2 = ImageTk.PhotoImage(image2)


iniciosesionboton = Button(root, image=photo2, highlightthickness=0, border= 0,cursor="hand2", command=interfaz_admin,bg='#A1EFFA',highlightcolor='#A1EFFA')
iniciosesionboton.place(x=150,y=400)

iniciosesionboton1 = Button(root, image=photo1, highlightthickness=0, border= 0,cursor="hand2", command=interfaz_comite,bg='#A1EFFA',highlightcolor='#A1EFFA')
iniciosesionboton1.place(x=600,y=400)

estudianteButton = Button(root, image=photo,cursor="hand2", highlightthickness=0, border= 0, command=interfaz_estudiante, bg='#A1EFFA',highlightcolor='#A1EFFA')
estudianteButton.place(x=1050,y=400)
estudianteButton.photo = photo

root.wait_window(root)