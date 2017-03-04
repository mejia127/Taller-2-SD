# -*- coding: utf-8 -*-
import json
import time
import os

a=5

def menu():
    lista = ["Bienvenido a la Calculadora", "1. Suma", "2. Resta", "3. Multiplicar", "4. División", "5. Salir", "Digite el número de la opción >>"]
    cadena = json.dumps(lista)
    return cadena

def menu1():
    lista = ["Bienvenido a Procesador de Palabras", "1. Listar Archvios", "2. Crear Archivo ", "3. Modificar Archivo",
             "4. Eliminar Archivo", "5. Salir", "Digite el número de la opción >>"]
    cadena = json.dumps(lista)
    return cadena

def menu2():
    lista = ["Bienvenido a Supermercado", "1. Comprar Productos", "2. Ventas del dia ", "3. Inventarios",
             "4. Salir", "Digite el número de la opción >>"]
    cadena = json.dumps(lista)
    return cadena

def getusuario():
    lista = ["Ingrese su Usuario >>"]
    cadena = json.dumps(lista)
    return cadena

def getcontrasena():
    lista = ["Ingrese su Contraseña >>"]
    cadena = json.dumps(lista)
    return cadena

def validar_usuario(cadena):
    if(cadena == "Fernando"):
        return True
    else:
        return False

def validar_contrasena(cadena):
    if(cadena == "Fernando"):
        return True
    else:
        return False

def getusuario_error():
    lista = ["Usuario incorrecto", "Presione enter para intentarlo de nuevo >>"]
    cadena = json.dumps(lista)
    return cadena

def getcontrasena_error():
    lista = ["Contraseña incorrecta", "Presione enter para intentarlo de nuevo >>"]
    cadena = json.dumps(lista)
    return cadena

def getmenu_error():
    lista = ["Opcion Invalida", "\n", "Presione enter para mostrar el menu de nuevo"]
    cadena = json.dumps(lista)
    return cadena

def getmenu1_error():
    lista = ["Opcion Invalida", "\n", "Presione enter para mostrar el menu de nuevo"]
    cadena = json.dumps(lista)
    return cadena

