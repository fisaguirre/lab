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
import crear_rojo
import crear_verde
import crear_azul

opciones, argumentos = getopt.getopt(sys.argv[1:], "u:h")

URLs_images = ""

for o in opciones:
    if o[0] == "-h":
        OpcAyuda()
    if o[0] == "-u":
        #La pos. 1 del arreglo constituye la URL de la página.
        URLs_images = o[1]
        print(o[1])

urls = URLs_images

hosts = urls.split(",")

contents = {}
imageSources = []

for host in hosts:
    contents[host] = BeautifulSoup(requests.get(host).text, "html.parser")
    #beautifulsoup extrae datos desde html

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

ruta = 'images/'
lista_numeros_imagenes = []

for i in range(len(imageSources)):
    lista_numeros_imagenes.append(i)

for url in imageSources:
    cantidad = len(url)
    if (url[cantidad-3::] == "jpg"):
        #donde empieza
        #cantidad de caracteres
        #cada tantos caracteres
        try:
            nombre_imagen= lista_numeros_imagenes.pop()
            urllib.request.urlretrieve(url, ruta+str(nombre_imagen)+".jpg")
            ruta_imagen = 'images/'+str(nombre_imagen)
            im = Image.open(ruta_imagen+".jpg").convert('RGB').save(ruta_imagen+".ppm")
            os.remove(ruta_imagen+".jpg")
            #convert('rgb') sirve porque sino salta un error para convertirla a ppm
            crear_rojo.rojo(ruta_imagen)
            crear_azul.azul(ruta_imagen)
            crear_verde.verde(ruta_imagen)
        except urllib.error.HTTPError as e:
            print('status', e.code)
            print('reason', e.reason)
    if (url[cantidad-3::] == "png"):
        try:
            nombre_imagen= lista_numeros_imagenes.pop()
            urllib.request.urlretrieve(url, ruta+str(nombre_imagen)+'.png')
            ruta_imagen = 'images/'+str(nombre_imagen)
            im = Image.open(ruta_imagen+".png").convert('RGB').save(ruta_imagen+".ppm")
            os.remove(ruta_imagen+".png")
            crear_rojo.rojo(ruta_imagen)
            crear_azul.azul(ruta_imagen)
            crear_verde.verde(ruta_imagen)
        except urllib.error.HTTPError as e:
            print('status', e.code)
            print('reason', e.reason)
