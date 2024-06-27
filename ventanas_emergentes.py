from tkinter import messagebox
import mysql.connector
from tkinter import *
from Funciones import registrarmysql , buscarsql, ingresar, buscarsql_admin, eliminar_producto
from Funciones import cerrar_aplicacion1, cerrar_aplicacion3, cerrar_aplicacion4,boton_siguiente_admin,boton_atras_admin
from Funciones import gracias , limpiar2, mostrar_imagen , editar_producto, boton_siguiente, boton_atras,limpiar3
import tkinter as tk

#-----------------Conexion mysql de reserva----------------
#----------------------------------------------------------
mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    database = "tienda_db",
    password = "")
#-----------------Ventana de compra------------------------
#----------------------------------------------------------
def ventana_compra(entry2, entry11):
    # Crear una nueva ventana emergente
    ventana_compra = tk.Toplevel()
    ventana_compra.title("Carrito de compras")
    ventana_compra.geometry("500x150")
    ventana_compra.configure(bg="#D9DE9C")
    # Obtener los valores de entry2 y entry11
    valor_entry2 = entry2.get()
    valor_entry11 = entry11.get()

    # Mostrar los valores en la nueva ventana
    tk.Label(ventana_compra, font="Arial 15", text=f"Producto: {valor_entry2}").place(x=20,y=10)
    tk.Label(ventana_compra, font="Arial 15", text=f"Precio a pagar: {valor_entry11}").place(x=20,y=50)

    # Función para el botón de pagar
    def pagar():
        mensaje = "Compra realizada"
        messagebox.showinfo(mensaje,"Gracias por su compra, vuelva pronto :)")
        ventana_compra.destroy()

        print("Pago realizado con éxito")

    # Botón para pagar
    boton_pagar = tk.Button(ventana_compra,font="Arial 15", text="Pagar", command=pagar)
    boton_pagar.place(x=230,y=100)
#-----------------Fin de la Ventana de compra------------------------
#--------------------------------------------------------------------
#--------------------Ventana de Registro-----------------------------
#--------------------------------------------------------------------
def abrir_ventana_emergente(ventana):
    ventana_registro = tk.Toplevel()
    ventana_registro.title("REGISTRO-LAPTOPSTORE-UNEFA V1.0")
    ventana_registro.geometry("800x600")
    ventana_registro.configure(bg="#6DEEFF")
    logo2 = PhotoImage(file="Logo2.png")
    logo2 = logo2.subsample(2, 2)

    entry_nombre = Entry(ventana_registro, font="Arial 15")
    entry_nombre.place(x=400, y=247)
    entry_apellido = Entry(ventana_registro, font="Arial 15")
    entry_apellido.place(x=400, y=297)
    entry_usuario = Entry(ventana_registro, font="Arial 15")
    entry_usuario.place(x=400, y=347)
    entry_contraseña = Entry(ventana_registro, font="Arial 15")
    entry_contraseña.place(x=400, y=397)

    text1 = Label(ventana_registro, text="Ingresa tu Nombre: ", font="Arial 15", border=3).place(x=165, y=245)
    text2 = Label(ventana_registro, text="Ingresa tu Apellido: ", font="Arial 15", border=3).place(x=165, y=295)
    text3 = Label(ventana_registro, text="Ingresa tu Usuario: ", font="Arial 15", border=3).place(x=165, y=345)
    text4 = Label(ventana_registro, text="Ingresa tu Contraseña: ", font="Arial 15", border=3).place(x=145, y=395)

    comentario1 = Label(ventana_registro, text="Bienvenido al registro de LAPTOPSTORE-UNEFA,\n aquí puedes registrarte como nuevo usuario de nuestra tienda\n online, únete y consigue la laptop que todo ingeniero necesita.", background="#D9DE9C", border=5, font="Arial 15")
    comentario1.place(x=122, y=445)

    logo2_label = Label(ventana_registro, image=logo2)  # Utilizar la variable global logo
    logo2_label.place(x=235, y=7)

    boton_salir = Button(ventana_registro, text="Salir", border=3, font="Arial 13", command=lambda: cerrar_aplicacion1(ventana_registro)).place(x=20, y=545)
    boton_registrar = Button(ventana_registro, text="Registrar", border=3, font="Arial 16", command=lambda: registrarmysql(entry_nombre, entry_apellido, entry_usuario, entry_contraseña, mydb, ventana_registro)).place(x=350, y=545)
    boton_gracias = Button(ventana_registro, text="Gracias", border=3, font="Arial 13", command=lambda: gracias(ventana)).place(x=710, y=545)

    ventana.mainloop()

