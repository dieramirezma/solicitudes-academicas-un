from tkinter import *
from tkinter import messagebox
import mysql.connector
import tkinter.font as tkfont   
import realizar_solicitudes

def llamar_login_estudiante():
    root = Toplevel()
    root.title("Sistema de inicio de sesión")
    root.geometry("1366x768")
    root.resizable(False, False) 

    font = tkfont.Font(family="Segoe UI", size=15)

    # Imagen de fondo
    frame = Frame(root,bg="red")
    frame.pack(fill=Y)

    backgroundimage = PhotoImage(file="imagenes/loginEst.png")
    Label(frame, image=backgroundimage).pack()

    # Entrada de usuario
    def user_enter(a):
        if user.get() == "Usuario":
            user.delete(0,"end")

    def user_leave(a):
        if user.get() == "":
            user.insert(0,"Usuario")

    user = Entry(frame, width=18, fg="black", border=0, bg="#56E9FE", font=(font), justify="center")
    user.insert(0,"Usuario")
    user.bind("<FocusIn>", user_enter)
    user.bind("<FocusOut>", user_leave)
    user.place(x=580,y=330)

    # Entrada de contraseña
    def password_enter(a):
        if code.get() == "Contraseña":
            code.delete(0,"end")
            code.configure(show="•") 

    def password_leave(a):
        if code.get() == "":
            code.configure(show="")
            code.insert(0,"Contraseña")

    code = Entry(frame, width=18, fg="black", border=0, bg="#56E9FE", font=(font), justify="center")
    code.insert(0,"Constraseña")
    code.bind("<FocusIn>", password_enter)
    code.bind("<FocusOut>", password_leave)
    code.place(x=580,y=370)

    # Boton de Iniciar sesión
    def loginuser():
        global username
        global password
        username = user.get()
        password = code.get()

        if (username=="" or username=="UserID") or (password=="" or password=="Password"): 
            messagebox.showerror("Se deben completar ambos campos")
        else:
            solicitudes_consejo=mysql.connector.connect(host="localhost",user="admin1",password="A12345678",database="solicitudes_consejo")
            mycursor = solicitudes_consejo.cursor()

            command = "select * from loginestudiantes where usuario=%s and contrasena=%s"
            mycursor.execute(command,(username,password))
            myresult = mycursor.fetchone()

            if myresult==None:
                messagebox.showinfo("invalid","Usuario y contraseña invalidos")
            else:
                with open("username.txt", "w") as file:
                    file.write(username)
                messagebox.showinfo("Login","Iniciando sesión")
                root.destroy()
                realizar_solicitudes.llamar_interfaz_estudiante()

    def return_home():
        messagebox.showinfo("Principal","Redirigiendo a la ventana principal")
        root.destroy()

    loginButton = Button(root,text="Iniciar Sesión", fg="white", border=0, bg="#037770", cursor="hand2", font=(font), command=loginuser, justify="center")
    loginButton.place(x=620,y=420)

    home = Button(root,text="Principal", fg="white", border=0, bg="#037770", cursor="hand2", font=(font), command=return_home, justify="center")
    home.place(x=640,y=520)
    root.wait_window(root)