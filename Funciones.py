from tkinter import messagebox 
from mysql.connector import *
from PIL import Image, ImageTk
import tkinter as tk 

def limpiar(entry1, entry2):
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    messagebox.showinfo("Limpiado", "Se ha limpiado correctamente")

def cerrar_aplicacion1(ventana_registro):
    if messagebox.askokcancel("Salir", "¿Seguro que quieres salir?"):
        ventana_registro.destroy()

def cerrar_aplicacion2(ventana):
    if messagebox.askokcancel("Salir", "¿Seguro que quieres salir?"):
        ventana.destroy()

def cerrar_aplicacion3(ventana_tienda):
    if messagebox.askokcancel("Salir", "¿Seguro que quieres salir?"):
        ventana_tienda.destroy()

def cerrar_aplicacion4(ventana_admin):
    if messagebox.askokcancel("Salir", "¿Seguro que quieres salir?"):
        ventana_admin.destroy()

def registrarmysql(entry1, entry2, entry3, entry4, mydb, ventana_registro):
    nombre = entry1.get()
    apellido = entry2.get()
    usuario = entry3.get()
    contraseña = entry4.get()

    if nombre and apellido and usuario and contraseña:  # Verifica que ningún campo esté vacío
        mycursor = mydb.cursor()
        mensaje = f"Nombre: {nombre}\nApellido: {apellido}\nUsuario: {usuario}\nContraseña: {contraseña}"
        ingreso = f"Usuario: {usuario}\nContraseña: {contraseña}"
        sql = "INSERT INTO usuarios_tienda(nombre, apellido, usuario, contraseña) VALUES (%s, %s, %s, %s)"
        val = (nombre, apellido, usuario, contraseña)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Informacion enviada", mensaje)
        messagebox.showinfo("Datos para ingresar:", ingreso)
        mydb.commit()
        ventana_registro.destroy()
    else:
        messagebox.showerror("Error", "Todos los campos son requeridos")

def buscarsql(entry1,entry2,entry3,entry4,entry5,entry6,entry7,entry8,entry9,entry10,entry11,ventana_tienda,mydb):
    mycursor =mydb.cursor()
    id = entry1.get()
    sql = f"select * from `productos_tienda` where Id = '{id}'"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for i in result:
        producto = i[1]
        procesador = i[2]
        ram = i[3]
        rom = i[4]
        gpu = i[5]
        pantalla = i[6]
        sistema = i[7]
        proveedor = i[9]
        inventario = i[10]
        precio = i[8]

    entry2.insert(0, producto)
    entry2.config(width=len(producto))
    entry3.insert(0, procesador)
    entry3.config(width=len(procesador))
    entry4.insert(0, ram)
    entry4.config(width=len(ram))
    entry5.insert(0, rom)
    entry5.config(width=len(rom))
    entry6.insert(0, gpu)
    entry6.config(width=len(gpu))
    entry7.insert(0, pantalla)
    entry7.config(width=len(pantalla))
    entry8.insert(0, sistema)
    entry8.config(width=len(sistema))
    entry9.insert(0, proveedor)
    entry9.config(width=len(proveedor))
    entry10.insert(0, inventario)
    entry11.insert(0, precio)
   
def gracias(ventana):
    messagebox.showinfo("Mensaje de agradecimiento", "Gracias por utilizar LAPTOPSTORE-UNEFA")

def limpiar2(entry2,entry3,entry4,entry5,entry6,entry7,entry8,entry9,entry10,entry11,ventana_tienda):
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    entry4.delete(0, 'end')
    entry5.delete(0, 'end')
    entry6.delete(0, 'end')
    entry7.delete(0, 'end')
    entry8.delete(0, 'end')
    entry9.delete(0, 'end')
    entry10.delete(0, 'end')
    entry11.delete(0, 'end')
    messagebox.showinfo("Limpiado", "Se ha limpiado correctamente")

def limpiar3(entry2,entry3,entry4,entry5,entry6,entry7,entry8,entry9,entry10,entry11,ventana_admin):
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    entry4.delete(0, 'end')
    entry5.delete(0, 'end')
    entry6.delete(0, 'end')
    entry7.delete(0, 'end')
    entry8.delete(0, 'end')
    entry9.delete(0, 'end')
    entry10.delete(0, 'end')
    entry11.delete(0, 'end')

label_imagen = None

