# -*- coding: utf-8 -*-

# Creación de un Chat Cliente Servidor Usando Sockets en Python
import socket
import funciones_cliente

cliente = socket.socket()
cliente.connect(("localhost", 5000))

while True:

    mensaje_servidor = cliente.recv(1024)
    funciones_cliente.imprimir(mensaje_servidor)

    mensaje_cliente = raw_input("Ingrese Mensaje al Servidor >> ")
    cliente.send(mensaje_cliente)

    if mensaje_cliente == "salir":

        break
    


print "Hasta Pronto"
cliente.close()