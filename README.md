# Tienda de laptops a traves del lenguaje de programacion Python

## Descripcion:

Este codigo se basa en una tienda de laptops virtual hecha con el lenguaje de programacion Python, que consta con 5 interfaces una interfaz de inicio de sesion, otra para administrador, una para nuevos registros, una principal de la tienda y una pequeña ventana de compra, esta tienda fue hecha con una base de datos creada y manipulada desde 0 en mysql con dos tablas, una para usuario y otra para productos, dicho codigo es capaz de realizar tareas como: 

* Iniciar sesion: Es capaz de verificar si el usuario y contraseña ingresada en la ventana de inicio coincide con uno ya existente en la base de datos.
* Registrar nuevo usuario: En el caso de no estar registrado, consta de una interfaz para registrar nuevos usuarios y que estos sean ingresados en la base de datos.
* Comandos Admin: Realiza comandos de administrador solo si el usuario y contraseña son las del administrador del codigo, y permite editar, eliminar, buscar y guardar datos en la base de datos de productos.
* Interfaz interactiva con imagenes: Tiene disponibles 10 imagenes de diferentes modelos de laptops con sus precios reales, y dos botones interactivos para pasar al siguiente producto o al anterior.(En el caso de querer agregarse mas imagenes hay un apartado comentado en el codigo para eso)
* Comentarios informativos: En las diferentes interfaces del codigo cuenta con pequeños comentarios informativos para hacer mas entendible el funcionamiento de la tienda.

Esta aplicacion fue realizada al 100% con el lenguaje de programacion Python utilizando como interfaz grafica la libreria tkinter, y como opcion para guardar y manejar base de datos se ha usado Mysql en el panel de XAMPP.

El archivo es originalmente elaborado por el estudiante del 6to Semestre de Telecom @MisaVnz(Misael Carmona), estudiante de la UNEFA.

Este codigo fue realizado como una asignacion del 4to Corte de la materia de Computacion Avanzada dada por el Ingeniero Manuel Jimenez.

## Recursos:
* [Documentación oficial de Tkinter](https://docs.python.org/es/3/library/tk.html)