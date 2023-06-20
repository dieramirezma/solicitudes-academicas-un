# Registro de datos en MySQL desde una GUI en TkInter
# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren

from tkinter import Toplevel, Entry, Label, Frame, Tk, Button,ttk, Scrollbar, VERTICAL, HORIZONTAL,StringVar,END, messagebox
import mysql.connector  #pip install mysql-connector-python
 
class Registro_datos():
    def __init__(self):
        self.conexion = mysql.connector.connect( host='localhost',
                                            database ='solicitudes_consejo', 
                                            user = 'admin1',
                                            password ='A12345678')

    def inserta_producto(self,solId,nomId,solMedio,solTipo,solFechaEnvio,solComentarios,solEstado,perCedulaEstudiante):
        cur = self.conexion.cursor()
        sql='''INSERT INTO vw_estudiante_solicitudes (solId,nomId,solMedio,solTipo,solFechaEnvio,solComentarios,solEstado,perCedulaEstudiante) 
        VALUES('{}','{}','{}','{}','{}','{}','{}','{}')'''.format(solId,nomId,solMedio,solTipo,solFechaEnvio,solComentarios,solEstado,perCedulaEstudiante)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()


    def mostrar_productos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM vw_estudiante_solicitudes " 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_producto(self, cedula):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM vw_estudiante_solicitudes WHERE perCedulaEstudiante = {}".format(cedula)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()
        return nombreX 

    def elimina_productos(self,solId):
        cur = self.conexion.cursor()
        sql='''DELETE FROM vw_estudiante_solicitudes WHERE solId = {}'''.format(solId)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()