def mostrar_imagen(ventana_tienda, entry_id):
    global label_imagen

    valor = int(entry_id.get())  # Obtener el valor del entry_id como entero
    if valor >= 0 and valor <= 10:
        imagen_path = f"{valor}.png"
    else:
        imagen_path = '0.png'

    imagen = Image.open(imagen_path)
    imagen = imagen.resize((350, 350), Image.LANCZOS)  # Utiliza LANCZOS en lugar de ANTIALIAS

    imagen_tk = ImageTk.PhotoImage(imagen)  # Convertir la imagen a un formato compatible con tkinter

    # Verificar si el label_imagen ya existe y está en la ventana
    if label_imagen and label_imagen.winfo_exists():
        label_imagen.config(image=imagen_tk)
        label_imagen.image = imagen_tk
    else:
        # Crear un nuevo label si no existe uno o ha sido eliminado
        label_imagen = tk.Label(ventana_tienda, image=imagen_tk)
        label_imagen.image = imagen_tk
        label_imagen.place(x=560, y=130)  # Ajustar la posición de la imagen en la ventana

def ingresar(entry2,entry3,entry4,entry5,entry6,entry7,entry8,entry9,entry10,entry11,ventana_admin,mydb):
    mycursor =mydb.cursor()
    producto = entry2.get()
    procesador = entry3.get()
    ram = entry4.get()
    rom = entry5.get()
    gpu = entry6.get()
    pantalla = entry7.get()
    sistema = entry8.get()
    proveedor = entry11.get()
    inventario = entry9.get()
    precio = entry10.get()
    mensaje =(f"Producto: {producto}\nProcesador: {procesador}\nRAM: {ram}\nROM: {rom}\nGPU: {gpu}\nPantalla: {pantalla}\nSistema: {sistema}\nPrecio: {proveedor}\nProveedor: {inventario}\nInventario: {precio}")
    sql="INSERT INTO `productos_tienda`(`Nombre_Producto`, `Procesador`, `Memoria_RAM`, `Memoria_ROM`, `GPU`, `Pantalla`, `Sistema`, `Precio`, `Proveedor`, `Inventario`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val =(producto,procesador,ram,rom,gpu,pantalla,sistema,proveedor,inventario,precio)
    mycursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo("Informacion enviada", mensaje)

def buscarsql_admin(entry1,entry2,entry3,entry4,entry5,entry6,entry7,entry8,entry9,entry10,entry11,ventana_admin,mydb):
    mycursor =mydb.cursor()
    id = entry1.get()
    sql = f"select * from `productos_tienda` where Id = '{id}'"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for i in result:
        producto = i[1]
        procesador = i[2]
        ram = i[3]
        rom = i[4]
        gpu = i[5]
        pantalla = i[6]
        sistema = i[7]
        proveedor = i[9]
        inventario = i[10]
        precio = i[8]

    entry2.insert(0, producto)
    entry2.config(width=len(producto))
    entry3.insert(0, procesador)
    entry3.config(width=len(procesador))
    entry4.insert(0, ram)
    entry4.config(width=len(ram))
    entry5.insert(0, rom)
    entry5.config(width=len(rom))
    entry6.insert(0, gpu)
    entry6.config(width=len(gpu))
    entry7.insert(0, pantalla)
    entry7.config(width=len(pantalla))
    entry8.insert(0, sistema)
    entry8.config(width=len(sistema))
    entry9.insert(0, proveedor)
    entry9.config(width=len(proveedor))
    entry10.insert(0, inventario)
    entry11.insert(0, precio)

def editar_producto(entry1,entry2,entry3,entry4,entry5,entry6,entry7,entry8,entry9,entry10,entry11,ventana_admin,mydb):
    mycursor =mydb.cursor()
    id = entry1.get()
    producto = entry2.get()
    procesador = entry3.get()
    ram = entry4.get()
    rom = entry5.get()
    gpu = entry6.get()
    pantalla = entry7.get()
    sistema = entry8.get()
    proveedor = entry9.get()
    inventario = entry10.get()
    precio = entry11.get()

    sql = "update `productos_tienda` set Nombre_producto=%s, Procesador=%s, Memoria_RAM=%s, Memoria_ROM=%s, GPU=%s, Pantalla=%s, Sistema=%s, Proveedor=%s, Inventario=%s, Precio=%s where Id = %s"
    valores =(producto,procesador, ram, rom, gpu, pantalla, sistema, proveedor, inventario, precio, id)
    mycursor.execute(sql, valores)
    mydb.commit()
    messagebox.askokcancel("Mensaje", "Registro actualizado")
    limpiar3(entry1,entry2,entry3,entry4,entry5,entry6,entry7,entry8,entry9,entry10,entry11,ventana_admin)