def getnum_1():
    lista = ["Ingese el numero 1 y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def getnum_2():
    lista = ["Ingese el numero 2 y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def suma(num1, num2):
    suma = str(num1 + num2)
    lista = ["Resultado de la operacion = " + suma, "Presione enter para volver al menu"]
    cadena = json.dumps(lista)
    return cadena

def resta(num1, num2):
    resta = str(num1 - num2)
    lista = ["Resultado de la operacion = " + resta, "Presione enter para volver al menu"]
    cadena = json.dumps(lista)
    return cadena

def multiplicar(num1, num2):
    multiplicar = str(num1 * num2)
    lista = ["Resultado de la operacion = " + multiplicar, "Presione enter para volver al menu"]
    cadena = json.dumps(lista)
    return cadena

def dividir(num1, num2):
    dividir = str(num1 / num2)
    lista = ["Resultado de la operacion = " + dividir, "Presione enter para volver al menu"]
    cadena = json.dumps(lista)
    return cadena

def creartxt():
    archivo=open('datos.txt','w')
    archivo.close()

def grabartxt(d,e,f):
    creartxt()
    archivo=open('datos.txt','a')
    fecha=time.strftime("%x")
    hora=time.strftime("%X")
    archivo.write("Usuario " + d + '\n')
    archivo.write("Contraseña " + e + '\n')
    archivo.write("Ip " + f +'\n')
    archivo.write("Fecha " + fecha + '\n')
    archivo.write("Hora " + hora + '\n')
    archivo.close()

def listar():
    path = "C:\Users\octavio murillo\PycharmProjects\cliente_servidor"
    mitexto = os.listdir(path)
    archivos = []
    for ruta in mitexto:
        (nombreFichero, extension) = os.path.splitext(ruta)
        if(extension == ".txt"):
            archivos.append(nombreFichero+extension)
    archivos.append("Presione Enter para Continuar")
    cadena = json.dumps(archivos)

    return cadena

def archivo():
    lista = ["Ingese el nombre del archivo y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def crear_txt(nombreFichero):
    archivo=str(nombreFichero+".txt")
    lista = ["Archivo = " + archivo, "Creado Exitosamente , Presione enter para volver al menu "]
    cadena = json.dumps(lista)
    archivo = open(archivo, 'w')
    archivo.close()
    return cadena


def leer_txt(nombreFichero):
    archivo = str(nombreFichero + ".txt")
    archi = open(archivo, 'r')
    lineas=archi.readlines()
    texto=str(lineas)
    lista = ["Contenido del Archivo "+ archivo + '\n' + texto + '\n'+ "Ingrese Texto Adicional al Archivo "]
    cadena = json.dumps(lista)
    archi.close()
    return cadena

def editar_txt(nombreFichero,texto):
    archi=str(nombreFichero+".txt")
    archivo = open(archi, 'a')
    archivo.write('\n' + texto)
    lista = ["Archivo = " + archi, "Modificado Exitosamente , Presione enter para volver al menu "]
    cadena = json.dumps(lista)
    archivo.close()
    return cadena


def eliminar_txt(nombreFichero):
    archi = str(nombreFichero + ".txt")
    os.remove(archi)
    lista = ["Archivo = " + archi, "Eliminado Exitosamente , Presione enter para volver al menu "]
    cadena = json.dumps(lista)
    return cadena

def mostrar(w):


    h=id(1)
    p = nombre_producto()
    e = w
    r = precio()
    lista=[[h, p , e, r, "presione enter para continuar"]]
    cadena = json.dumps(lista)
    return cadena

def id_producto():
    lista = ["Ingrese el id del producto y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def cantidad_producto():
    lista = ["Ingrese  cantidad a comprar y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def id(n):

    lista = [1]
    contador = 0
    for letra in lista:
        if letra == n:
            contador = contador + 1

    return contador

def nombre_producto():

    lista=["Banano"]
    cadena = json.dumps(lista)
    return cadena

def cantidad(m,n):
    d = m-n
    return d

def precio():
    valor=1000
    return valor

def inventario(n, m, y):

    q=int(id(n))
    w=str(nombre_producto())
    e=cantidad(m, y)
    r=precio()
    #venta=y

    archivo = open("ventas.txt",'a')
    fecha = time.strftime("%x")
    hora = time.strftime("%X")
    archivo.write("Id Producto "+ str(q)+ '\n')
    archivo.write("Nombre del Produto "+ w + '\n')
    archivo.write("Unidades vendidas " + str(y) + '\n')
    archivo.write("Fecha Venta " + fecha + '\n')
    archivo.write("Hora Venta " + hora + '\n')
    archivo.close()

    archivo = open("inventario.txt", 'a')
    archivo.write("Id Producto " + str(q) + '\n')
    archivo.write("Nombre del Produto " + w + '\n')
    archivo.write("Unidades Actuales Bodega " + str(e) + '\n')
    archivo.close()


    lista = ["Comprar realizada con exito, presione enter para continuar "]
    cadena = json.dumps(lista)
    return cadena

def ventas():
    archi = open("ventas.txt", 'r')
    lineas=archi.readlines()
    texto=str(lineas)
    lista = ["Contenido del Archivo ventas.txt " + '\n' + texto + '\n' + "presione enter para volver al menu "]
    cadena = json.dumps(lista)
    archi.close()
    return cadena

def inve_real():
    archi = open("inventario.txt", 'r+')
    lineas=archi.readlines()
    texto=str(lineas)
    lista = ["Contenido del Archivo inventario " + '\n' + texto + '\n' + "Presione enter para volver al menu "]
    cadena = json.dumps(lista)
    archi.close()
    return cadena




























