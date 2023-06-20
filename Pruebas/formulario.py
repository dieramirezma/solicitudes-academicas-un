import tkinter as tk
from tkinter import messagebox
valores_formulario = {}
def validar_formulario():
    global valores_formulario,ventana, entry_nombres, entry_apellidos, entry_cedula, entry_telefono, var_tipo_solicitud, entry_area_curricular, entry_comentarios
    nombres = entry_nombres.get()
    apellidos = entry_apellidos.get()
    cedula = entry_cedula.get()
    telefono = entry_telefono.get()
    tipo_solicitud = var_tipo_solicitud.get()
    area_curricular = entry_area_curricular.get()
    comentarios = entry_comentarios.get()

    # Validar campos obligatorios
    if not nombres or not apellidos or not cedula or not telefono or not tipo_solicitud or not area_curricular :
        messagebox.showerror("Error", "Hay campos sin completar")
        return

    # Validar tipo de dato para cedula y telefono
    if not cedula.isdigit() or not telefono.isdigit():
        messagebox.showerror("Error", "Los campos de cédula y teléfono deben ser numéricos")
        return

    valores_formulario = {
            'nombres': nombres,
            'apellidos': apellidos,
            'cedula': cedula,
            'telefono': telefono,
            'tipo_solicitud': tipo_solicitud,
            'area_curricular': area_curricular,
            'comentarios': comentarios
        }
    messagebox.showinfo("Éxito", "El formulario se ha enviado correctamente")
    ventana.destroy()

def mostrar_formulario():
  global ventana, entry_nombres, entry_apellidos, entry_cedula, entry_telefono, var_tipo_solicitud, entry_area_curricular, entry_comentarios
  ventana = tk.Toplevel()
  ventana.title("Formulario de Solicitud")
  
  # Etiquetas y campos de entrada
  label_nombres = tk.Label(ventana, text="Nombres:")
  label_nombres.pack()
  entry_nombres = tk.Entry(ventana)
  entry_nombres.pack()

  label_apellidos = tk.Label(ventana, text="Apellidos:")
  label_apellidos.pack()
  entry_apellidos = tk.Entry(ventana)
  entry_apellidos.pack()

  label_cedula = tk.Label(ventana, text="Cédula:")
  label_cedula.pack()
  entry_cedula = tk.Entry(ventana)
  entry_cedula.pack()

  label_telefono = tk.Label(ventana, text="Teléfono:")
  label_telefono.pack()
  entry_telefono = tk.Entry(ventana)
  entry_telefono.pack()

  label_tipo_solicitud = tk.Label(ventana, text="Tipo de Solicitud:")
  label_tipo_solicitud.pack()

  var_tipo_solicitud = tk.StringVar()
  radio_opcion1 = tk.Radiobutton(ventana, text="Pregrado", variable=var_tipo_solicitud, value=1)
  radio_opcion1.pack()
  radio_opcion2 = tk.Radiobutton(ventana, text="Posgrado", variable=var_tipo_solicitud, value=2)
  radio_opcion2.pack()
  radio_opcion3 = tk.Radiobutton(ventana, text="Otra", variable=var_tipo_solicitud, value=3)
  radio_opcion3.pack()

  label_area_curricular = tk.Label(ventana, text="Programa Curricular:")
  label_area_curricular.pack()
  entry_area_curricular = tk.Entry(ventana)
  entry_area_curricular.pack()

  label_comentarios = tk.Label(ventana, text="Comentarios: (Opcional)")
  label_comentarios.pack()
  entry_comentarios = tk.Entry(ventana)
  entry_comentarios.pack()

  # Botón de enviar
  boton_enviar = tk.Button(ventana, text="Enviar", command=validar_formulario)
  boton_enviar.pack()

  ventana.wait_window(ventana)
  return valores_formulario