def eliminar_producto(entry1,entry2,entry3,entry4,entry5,entry6,entry7,entry8,entry9,entry10,entry11,ventana_admin,mydb):
    buscarsql_admin(entry1,entry2,entry3,entry4,entry5,entry6,entry7,entry8,entry9,entry10,entry11,ventana_admin,mydb)
    mycursor =mydb.cursor()
    sql = f"DELETE FROM `productos_tienda` WHERE Id ={entry1.get()}"
    mycursor.execute(sql)
    mydb.commit()
    messagebox.askokcancel("Mensaje", "Seguro que deseas eliminar este registro?")
    messagebox.showinfo("Mensaje", "Registro eliminado correctamente")
    limpiar3(entry1,entry2,entry3,entry4,entry5,entry6,entry7,entry8,entry9,entry10,entry11,ventana_admin)
   
def boton_siguiente(entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11, ventana_tienda, mydb):
    mensaje = "Lo lamentamos :("
    id = int(entry1.get())
    # Verifica que id sea menor o igual a 10 antes de incrementarlo
    if id < 10:
        id += 1
        entry1.delete(0, 'end')  # Borra el contenido actual de entry1
        entry1.insert(0, str(id))  # Inserta el nuevo valor de id en entry1

        # Borra el contenido de las entradas anteriores
        entry2.delete(0, 'end')
        entry3.delete(0, 'end')
        entry4.delete(0, 'end')
        entry5.delete(0, 'end')
        entry6.delete(0, 'end')
        entry7.delete(0, 'end')
        entry8.delete(0, 'end')
        entry9.delete(0, 'end')
        entry10.delete(0, 'end')
        entry11.delete(0, 'end')

        buscarsql_admin(entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11, ventana_tienda, mydb)
        mostrar_imagen(ventana_tienda, entry1)
    else:
        messagebox.showerror(mensaje,"No tenemos mas productos actualmente\nprueba echandole otro vistazo a los disponibles")

def boton_atras(entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11, ventana_tienda, mydb):
    mensaje = "Lo lamentamos :("
    id = int(entry1.get())
    # Verifica que id sea menor o igual a 0 antes de reducirlo
    if id == 0:
        print("No tenemos articulos con Id de -1 Ingeniero :)")   
    elif id == 1 : 
        print("No tenemos articulos con Id de 0 Ingeniero :)")   
    elif id < 100:
            id -= 1
            entry1.delete(0, 'end')  # Borra el contenido actual de entry1
            entry1.insert(0, str(id))  # Inserta el nuevo valor de id en entry1

            # Borra el contenido de las entradas anteriores
            entry2.delete(0, 'end')
            entry3.delete(0, 'end')
            entry4.delete(0, 'end')
            entry5.delete(0, 'end')
            entry6.delete(0, 'end')
            entry7.delete(0, 'end')
            entry8.delete(0, 'end')
            entry9.delete(0, 'end')
            entry10.delete(0, 'end')
            entry11.delete(0, 'end')

            buscarsql_admin(entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11, ventana_tienda, mydb)
            mostrar_imagen(ventana_tienda, entry1)

def boton_siguiente_admin(entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11, ventana_tienda, mydb):
    id = int(entry1.get())
    mensaje = "¿Nuevo producto?"
    # Verifica que id sea menor o igual a 10 antes de incrementarlo
    if id < 100:
        id += 1
        entry1.delete(0, 'end')  # Borra el contenido actual de entry1
        entry1.insert(0, str(id))  # Inserta el nuevo valor de id en entry1

        # Borra el contenido de las entradas anteriores
        entry2.delete(0, 'end')
        entry3.delete(0, 'end')
        entry4.delete(0, 'end')
        entry5.delete(0, 'end')
        entry6.delete(0, 'end')
        entry7.delete(0, 'end')
        entry8.delete(0, 'end')
        entry9.delete(0, 'end')
        entry10.delete(0, 'end')
        entry11.delete(0, 'end')

        buscarsql_admin(entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11, ventana_tienda, mydb)

def boton_atras_admin(entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11, ventana_tienda, mydb):
    id = int(entry1.get())
    # Verifica que id sea menor o igual a 0 antes de reducirlo
    if id == 0:
        print("No tenemos articulos con Id de -1 Ingeniero :)")   
    elif id == 1 : 
        print("No tenemos articulos con Id de 0 Ingeniero :)")   
    elif id < 100:
            id -= 1
            entry1.delete(0, 'end')  # Borra el contenido actual de entry1
            entry1.insert(0, str(id))  # Inserta el nuevo valor de id en entry1

            # Borra el contenido de las entradas anteriores
            entry2.delete(0, 'end')
            entry3.delete(0, 'end')
            entry4.delete(0, 'end')
            entry5.delete(0, 'end')
            entry6.delete(0, 'end')
            entry7.delete(0, 'end')
            entry8.delete(0, 'end')
            entry9.delete(0, 'end')
            entry10.delete(0, 'end')
            entry11.delete(0, 'end')

            buscarsql_admin(entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11, ventana_tienda, mydb)
        




        
        




   