# -*- coding: utf-8 -*-

# Creación de un Chat Cliente Servidor Usando Sockets en Python
import socket
import funciones_servidor


def main():
    servidor = socket.socket()
    servidor.bind(("", 5000))
    servidor.listen(1)
    socket_cliente, datos_conexion = servidor.accept()

    usuario = False
    contrasena = False
    menu = False
    menu_1 = False
    d =False
    con=1
    menu_2=False
    m=False
    w=int(5)
    i=0
    l=True


    while l==True:


        #mensaje_servidor = raw_input("Ingrese Respuesta al Cliente >> ")
        contador = 0


        #validar usuario
        while(usuario != True):
            if(contador > 0):
                mensaje_servidor = funciones_servidor.getusuario_error()
                socket_cliente.send(mensaje_servidor)

            mensaje_servidor = funciones_servidor.getusuario()
            socket_cliente.send(mensaje_servidor)
            mensaje_cliente = socket_cliente.recv(1024)

            if(funciones_servidor.validar_usuario(mensaje_cliente)):
                usuario = True



            contador = contador + 1
        a = mensaje_cliente
        #validar contraseña
        contador = 0
        while (contrasena != True):
            if (contador > 0):
                mensaje_servidor = funciones_servidor.getcontrasena_error()
                socket_cliente.send(mensaje_servidor)

            mensaje_servidor = funciones_servidor.getcontrasena()
            socket_cliente.send(mensaje_servidor)
            mensaje_cliente = socket_cliente.recv(1024)

            if (funciones_servidor.validar_contrasena(mensaje_cliente)):
                contrasena = True
                funciones_servidor.creartxt()
                b = mensaje_cliente
                c = datos_conexion[0]
                funciones_servidor.grabartxt(a, b, c)
                #socket_cliente.send(mensaje_servidor)
            contador = contador + 1

        contador = 0
        if(menu != True and contrasena == True):
            while(True):
                if (contador > 0):
                    mensaje_servidor = funciones_servidor.getmenu_error()
                    socket_cliente.send(mensaje_servidor)

                mensaje_servidor = funciones_servidor.menu()
                socket_cliente.send(mensaje_servidor)
                mensaje_cliente = int(socket_cliente.recv(1024))
                if(mensaje_cliente > 0 and mensaje_cliente <6):
                    menu = True
                    break

                contador += 1


        operacion = mensaje_cliente
        if operacion == 5:
            con=5

        while (menu == True):
            if (con < 5):
                #print con
                mensaje_servidor = funciones_servidor.getnum_1()
                socket_cliente.send(mensaje_servidor)
                num_1 = int(socket_cliente.recv(1024))
                mensaje_servidor = funciones_servidor.getnum_2()
                socket_cliente.send(mensaje_servidor)
                num_2 = int(socket_cliente.recv(1024))

            if(operacion == 1):
                mensaje_servidor = funciones_servidor.suma(num_1, num_2)
                socket_cliente.send(mensaje_servidor)
                menu = False
                con += 1

            if (operacion == 2):

                mensaje_servidor = funciones_servidor.resta(num_1, num_2)
                socket_cliente.send(mensaje_servidor)
                menu = False
                con += 1
            if (operacion == 3):

                mensaje_servidor = funciones_servidor.multiplicar(num_1, num_2)
                socket_cliente.send(mensaje_servidor)
                menu = False
                con += 1
            if (operacion == 4):
                mensaje_servidor = funciones_servidor.dividir(num_1, num_2)
                socket_cliente.send(mensaje_servidor)
                menu = False
                con += 1
            if (operacion == 5):
                menu = False
                menu_1 = True

                break
            break

        while menu_1 == True:
            if i == 0:
                while (True):

                    if (contador > 0):
                        mensaje_servidor = funciones_servidor.getmenu1_error()
                        socket_cliente.send(mensaje_servidor)

                    mensaje_servidor = funciones_servidor.menu1()
                    socket_cliente.send(mensaje_servidor)
                    mensaje_cliente = int(socket_cliente.recv(1024))
                    if (mensaje_cliente > 0 and mensaje_cliente < 6):
                        menu_1 = False
                        d = True
                        break
                    contador += 1
            break
        operacion_1 = mensaje_cliente
        while (d == True):

            if (operacion_1 == 1):
                mensaje_servidor = funciones_servidor.listar()
                socket_cliente.send(mensaje_servidor)
                d = False
                menu_1=True
                menu=True
                mensaje_cliente=5

            if (operacion_1 == 2):
                mensaje_servidor = funciones_servidor.archivo()
                socket_cliente.send(mensaje_servidor)
                archi =(socket_cliente.recv(1024))
                mensaje_servidor = funciones_servidor.crear_txt(archi)
                socket_cliente.send(mensaje_servidor)
                d = False
                menu_1=True
                menu=True
                mensaje_cliente=5

            if (operacion_1 == 3):
                mensaje_servidor = funciones_servidor.archivo()
                socket_cliente.send(mensaje_servidor)
                archi = (socket_cliente.recv(1024))
                mensaje_servidor = funciones_servidor.leer_txt(archi)
                socket_cliente.send(mensaje_servidor)
                texto = (socket_cliente.recv(1024))
                mensaje_servidor = funciones_servidor.editar_txt(archi,texto)
                socket_cliente.send(mensaje_servidor)
                d = False
                menu_1 = True
                menu = True
                mensaje_cliente = 5

            if (operacion_1 == 4):
                mensaje_servidor = funciones_servidor.archivo()
                socket_cliente.send(mensaje_servidor)
                archi = (socket_cliente.recv(1024))
                mensaje_servidor = funciones_servidor.eliminar_txt(archi)
                socket_cliente.send(mensaje_servidor)
                d = False
                menu_1 = True
                menu = True
                mensaje_cliente = 5

            if (operacion_1 == 5):
                d = False
                menu_1 = False
                menu = True
                mensaje_cliente = 5
                menu_2=True
                break
            break

        while menu_2 == True:
            while (True):
                if (contador > 0):
                    mensaje_servidor = funciones_servidor.getmenu2_error()
                    socket_cliente.send(mensaje_servidor)

                mensaje_servidor = funciones_servidor.menu2()
                socket_cliente.send(mensaje_servidor)
                mensaje_cliente = int(socket_cliente.recv(1024))
                if (mensaje_cliente > 0 and mensaje_cliente < 5):
                    menu_2 = False
                    m = True
                    break

                contador += 1
        operacion_2 = mensaje_cliente
        while (m == True):

            if (operacion_2 == 1):
                mensaje_servidor = funciones_servidor.mostrar(w)
                socket_cliente.send(mensaje_servidor)
                mensaje_servidor = funciones_servidor.id_producto()
                socket_cliente.send(mensaje_servidor)
                id = int(socket_cliente.recv(1024))
                mensaje_servidor = funciones_servidor.cantidad_producto()
                socket_cliente.send(mensaje_servidor)
                producto = int(socket_cliente.recv(1024))
                mensaje_servidor = funciones_servidor.inventario(id, w, producto)
                socket_cliente.send(mensaje_servidor)
                d = False
                menu_1=False
                menu=True
                menu_2=True
                m=False
                mensaje_cliente=5
                i=1
            if (operacion_2 == 2):
                mensaje_servidor = funciones_servidor.ventas()
                socket_cliente.send(mensaje_servidor)
                d = False
                menu_1 = False
                menu = True
                menu_2 = True
                m = False
                mensaje_cliente = 5
                i = 1
            if (operacion_2 == 3):
                mensaje_servidor = funciones_servidor.inve_real()
                socket_cliente.send(mensaje_servidor)
                d = False
                menu_1 = False
                menu = True
                menu_2 = True
                m = False
                mensaje_cliente = 5
                i = 1
            if (operacion_2 == 4):
                d = False
                menu_1 = False
                menu = True
                menu_2 = False
                m = False
                mensaje_cliente = 6
                i = 1
                l = False
                break
            break

    socket_cliente.close()
    servidor.close()

if __name__ == '__main__':
    main()