#------------------Fin de la Ventana de Registro---------------
#--------------------------------------------------------------
#------------------Ventana principal de la tienda--------------
#--------------------------------------------------------------
def ventana_tienda(ventana,e1,e2):
    ventana_tienda = tk.Toplevel()
    ventana_tienda.title("TIENDA-LAPTOPSTORE-UNEFA V1.0")
    ventana_tienda.geometry("1024x720")
    ventana_tienda.configure(bg="#6DEEFF")

    logo3 = PhotoImage(file="Logo3.png")
    logo3 = logo3.subsample(2, 2)
    
    entry_id = Entry(ventana_tienda, font="Arial 15")
    entry_id.insert(0, "0")
    #entry_id.place(x=185, y=22)
    entry_producto = Entry(ventana_tienda, font="Arial 15")
    entry_producto.place(x=185, y=32)
    entry_procesador = Entry(ventana_tienda, font="Arial 15")
    entry_procesador.place(x=185, y=102)
    entry_ram = Entry(ventana_tienda, font="Arial 15")
    entry_ram.place(x=185, y=172)
    entry_rom = Entry(ventana_tienda, font="Arial 15")
    entry_rom.place(x=185, y=242)
    entry_gpu = Entry(ventana_tienda,font="Arial 15")
    entry_gpu.place(x=185, y=312)
    entry_pantalla = Entry(ventana_tienda, font="Arial 15")
    entry_pantalla.place(x=185, y=382)
    entry_sistema = Entry(ventana_tienda,font="Arial 15")
    entry_sistema.place(x=185, y=452)
    entry_proveedor = Entry(ventana_tienda, font="Arial 15")
    entry_proveedor.place(x=185, y=522)
    entry_inventario = Entry(ventana_tienda,font="Arial 15")
    entry_inventario.place(x=185, y=592)
    entry_precio = Entry(ventana_tienda, font="Arial 15")
    entry_precio.place(x=660, y=562)

    #text0 = Label(ventana_tienda, text="ID: ", font="Arial 15", border=3).place(x=40, y=20)
    text1 = Label(ventana_tienda, text="Producto: ", font="Arial 15", border=3).place(x=20, y=30)
    text2 = Label(ventana_tienda, text="Procesador: ", font="Arial 15", border=3).place(x=20, y=100)
    text3 = Label(ventana_tienda, text="Memoria-RAM: ", font="Arial 15", border=3).place(x=20, y=170)
    text4 = Label(ventana_tienda, text="Memoria-ROM: ", font="Arial 15", border=3).place(x=20, y=240)
    text5 = Label(ventana_tienda, text="GPU: ", font="Arial 15", border=3).place(x=20, y=310)
    text6 = Label(ventana_tienda, text="Pantalla: ", font="Arial 15", border=3).place(x=20, y=380)
    text7 = Label(ventana_tienda, text="Sistema: ", font="Arial 15", border=3).place(x=20, y=450)
    text8 = Label(ventana_tienda, text="Proveedor: ", font="Arial 15", border=3).place(x=20, y=520)
    text9 = Label(ventana_tienda, text="Inventario: ", font="Arial 15", border=3).place(x=20, y=590)
    text10 = Label(ventana_tienda, text="Precio: ", font="Arial 15", border=3).place(x=540, y=560)

    logo3_label = Label(ventana_tienda, image=logo3)  # Utilizar la variable global logo
    logo3_label.place(x=540, y=15)

    boton_salir = Button(ventana_tienda, text="Salir", border=3, font="Arial 15", command=lambda: cerrar_aplicacion3(ventana_tienda)).place(x=20, y=650)
    boton_comprar = Button(ventana_tienda, text="Comprar", border=5, font="Arial 18", command=lambda: ventana_compra(entry_producto, entry_precio)).place(x=480, y=640)
    boton_limpiar = Button(ventana_tienda, text="Limpiar", border=3, font="Arial 15", command=lambda: limpiar2(entry_producto,entry_procesador,entry_ram,entry_rom,entry_gpu,entry_pantalla, entry_sistema,entry_proveedor,entry_inventario,entry_precio,ventana_tienda)).place(x=920, y=650) 
    boton_next = Button(ventana_tienda, text="Siguiente", border=3, font=14, command=lambda:boton_siguiente(entry_id,entry_producto,entry_procesador,entry_ram,entry_rom,entry_gpu,entry_pantalla, entry_sistema,entry_proveedor,entry_inventario,entry_precio,ventana_tienda,mydb)).place(x=730, y=500)
    boton_back = Button(ventana_tienda, text="Anterior", border=3, font=14, command=lambda:boton_atras(entry_id,entry_producto,entry_procesador,entry_ram,entry_rom,entry_gpu,entry_pantalla, entry_sistema,entry_proveedor,entry_inventario,entry_precio,ventana_tienda,mydb)).place(x=630, y=500)
    
    ventana.mainloop()

