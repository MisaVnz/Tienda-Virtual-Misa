from tkinter import *
import mysql.connector 
from Funciones import limpiar  
from Funciones import cerrar_aplicacion2
import tkinter as tk
from ventanas_emergentes import abrir_ventana_emergente , ventana_tienda, ventana_admin
from tkinter import messagebox 

# Conexion mysql------------------------------------------------
# --------------------------------------------------------------

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    database="tienda_db",
    password="")
# --------------------------------------------------------------
# ---------------Funcion para iniciar sesion--------------------
def iniciar_sesion(e1,e2,mydb):
    mycursor = mydb.cursor()
    usuario = e1.get()
    contraseña = e2.get()
    enlace = "SELECT * FROM `usuarios_tienda` WHERE usuario = %s AND contraseña = %s"
    mycursor.execute(enlace,(usuario, contraseña))
    conexion = mycursor.fetchone()
    if conexion:
        mydb.commit()
        messagebox.showinfo("Datos correctos", "¡Inicio de sesion exitoso!")
        ventana_tienda(ventana,e1,e2)
    else:
        messagebox.showerror("Error de datos","Usuario o contraseña incorrecta")
# --------------------------------------------------------------
# Interfaz de usuarios de la tienda-----------------------------
# --------------------------------------------------------------

ventana = tk.Tk()
ventana.title("LAPTOPSTORE-UNEFA V1.0")
ventana.geometry("800x600")
ventana.configure(bg="#6DEEFF")

logo = PhotoImage(file="Logo.png")
logo = logo.subsample(2, 2)

e1 = Entry(ventana, font="Arial 15")
e1.place(x=400, y=262)
e2 = Entry(ventana, font="Arial 15", show="*")
e2.place(x=400, y=312)

texto1 = Label(ventana, text="Ingresa tu Usuario: ", font="Arial 15", border=3).place(x=180, y=262)
texto2 = Label(ventana, text="Ingresa tu Contraseña: ", font="Arial 15", border=3).place(x=165, y=312)

comentario = Label(ventana, text="Si aun no te has unido a LAPTOPSTORE-UNEFA,\n siempre puedes registrar a un nuevo usuario en el boton de\n registrar, te esperamos con la mejor calidad y precio, ven\n y consigue la laptop que todo ingeniero necesita", background="#D9DE9C", border=5, font="Arial 15")
comentario.place(x=122, y=440)

boton1 = Button(ventana, text="Administrador", border=3, font="Arial 11", command=lambda: ventana_admin(ventana,e1,e2)).place(x=680, y=560)
boton2 = Button(ventana, text="Ingresar", border=3, font="Arial 15",command=lambda: iniciar_sesion(e1,e2,mydb)).place(x=350, y=380)
boton3 = Button(ventana, text="Limpiar", border=3, font="Arial 15", command=lambda: limpiar(e1, e2)).place(x=200, y=380)
boton4 = Button(ventana, text="Registrar",font="Arial 15",border=3, command=lambda: abrir_ventana_emergente(ventana)).place(x=500, y=380)
boton5 = Button(ventana, text="Salir", border=3, font="Arial 11", command=lambda: cerrar_aplicacion2(ventana)).place(x=20, y=560)

logo_label = Label(ventana, image=logo)
logo_label.place(x=235, y=20)

ventana.mainloop()
# --------------------------------------------------------------