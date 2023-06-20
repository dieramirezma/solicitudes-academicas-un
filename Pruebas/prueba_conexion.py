from tkinter import Toplevel, Entry, messagebox, Label, Frame, Tk, Button,ttk, Scrollbar, VERTICAL, HORIZONTAL,StringVar,END
import mysql.connector  #pip install mysql-connector-python
from datetime import date
import tkinter.font as tkfont 

conexion = mysql.connector.connect( host='localhost',
                                    database ='solicitudes_consejo', 
                                    user = 'estudianteX',
                                    password ='12345678')

# cur0 = conexion.cursor()
# sql0 = cur0.callproc('cedula_estudiante', args=('{}'.format(username),))
# for result in cur0.stored_results():
#     cedula = (str(result.fetchone())).replace('(','').replace(',','').replace(')','')
# cur0.close()

def busca_producto(cedula):
    cur = conexion.cursor()
    sql = cur.callproc('estudiante_ver_solicitud', args=(int('{}'.format(cedula).replace("'",'')),))
    for result in cur.stored_results():
        nombreX = result.fetchall()
    cur.close()
    return nombreX 

print(busca_producto("541918572"))

def nombres():
    cur = conexion.cursor()
    sql = cur.callproc('solicitudes_nombres')
    for result in cur.stored_results():
        nombreX = result.fetchall()
    cur.close()
    return nombreX 

opciones = nombres()
nombres_sol = [opcion[1] for opcion in opciones]
print(nombres_sol)