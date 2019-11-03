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
import os
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
        try:
            nombre_imagen= listita.pop()
            urllib.request.urlretrieve(url, ruta+str(nombre_imagen)+".jpg")
            a = '/home/fernando/Desktop/Compu2/lab/alumnos/55124-fernando-isaguirre/tp4/images/'+str(nombre_imagen)
            im = Image.open(a+".jpg").convert('RGB').save(a+".ppm")
            os.remove(a+".jpg")
            #convert('rgb') sirve porque sino salta un error para convertirla a ppm
        except urllib.error.HTTPError as e:
            print('status', e.code)
            print('reason', e.reason)
    if (url[cantidad-3::] == "png"):
        try:
            nombre_imagen= listita.pop()
            urllib.request.urlretrieve(url, ruta+str(nombre_imagen)+'.png')
            a = '/home/fernando/Desktop/Compu2/lab/alumnos/55124-fernando-isaguirre/tp4/images/'+str(nombre_imagen)
            im = Image.open(a+".png").convert('RGB').save(a+".ppm")
            os.remove(a+".png")
        except urllib.error.HTTPError as e:
            print('status', e.code)
            print('reason', e.reason)

#agregar para ponerle nombres a las imagenes