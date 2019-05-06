#!/usr/bin/python
import os

os.write(1,"ingrese el nombre del archivo origen:")
archivo_origen = os.read(0,10000).strip()
#si con read alcanza el final del archivo, devuelve una cadena vacia(hay un \n)
#archivo_origen = raw_input()

os.write(1,"ingrese el nombre del archivo destino:")
archivo_destino = os.read(0,10000).strip()

fd = os.open(archivo_origen,os.O_RDWR)
#os.open() es otro file descriptor
var_origen= os.read(fd,10000)
os.close(fd)

#with os.open(fd,os.O_RDONLY) as open_file:
#    var_origen = open_file.os.read(fd)

fdd = os.open(archivo_destino,os.O_RDWR|os.O_CREAT)

final = os.write(fdd,var_origen)
os.close(fdd)

