import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import formulario

datos_form = {}

def buscar_documentos():
    rutas_documentos = filedialog.askopenfilenames(
        title="Seleccionar documentos",
        filetypes=(("Archivos PDF", "*.pdf"), ("Todos los archivos", "*.*"))
    )
    if rutas_documentos:
        for ruta in rutas_documentos:
            mostrar_icono_con_texto(ruta)

def mostrar_icono_con_texto(ruta):
    imagen = Image.open("imagenes/pdf.png")  # Reemplaza "icono_archivo.png" con la ruta de tu propio icono
    imagen = imagen.resize((50, 50))  # Ajusta el tamaño del icono según tus preferencias
    icono = ImageTk.PhotoImage(imagen)
    
    # Crear un Frame para contener el icono, el nombre del archivo y el botón de eliminar
    frame_archivo = tk.Frame(ventana)
    frame_archivo.pack(anchor=tk.W)
    
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

def llamar_form():
  global datos_form
  valores_formulario = formulario.mostrar_formulario()
  datos_form = valores_formulario
  mostrar_resultado()
  
def mostrar_resultado():
    resultado_text.delete("1.0", tk.END)  # Borrar el contenido existente en el campo de texto
    resultado_text.insert(tk.END, str(datos_form))

ventana = tk.Tk()

boton_buscar = tk.Button(ventana, text="Buscar documentos", command=buscar_documentos)
boton_buscar.pack()


boton_mostrar_formulario = tk.Button(ventana, text="Mostrar formulario", command=llamar_form)
boton_mostrar_formulario.pack()
resultado_text = tk.Text(ventana, height=10, width=30)
resultado_text.pack()

ventana.mainloop()
