#!/usr/bin/python3
import requests
import urllib.request, urllib.parse, urllib.error
from PIL import Image
from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys,getopt,os
import crear_rojo,crear_verde,crear_azul
import multiprocessing as mp

def parseo(hosts):
    contents = {}
    imageSources = []

    for host in hosts:
        contents[host] = BeautifulSoup(requests.get(host).text, "html.parser")

    for host in hosts:
        images = contents[host].findAll("img")
        for img in images:
            imgUrl = img.get("src")
            if imgUrl[0] == "/":
                imgUrl = host + imgUrl
            imageSources.append(imgUrl)

    for i in range(len(imageSources)):
        src = imageSources[i]
        parsedUrl = urllib.parse.urlparse(src)
        newUrl = parsedUrl.scheme + "://" + parsedUrl.netloc + parsedUrl.path
        imageSources[i] = newUrl
    return imageSources

def asincronismo(imageSources):
    pool = mp.Pool(4)
    for url in imageSources:
        print(".")
        pool.apply_async(descarga, args=(url,))

def nombre_extension(url):
    nombre_imagen = (url.split("/")[-1])[0:-4]
    extension = url[-4::]
    return(nombre_imagen,extension)

def descarga(url):
    nombre_imagen,extension = nombre_extension(url)
    ruta = 'images/'
    ruta_imagen = ruta+nombre_imagen+extension
    if (extension == ".jpg" or extension == ".png"):
        try:
            urllib.request.urlretrieve(url, ruta_imagen)
            im = Image.open(ruta_imagen).convert('RGB').save(ruta+nombre_imagen+".ppm")
            os.remove(ruta_imagen)
            #conversion(ruta+nombre_imagen)
            crear_rojo.rojo(ruta+nombre_imagen)
        except urllib.error.HTTPError as e:
            print('status', e.code)
            print('reason', e.reason)

opciones, argumentos = getopt.getopt(sys.argv[1:], "u:h")

URLs_images = ""

for o in opciones:
    if o[0] == "-h":
        OpcAyuda()
    if o[0] == "-u":
        URLs_images = o[1]
        print(o[1])

urls = URLs_images

urls = args.url
hosts = urls.split(",")
imageSources = parseo(hosts)

asincronismo(imageSources)
