#!/usr/bin/python3
import argparse
import requests
import urllib.request, urllib.parse
from PIL import Image
from bs4 import BeautifulSoup
import urllib.error
from urllib.request import urlopen
import sys
import getopt
import array
import os

def color_rojo(ruta):
    fd = os.open(ruta+".ppm", os.O_RDONLY)

    cabecera = os.read(fd,16)
    cabecera_split = str(cabecera).split("\\n")

    p_image = cabecera_split[0][2] + cabecera_split[0][3]
    width = int(cabecera_split[1].split()[0])
    height = int(cabecera_split[1].split()[1])
    max_value = int(cabecera_split[2])

    ppm_header = p_image + ' ' + str(width) + ' ' + str(height) + ' ' + str(max_value) + "\n"
    imorig = os.read(fd, width*height*3)

    image = array.array('B', [0, 0, 0] * width * height)

    for x in range(0, height):
        for y in range(0, width):
            index = 3 * (x * width + y)
            image[index + 0] = imorig[index + 0]

    ## Save the PPM image as a binary file
    f =  open(ruta+'rojo.ppm', 'wb')
    f.write(bytearray(ppm_header, 'ascii'))
    image.tofile(f)
def color_azul(ruta):
    fd = os.open(ruta+".ppm", os.O_RDONLY)

    cabecera = os.read(fd,15)
    #con el azul tengo que leer 15 bytes(solucionar)
    #salta index error
    cabecera_split = str(cabecera).split("\\n")

    p_image = cabecera_split[0][2] + cabecera_split[0][3]
    width = int(cabecera_split[1].split()[0])
    height = int(cabecera_split[1].split()[1])
    max_value = int(cabecera_split[2])

    ppm_header = p_image + ' ' + str(width) + ' ' + str(height) + ' ' + str(max_value) + "\n"
    imorig = os.read(fd, width*height*3)

    image = array.array('B', [0, 0, 0] * width * height)

    for x in range(0, height):
        for y in range(0, width):
            index = 3 * (x * width + y)
            image[index + 2] = imorig[index + 2]

    ## Save the PPM image as a binary file
    f =  open(ruta+'azul.ppm', 'wb')
    f.write(bytearray(ppm_header, 'ascii'))
    image.tofile(f)
def color_verde(ruta):
    fd = os.open(ruta+".ppm", os.O_RDONLY)

    cabecera = os.read(fd,16)
    cabecera_split = str(cabecera).split("\\n")

    p_image = cabecera_split[0][2] + cabecera_split[0][3]
    width = int(cabecera_split[1].split()[0])
    height = int(cabecera_split[1].split()[1])
    max_value = int(cabecera_split[2])

    ppm_header = p_image + ' ' + str(width) + ' ' + str(height) + ' ' + str(max_value) + "\n"
    imorig = os.read(fd, width*height*3)

    image = array.array('B', [0, 0, 0] * width * height)

    for x in range(0, height):
        for y in range(0, width):
            index = 3 * (x * width + y)
            image[index + 1] = imorig[index + 1]

    ## Save the PPM image as a binary file
    f =  open(ruta+'verde.ppm', 'wb')
    f.write(bytearray(ppm_header, 'ascii'))
    image.tofile(f)

opciones, argumentos = getopt.getopt(sys.argv[1:], "u:h")

#Bucle para recorrer el arreglo y localizar el url de la página.
URLs_images = ""

for o in opciones:
    if o[0] == "-h":
        #Llamada a función de ayuda para guiar al usuario.
        OpcAyuda()
    if o[0] == "-u":
        #La pos. 1 del arreglo constituye la URL de la página.
        URLs_images = o[1]
        print(o[1])

# Auxiliar variables
urls = URLs_images

hosts = urls.split(",")

contents = {}
imageSources = []

# Get hosts HTML (using Beautiful Soup)
for host in hosts:
    contents[host] = BeautifulSoup(requests.get(host).text, "html.parser")
    #beautifulsoup extrae datos desde html

# Extract images
for host in hosts:
    images = contents[host].findAll("img")
    for img in images:
        imgUrl = img.get("src")
        if imgUrl[0] == "/":
            #esto es para los que le falta el hostname
            imgUrl = host + imgUrl
        imageSources.append(imgUrl)

for i in range(len(imageSources)):
    src = imageSources[i]
    #print(imageSources[i])
    parsedUrl = urllib.parse.urlparse(src)
    #esto es para parsear las urls de la lista, o sea, devuelve los elementos dela estructura de la url,scheme,netloc,path...
    newUrl = parsedUrl.scheme + "://" + parsedUrl.netloc + parsedUrl.path
    imageSources[i] = newUrl

ruta = '/home/fernando/Desktop/Compu2/lab/alumnos/55124-fernando-isaguirre/tp4/images/'
listita = []
for a in range(len(imageSources)):
    listita.append(a)

for url in imageSources:
    cantidad = len(url)
    if (url[cantidad-3::] == "jpg"):
        #donde empieza
        #cantidad de caracteres
        #cada tantos caracteres
        try:
            nombre_imagen= listita.pop()
            urllib.request.urlretrieve(url, ruta+str(nombre_imagen)+".jpg")
            ruta_imagen = '/home/fernando/Desktop/Compu2/lab/alumnos/55124-fernando-isaguirre/tp4/images/'+str(nombre_imagen)
            im = Image.open(ruta_imagen+".jpg").convert('RGB').save(ruta_imagen+".ppm")
            os.remove(ruta_imagen+".jpg")
            #convert('rgb') sirve porque sino salta un error para convertirla a ppm
            color_rojo(ruta_imagen)
            color_azul(ruta_imagen)
            color_verde(ruta_imagen)
        except urllib.error.HTTPError as e:
            print('status', e.code)
            print('reason', e.reason)
    if (url[cantidad-3::] == "png"):
        try:
            nombre_imagen= listita.pop()
            urllib.request.urlretrieve(url, ruta+str(nombre_imagen)+'.png')
            ruta_imagen = '/home/fernando/Desktop/Compu2/lab/alumnos/55124-fernando-isaguirre/tp4/images/'+str(nombre_imagen)
            im = Image.open(ruta_imagen+".png").convert('RGB').save(ruta_imagen+".ppm")
            os.remove(ruta_imagen+".png")
            color_rojo(ruta_imagen)
            color_azul(ruta_imagen)
            color_verde(ruta_imagen)
        except urllib.error.HTTPError as e:
            print('status', e.code)
            print('reason', e.reason)
