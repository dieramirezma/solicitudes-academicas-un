# Registro de datos en MySQL desde una GUI en TkInter
# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren

from tkinter import Toplevel, Entry, messagebox, Label, W,LEFT, Frame, Tk, Button,ttk, Scrollbar, VERTICAL, HORIZONTAL,StringVar,END
import mysql.connector  #pip install mysql-connector-python
from datetime import date
import tkinter.font as tkfont 
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from tkinter import filedialog
from tkinter import PhotoImage

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

def nombres():
    cur = conexion.cursor()
    sql = cur.callproc('solicitudes_nombres')
    for result in cur.stored_results():
        nombreX = result.fetchall()
    cur.close()
    return nombreX 

def inserta_sol(perCedulaEstudiante,nomId,solMedio,solComentarios):
    cur = conexion.cursor()
    try:
        sql = cur.callproc('estudiante_crear_solicitud', args=('{}'.format(perCedulaEstudiante),'{}'.format(nomId),'{}'.format(solMedio),'{}'.format(solComentarios)))
    except mysql.connector.Error as error:
        print("Error al ejecutar la consulta: {}".format(error))
    conexion.commit()
    cur.close()

def llamar_crear_solicitudes():
    icono = ""
    def return_atras():
        messagebox.showinfo("Solicitudes","Redirigiendo a la ventana de crear solicitudes")
        ventana.destroy()
        
    font = tkfont.Font(family="Segoe UI")
    ventana = Toplevel()
    ventana.wm_title("Registro de Datos en MySQL")
    ventana.config(bg='gray22')
    ventana.geometry('1500x830')
    ventana.configure(background="#A1EFFA")
    
    frame = Frame(ventana,bg="red")
    frame.pack(fill=Y)

    backgroundimage = PhotoImage(file="imagenes/crear_sol_fondo.png")
    Label(frame, image=backgroundimage).pack()
    
    image = Image.open("imagenes/atras.png")
    photo = ImageTk.PhotoImage(image)

    home = Button(ventana, image=photo,cursor="hand2", highlightthickness=0, border= 0, command=return_atras, bg='#A1EFFA',highlightcolor='#A1EFFA')
    home.place(x=615,y=555)

    valores_formulario = {}
    def validar_formulario():
        tipo_solicitud = var_tipo_solicitud.get()
        comentarios = entry_comentarios.get()

        # Validar campos obligatorios
        if not tipo_solicitud:
            messagebox.showerror("Error", "Hay campos sin completar")
            return


        valores_formulario = {
                'tipo_solicitud': tipo_solicitud,
                'comentarios': comentarios
            }
        messagebox.showinfo("Éxito", "El formulario se ha enviado correctamente")
        txtSol = solicitud.get()
        txtTipo = var_tipo_solicitud.get()
        txtCom = entry_comentarios.get()

        x = 0
        for tupla in opciones:
            if tupla[1] == txtSol:
                x = tupla[0]
                break
        print(x, txtTipo, txtCom)

        nomId = x
        solMedio = "SIA"
        solComentarios = txtCom
        perCedulaEstudiante = cedula

        inserta_sol(perCedulaEstudiante,nomId,solMedio,solComentarios)
        ventana.destroy()

    def buscar_documentos():
        rutas_documentos = filedialog.askopenfilenames(
            title="Seleccionar documentos",
            filetypes=(("Archivos PDF", "*.pdf"), ("Todos los archivos", "*.*"))
        )
        if rutas_documentos:
            for ruta in rutas_documentos:
                mostrar_icono_con_texto(ruta)

    # def mostrar_icono_con_texto(ruta):
    #     global icono
    #     imagen = Image.open("imagenes/pdf.png")  # Reemplaza "icono_archivo.png" con la ruta de tu propio icono
    #     imagen = imagen.resize((50, 50))  # Ajusta el tamaño del icono según tus preferencias
    #     icono = PhotoImage(imagen)
        
    #     # Crear un Frame para contener el icono, el nombre del archivo y el botón de eliminar
    #     vent = Toplevel()
    #     frame_archivo = Frame(ventana)
    #     frame_archivo.pack(anchor="w")
        
    #     label_icono = Label(frame_archivo, image=icono, compound="left")
    #     label_icono.image = icono
    #     label_icono.pack(side="left")
        
    #     nombre_archivo = ruta.split("/")[-1]  # Obtén el nombre del archivo desde la ruta
    #     etiqueta_nombre = Label(frame_archivo, text=nombre_archivo)
    #     etiqueta_nombre.pack(side="left")
        
    #     boton_eliminar = Button(frame_archivo, text="Eliminar", command=lambda: eliminar_archivo(frame_archivo))
    #     boton_eliminar.pack(side="left")
    def mostrar_icono_con_texto(ruta):
        imagen = Image.open("imagenes/pdf.png")  # Reemplaza "icono_archivo.png" con la ruta de tu propio icono
        imagen = imagen.resize((50, 50))  # Ajusta el tamaño del icono según tus preferencias
        icono = ImageTk.PhotoImage(imagen)
        
        # Crear un Frame para contener el icono, el nombre del archivo y el botón de eliminar
        frame_archivo = tk.Frame(ventana,bg="#4CE8FE")
        frame_archivo.pack(anchor=tk.W)
        frame_archivo.place(relx=0.7, rely=0.45)
        
        label_icono = tk.Label(frame_archivo, image=icono, compound=tk.LEFT)
        label_icono.image = icono
        label_icono.pack(side=tk.LEFT)
        
        nombre_archivo = ruta.split("/")[-1]  # Obtén el nombre del archivo desde la ruta
        etiqueta_nombre = tk.Label(frame_archivo, text=nombre_archivo)
        etiqueta_nombre.pack(side=tk.LEFT)
        
        boton_eliminar = tk.Button(frame_archivo, text="Eliminar", command=lambda: eliminar_archivo(frame_archivo))
        boton_eliminar.pack(side=tk.LEFT)

    def eliminar_archivo(frame):
        frame.destroy()  # Elimina el Frame que contiene el archivo

    frame2 = Frame(ventana, width=200, height=200, bg="#A1EFFA")
    frame2.pack(expand=True, anchor="center")

    # Colocar el Frame en el centro de la ventana
    frame2.place(relx=0.5, rely=0.45, anchor="center")
    font_negrita = ("Arial", 12, "bold")
    # Etiquetas y campos de entrada

    opciones = nombres()
    nombres_sol = [opcion[1] for opcion in opciones]
    # Crear el Combobox y asociarle la lista de opciones
    label_solicitud = Label(frame2, bg="#4CE8FE",text="Solicitud a realizar:", font=("Arial", 12, "bold"))
    label_solicitud.config(height=2)
    label_solicitud.pack(pady=3,anchor="center")
    
    solicitud = Combobox(frame2, values=nombres_sol)
    solicitud.pack(pady=3,anchor="center")
    # Establecer un valor por defecto
    solicitud.set("Seleccione una opción")
    
    label_tipo_solicitud = Label(frame2, bg="#4CE8FE",text="Tipo de Solicitud:", font=("Arial", 12, "bold"))
    label_tipo_solicitud.config(height=2)
    label_tipo_solicitud.pack(pady=3,anchor="center")

    var_tipo_solicitud = StringVar()
    radio_opcion1 = Radiobutton(frame2, bg="#4CE8FE",text="Facultad", variable=var_tipo_solicitud, value="Facultad", font=("Arial", 10,"bold"))
    radio_opcion1.pack(pady=3,anchor="center")

    radio_opcion2 = Radiobutton(frame2, bg="#4CE8FE",text="Sede", variable=var_tipo_solicitud, value="Sede", font=("Arial", 10,"bold"))
    radio_opcion2.pack(pady=3,anchor="center")

    radio_opcion3 = Radiobutton(frame2, bg="#4CE8FE", text="CSU", variable=var_tipo_solicitud, value="CSU", font=("Arial", 10,"bold"))
    radio_opcion3.pack(pady=3,anchor="center")

    label_comentarios = Label(frame2, bg="#4CE8FE",text="Comentarios: (Opcional)", font=("Arial", 12,"bold"))
    label_comentarios.config(height=2)
    label_comentarios.pack(pady=3,anchor="center")

    entry_comentarios = Entry(frame2, bg="#4CE8FE",font=("Arial", 10,"bold"))
    entry_comentarios.pack(pady=3,anchor="center")


    label_buscar = Label(frame2, bg="#4CE8FE",text="Adjunte documentos de soporte", font=("Arial", 12,"bold"))
    label_buscar.config(height=2)
    label_buscar.pack(pady=3,anchor="center")
    boton_buscar = Button(frame2,bg="#4CE8FE", text="Buscar documentos", font=("Arial", 12,"bold"),command=buscar_documentos)
    boton_buscar.pack()

    boton_enviar = Button(frame2, bg="#4CE8FE",text="Enviar", font=("Arial", 12,"bold"), command=validar_formulario)
    boton_enviar.pack(pady=3,anchor="center")

    txtSol = solicitud.get()
    txtTipo = var_tipo_solicitud.get()
    txtCom = entry_comentarios.get()

    
    ventana.wait_window(ventana)