class Registro(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
                                    
        self.frame1 = Frame(master)
        self.frame1.grid(columnspan=2, column=0,row=0)
        self.frame2 = Frame(master, bg='light grey')
        self.frame2.grid(column=0, row=1)
        self.frame3 = Frame(master)
        self.frame3.grid(rowspan=2, column=1, row=1)

        self.frame4 = Frame(master, bg='black')
        self.frame4.grid(column=0, row=2)

        self.solId = StringVar()
        self.nomId = StringVar()
        self.solMedio = StringVar()
        self.solTipo = StringVar()
        self.solFechaEnvio = StringVar()
        self.solComentarios = StringVar()
        self.solEstado = StringVar()
        self.perCedulaEstudiante = StringVar()

        self.base_datos = Registro_datos()
        self.create_wietgs()

    def create_wietgs(self):
        Label(self.frame1, text = 'S I S T E M A \t S O L I C I T U D E S \t D E \t A D M I N I S T R A D O R',bg='gray22',fg='white', font=('Orbitron',15,'bold')).grid(column=0, row=0)
        
        Label(self.frame2, text = 'Enviar solicitud',fg='white', bg ='indianred4', font=('Rockwell',12,'bold')).grid(columnspan=2, column=0,row=0, pady=5)
        Label(self.frame2, text = 'solId',fg='white', bg ='indianred4', font=('Rockwell',13,'bold')).grid(column=0,row=1, pady=15)
        Label(self.frame2, text = 'nomId',fg='white', bg ='indianred4', font=('Rockwell',13,'bold')).grid(column=0,row=2, pady=15)
        Label(self.frame2, text = 'solMedio',fg='white', bg ='indianred4', font=('Rockwell',13,'bold')).grid(column=0,row=3, pady=15)
        Label(self.frame2, text = 'solTipo',fg='white', bg ='indianred4', font=('Rockwell',13,'bold')).grid(column=0,row=4, pady=15)
        Label(self.frame2, text = 'solFechaEnvio', fg='white',bg ='indianred4', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=15)
        Label(self.frame2, text = 'solComentarios',fg='white', bg ='indianred4', font=('Rockwell',13,'bold')).grid(column=0,row=6, pady=15)
        Label(self.frame2, text = 'solEstado',fg='white', bg ='indianred4', font=('Rockwell',13,'bold')).grid(column=0,row=7, pady=15)

        Entry(self.frame2,textvariable=self.solId , font=('Arial',12)).grid(column=1,row=1, padx =5)
        Entry(self.frame2,textvariable=self.nomId , font=('Arial',12)).grid(column=1,row=2)
        Entry(self.frame2,textvariable=self.solMedio , font=('Arial',12)).grid(column=1,row=3)
        Entry(self.frame2,textvariable=self.solTipo , font=('Arial',12)).grid(column=1,row=4)
        Entry(self.frame2,textvariable=self.solFechaEnvio , font=('Arial',12)).grid(column=1,row=5)
        Entry(self.frame2,textvariable=self.solComentarios , font=('Arial',12)).grid(column=1,row=6)
        Entry(self.frame2,textvariable=self.solEstado , font=('Arial',12)).grid(column=1,row=7)

        Label(self.frame4, text = 'Botones',fg='white', bg ='black', font=('Rockwell',12,'bold')).grid(columnspan=3, column=0,row=0, pady=1, padx=4)         
        Button(self.frame4,command= self.agregar_datos, text='Enviar solicitud', font=('Arial',10,'bold'), bg='indianred4').grid(column=0,row=1, pady=10, padx=4)
        Button(self.frame4,command = self.limpiar_datos, text='Limpiar', font=('Arial',10,'bold'), bg='indianred4').grid(column=1,row=1, padx=10)        
        Button(self.frame4,command = self.eliminar_fila, text='Eliminar', font=('Arial',10,'bold'), bg='indianred4').grid(column=2,row=1, padx=4)
        Button(self.frame4,command = self.buscar_nombre, text='Buscar por cédula', font=('Arial',8,'bold'), bg='indianred4').grid(columnspan=2,column = 1, row=2)
        Entry(self.frame4,textvariable=self.perCedulaEstudiante , font=('Arial',12), width=20).grid(column=0,row=2, pady=1, padx=8)
        Button(self.frame4,command = self.mostrar_todo, text='Mostrar tabla completa', font=('Arial',10,'bold'), bg='indianred4').grid(columnspan=3,column=0,row=3, pady=8)


        self.tabla = ttk.Treeview(self.frame3, height=30)
        self.tabla.grid(column=0, row=0)

        ladox = Scrollbar(self.frame3, orient = HORIZONTAL, command= self.tabla.xview)
        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy = Scrollbar(self.frame3, orient =VERTICAL, command = self.tabla.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.tabla.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
       
        self.tabla['columns'] = ('nomId','solMedio','solTipo','solFechaEnvio','solComentarios','solEstado','perCedulaEstudiante')

        self.tabla.column('#0', minwidth=100, width=120, anchor='center')
        self.tabla.column('nomId', minwidth=100, width=120 , anchor='center')
        self.tabla.column('solMedio', minwidth=100, width=120, anchor='center' )
        self.tabla.column('solTipo', minwidth=100, width=120, anchor='center')
        self.tabla.column('solFechaEnvio', minwidth=100, width=120, anchor='center')
        self.tabla.column('solComentarios', minwidth=100, width=120, anchor='center')
        self.tabla.column('solEstado', minwidth=100, width=120, anchor='center')
        self.tabla.column('perCedulaEstudiante', minwidth=100, width=120, anchor='center')

        self.tabla.heading('#0', text='solId', anchor ='center')
        self.tabla.heading('nomId', text='nomId', anchor ='center')
        self.tabla.heading('solMedio', text='solMedio', anchor ='center')
        self.tabla.heading('solTipo', text='solTipo', anchor ='center')
        self.tabla.heading('solFechaEnvio', text='solFechaEnvio', anchor ='center')
        self.tabla.heading('solComentarios', text='solComentarios', anchor ='center')
        self.tabla.heading('solEstado', text='solEstado', anchor ='center')
        self.tabla.heading('perCedulaEstudiante', text='perCedulaEstudiante', anchor ='center')


        estilo = ttk.Style(self.frame3)
        estilo.theme_use('alt') #  ('clam', 'alt', 'default', 'classic')
        estilo.configure(".",font= ('Helvetica', 12, 'bold'), foreground='red2')        
        estilo.configure("Treeview", font= ('Helvetica', 10, 'bold'), foreground='black',  background='white')
        estilo.map('Treeview',background=[('selected', 'green2')], foreground=[('selected','black')] )

        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)  # seleccionar  fila
        

    def agregar_datos(self):
        self.tabla.get_children()
        solId = self.solId.get()
        nomId = self.nomId.get()
        solMedio = self.solMedio.get()
        solTipo = self.solTipo.get()
        solFechaEnvio = self.solFechaEnvio.get()
        solComentarios = self.solComentarios.get()
        solEstado = self.solEstado.get()
        perCedulaEstudiante = self.perCedulaEstudiante.get()
        datos = (nomId,solMedio,solTipo,solFechaEnvio,solComentarios,solEstado,perCedulaEstudiante)
        if solId and nomId and solMedio and solTipo and solFechaEnvio and solComentarios and solEstado !='':        
            self.tabla.insert('',0, text = solId, values=datos)
            self.base_datos.inserta_producto(solId,nomId,solMedio,solTipo,solFechaEnvio,solComentarios,solEstado,perCedulaEstudiante)


    def limpiar_datos(self):
        self.tabla.delete(*self.tabla.get_children())
        self.solId.set('')
        self.nomId.set('')
        self.solMedio.set('')
        self.solTipo.set('')
        self.solFechaEnvio.set('')
        self.solComentarios.set('')
        self.solEstado.set('')

    def buscar_nombre(self):
        nombre_producto = self.buscar.get()
        nombre_producto = str("'" + nombre_producto + "'")
        nombre_buscado = self.base_datos.busca_producto(nombre_producto)
        self.tabla.delete(*self.tabla.get_children())
        i = -1
        for dato in nombre_buscado:
            i= i+1                       
            self.tabla.insert('',i, text = nombre_buscado[i][0:1], values=nombre_buscado[i][1:9])


    def mostrar_todo(self):
        self.tabla.delete(*self.tabla.get_children())
        registro = self.base_datos.mostrar_productos()
        i = -1
        for dato in registro:
            i= i+1                       
            self.tabla.insert('',i, text = registro[i][0:1], values=registro[i][1:9])


    def eliminar_fila(self):
        fila = self.tabla.selection()
        if len(fila) !=0:        
            self.tabla.delete(fila)
            nombre = ("'"+ str(self.nombre_borar) + "'")       
            self.base_datos.elimina_productos(nombre)


    def obtener_fila(self, event):
        current_item = self.tabla.focus()
        if not current_item:
            return
        data = self.tabla.item(current_item)
        self.nombre_borar = data['values'][0]

def llamar_interfaz_admin():
    def return_home():
        messagebox.showinfo("Principal","Redirigiendo a la ventana principal")
        ventana.destroy()
        

    ventana = Toplevel()
    ventana.wm_title("Registro de Datos en MySQL")
    ventana.config(bg='gray22')
    ventana.geometry('1366x768')
    ventana.resizable(False, False) 
    app = Registro(ventana)
    home = Button(ventana,text="Principal", fg="white", border=0, bg="#037770", cursor="hand2", command=return_home, justify="center")
    home.place(x=640,y=700)
    ventana.wait_window(ventana)
       