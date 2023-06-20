import tkinter as tk
import B

def open_popup():
    popup_text = B.show_popup()
    if popup_text:
        print("Texto ingresado:", popup_text)

root = tk.Tk()
button = tk.Button(root, text="Abrir ventana emergente", command=open_popup)
button.pack()
root.mainloop()
