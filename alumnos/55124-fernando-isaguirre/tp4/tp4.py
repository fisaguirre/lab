#!/usr/bin/python3
import os, sys
import argparse, getopt
import requests
import urllib.request, urllib.parse, urllib.error
from PIL import Image
from bs4 import BeautifulSoup
import crear_rojo, crear_verde, crear_azul
from concurrent.futures import ThreadPoolExecutor

def parseo(hosts):
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
        parsedUrl = urllib.parse.urlparse(src)
        #esto es para parsear las urls de la lista, o sea, devuelve los elementos dela estructura de la url,scheme,netloc,path...
        newUrl = parsedUrl.scheme + "://" + parsedUrl.netloc + parsedUrl.path
        imageSources[i] = newUrl
    return imageSources


def nombre_extension(url):
    nombre_imagen = (url.split("/")[-1])[0:-4]
    extension = url[-4::]
    return(nombre_imagen,extension)

def conversion(ruta):
    executor_convert = ThreadPoolExecutor(max_workers=3)
    fut_1 = executor_convert.submit(crear_rojo.rojo, (ruta))
    fut_2 = executor_convert.submit(crear_azul.azul, (ruta))
    fut_3 = executor_convert.submit(crear_verde.verde, (ruta))

def descarga(url):
    nombre_imagen,extension = nombre_extension(url)
    ruta = 'images/'
    ruta_imagen = ruta+nombre_imagen+extension
    if (extension == ".jpg" or extension == ".png"):
        try:
            urllib.request.urlretrieve(url, ruta_imagen)
            im = Image.open(ruta_imagen).convert('RGB').save(ruta+nombre_imagen+".ppm")
            os.remove(ruta_imagen)
            #convert('rgb') sirve porque sino salta un error para convertirla a ppm
            conversion(ruta+nombre_imagen)
        except urllib.error.HTTPError as e:
            print('status', e.code)
            print('reason', e.reason)

def pool_executor(imageSources):
    print("entra")
    executor_download = ThreadPoolExecutor(max_workers=len(imageSources))
    for i in range(0,len(imageSources)):
        if (len(imageSources)!= 0):
            future = executor_download.submit(descarga, (imageSources.pop()))

opciones, argumentos = getopt.getopt(sys.argv[1:], "u:h")

URLs_images = ""

for o in opciones:
    if o[0] == "-h":
        OpcAyuda()
    if o[0] == "-u":
        URLs_images = o[1]
        print(o[1])

urls = URLs_images

hosts = urls.split(",")

imageSources = parseo(hosts)

pool_executor(imageSources)

#with ThreadPoolExecutor(max_workers=80) as executor:
#    for i in range(0,80):
#        future = executor.submit(descarga_conversion, (imageSources.pop()))

#duda: primero se crean todas las promesas y luego se ejecutan?

#paginas para descargar imagenes
#https://www.miarevista.es/hogar/articulo/que-significa-el-ronroneo-de-un-gato-151446482278
#https://www.elconfidencial.com/alma-corazon-vida/2019-05-26/perros-sonrien-mascotas-simpaticos-chuchos_2010406/