#------------------Fin de la Ventana de la Tienda---------------
#---------------------------------------------------------------
#------------------Ventana principal de Administrador-----------
#---------------------------------------------------------------
def ventana_admin(ventana,e1,e2):
    if e1.get() == "Misa_Vnz" and e2.get() =="Santa25":
        ventana_admin = tk.Toplevel()
        ventana_admin.title("ADMINISTRADOR-LAPTOPSTORE-UNEFA V1.0")
        ventana_admin.geometry("1024x720")
        ventana_admin.configure(bg="#6DEEFF")

        logo4 = PhotoImage(file="Logo4.png")
        logo4 = logo4.subsample(2, 2)

        entry_id = Entry(ventana_admin, font="Arial 15")
        entry_id.insert(0, "0")
        #entry_id.place(x=185, y=22)
        entry_producto = Entry(ventana_admin, font="Arial 15")
        entry_producto.place(x=185, y=82)
        entry_procesador = Entry(ventana_admin, font="Arial 15")
        entry_procesador.place(x=185, y=142)
        entry_ram = Entry(ventana_admin, font="Arial 15")
        entry_ram.place(x=185, y=202)
        entry_rom = Entry(ventana_admin, font="Arial 15")
        entry_rom.place(x=185, y=262)
        entry_gpu = Entry(ventana_admin,font="Arial 15")
        entry_gpu.place(x=185, y=322)
        entry_pantalla = Entry(ventana_admin, font="Arial 15")
        entry_pantalla.place(x=185, y=382)
        entry_sistema = Entry(ventana_admin,font="Arial 15")
        entry_sistema.place(x=185, y=442)
        entry_proveedor = Entry(ventana_admin, font="Arial 15")
        entry_proveedor.place(x=185, y=502)
        entry_inventario = Entry(ventana_admin,font="Arial 15")
        entry_inventario.place(x=185, y=562)
        entry_precio = Entry(ventana_admin, font="Arial 15")
        entry_precio.place(x=660, y=562)

        boton_siguiente = Button(ventana_admin, text="Siguiente", border=3, font="Arial 14", command=lambda: boton_siguiente_admin(entry_id, entry_producto, entry_procesador, entry_ram, entry_rom, entry_gpu, entry_pantalla, entry_sistema, entry_proveedor, entry_inventario, entry_precio, ventana_admin, mydb)).place(x=750,y=280)
        boton_anterior = Button(ventana_admin, text="Anterior", border=3, font="Arial 14", command=lambda: boton_atras_admin(entry_id, entry_producto, entry_procesador, entry_ram, entry_rom, entry_gpu, entry_pantalla, entry_sistema, entry_proveedor, entry_inventario, entry_precio, ventana_admin, mydb)).place(x=650,y=280)
        boton_insertar = Button(ventana_admin, text="Insertar producto", border=3, font="Arial 15", command=lambda: ingresar(entry_producto,entry_procesador,entry_ram,entry_rom,entry_gpu,entry_pantalla, entry_sistema,entry_proveedor,entry_inventario,entry_precio,ventana_admin,mydb) ).place(x=660, y=340)
        boton_editar = Button(ventana_admin, text="Editar producto", border=3, font="Arial 15", command=lambda: editar_producto(entry_id,entry_producto,entry_procesador,entry_ram,entry_rom,entry_gpu,entry_pantalla, entry_sistema,entry_proveedor,entry_inventario,entry_precio,ventana_admin,mydb)).place(x=660, y=410)
        boton_eliminar = Button(ventana_admin, text="Eliminar producto", border=3, font="Arial 15", command=lambda: eliminar_producto(entry_id,entry_producto,entry_procesador,entry_ram,entry_rom,entry_gpu,entry_pantalla, entry_sistema,entry_proveedor,entry_inventario,entry_precio,ventana_admin,mydb)).place(x=660, y=480)
        boton_salir = Button(ventana_admin, text="Salir", border=3, font="Arial 15", command=lambda: cerrar_aplicacion4(ventana_admin)).place(x=20, y=650)
        boton_limpiar = Button(ventana_admin, text="Limpiar entradas", border=3, font="Arial 15", command=lambda: limpiar3(entry_producto,entry_procesador,entry_ram,entry_rom,entry_gpu,entry_pantalla, entry_sistema,entry_proveedor,entry_inventario,entry_precio,ventana_admin)).place(x=660, y=650)

        #text0 = Label(ventana_admin, text="ID: ", font="Arial 15", border=3).place(x=40, y=20)
        text1 = Label(ventana_admin, text="Producto: ", font="Arial 15", border=3).place(x=20, y=80)
        text2 = Label(ventana_admin, text="Procesador: ", font="Arial 15", border=3).place(x=20, y=140)
        text3 = Label(ventana_admin, text="Memoria-RAM: ", font="Arial 15", border=3).place(x=20, y=200)
        text4 = Label(ventana_admin, text="Memoria-ROM: ", font="Arial 15", border=3).place(x=20, y=260)
        text5 = Label(ventana_admin, text="GPU: ", font="Arial 15", border=3).place(x=20, y=320)
        text6 = Label(ventana_admin, text="Pantalla: ", font="Arial 15", border=3).place(x=20, y=380)
        text7 = Label(ventana_admin, text="Sistema: ", font="Arial 15", border=3).place(x=20, y=440)
        text8 = Label(ventana_admin, text="Proveedor: ", font="Arial 15", border=3).place(x=20, y=500)
        text9 = Label(ventana_admin, text="Inventario: ", font="Arial 15", border=3).place(x=20, y=560)
        text10 = Label(ventana_admin, text="Precio: ", font="Arial 15", border=3).place(x=540, y=560)

        logo4_label = Label(ventana_admin, image=logo4)  # Utilizar la variable global logo
        logo4_label.place(x=580, y=15)

        comentario = Label(ventana_admin, text="Recuerda que para ingresar un\nnuevo articulo solo debes pulsar\nlimpiar entradas, rellenarlas\ncon los nuevos datos y insertar producto :)", background="#D9DE9C", border=5, font="Arial 15")
        comentario.place(x=122, y=605)

        ventana.mainloop()
    else:
        messagebox.showinfo("Error", "No eres un usuario administrador")

#------------------Fin de la Ventana de Administrador----------------------
#--------------------------------------------------------------------------













