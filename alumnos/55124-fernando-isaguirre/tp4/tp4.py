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
    print("el host es: ",host)
    images = contents[host].findAll("img")
    for img in images:
        imgUrl = img.get("src")
        print("mia es: ",imgUrl)
        if imgUrl[0] == "/":
            #esto es para los que le falta el hostname
            imgUrl = host + imgUrl
            print("segunda es: ",imgUrl)
        imageSources.append(imgUrl)

for i in range(len(imageSources)):
    src = imageSources[i]
    #print(imageSources[i])
    parsedUrl = urllib.parse.urlparse(src)
    #esto es para parsear las urls de la lista, o sea, devuelve los elementos dela estructura de la url,scheme,netloc,path...
    newUrl = parsedUrl.scheme + "://" + parsedUrl.netloc + parsedUrl.path
    imageSources[i] = newUrl

for url in imageSources:
    cantidad = len(url)
    print("la url es: ",url)
    if (url[cantidad-3::] == "jpg" or url[cantidad-3::] == "png"):
        try:
            urllib.request.urlretrieve(url, '/home/fernando/Desktop/Compu2/lab/alumnos//55124-fernando-isaguirre/tp4/images/imagen.jpg')
        except urllib.error.HTTPError as e:
            print('status', e.code)
            print('reason', e.reason)

#agregar para ponerle nombres a las imagenes