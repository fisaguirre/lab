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
import multiprocessing as mp
import time
#el unico problema es al querer descargar la imagen con urlretrieve.... en asincronismo
def descarga_conversion(url,nombre_imagen,extension):
    print("se inicia un hijo: ",os.getpid())
    ruta = 'images/'
    ruta_imagen = ruta+nombre_imagen+extension
    print("la ruta es: ",ruta_imagen)
    if (extension == ".jpg" or extension == ".png"):
        print("extension : ",extension,"con proceso: ",os.getpid())
        #donde empieza
        #cantidad de caracteres
        #cada tantos caracteres
        try:
            print("entra al try")
            urllib.request.urlretrieve(url, ruta_imagen)
            #hay un problema al descargar las imagenes con asincronismo
            #nomb = "blank"
            #ex = ".jpg"
            print("1")
            im = Image.open(ruta_imagen).convert('RGB').save(ruta+nombre_imagen+".ppm")
            #im = Image.open(ruta+nomb+ex).convert('RGB').save(ruta+nomb+".ppm")
            print("2")
            os.remove(ruta_imagen)
            #convert('rgb') sirve porque sino salta un error para convertirla a ppm
            crear_rojo.rojo(ruta+nombre_imagen)
            #crear_rojo.rojo(ruta+nomb)
            print("3")
            print("4")
            crear_azul.azul(ruta+nombre_imagen)
            #crear_azul.azul(ruta+nomb)
            print("4")
            crear_verde.verde(ruta+nombre_imagen)
            #crear_verde.verde(ruta+nomb)
            print("5")
        except urllib.error.HTTPError as e:
            print('status', e.code)
            print('reason', e.reason)
        print("termina")
    else:
        print("es otra")
    print("termina hijo")
    return 

#def call(retorno):
#    print("se devuelve: ",retorno)

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

pool = mp.Pool(4)
start_time = time.time()
for url in imageSources:
    contador = 0
    url_split = url.split("/")
    longitud_url_split = len(url_split)
    for split in url_split:
        contador = contador + 1
        if (contador == longitud_url_split):
            nombre_imagen = split[:len(split)-4:]
            extension = split[-4::]
            print(".")
            #descarga_conversion(url,nombre_imagen,extension)
            pool.apply_async(descarga_conversion, args=(url,nombre_imagen,extension,))
            #el unico que no funciona es el pool.apply_async
elapsed_time = time.time() - start_time
print("tiempo total: ",elapsed_time-start_time)
