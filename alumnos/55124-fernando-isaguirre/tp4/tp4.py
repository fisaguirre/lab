#!/usr/bin/python3
import argparse
import requests
import re
import urllib.request, urllib.parse
from PIL import Image
from bs4 import BeautifulSoup
import random

# Accept arguments
argumentParser = argparse.ArgumentParser()
argumentParser.add_argument("-u", "--url", dest = "urls", nargs = "+", required = True, help = "URL's to be fetched")
args = argumentParser.parse_args()

# Auxiliar variables
hosts = args.urls
contents = {}
imageSources = []

# Get hosts HTML (using Beautiful Soup)
for host in hosts:
    contents[host] = BeautifulSoup(requests.get(host).text, "html.parser")

# Extract images
for host in hosts:
    images = contents[host].findAll("img")
    for img in images:
        imgUrl = img.get("src")
        if imgUrl[0] == "/":
            imgUrl = host + imgUrl
        imageSources.append(imgUrl)

for i in range(len(imageSources)):
    src = imageSources[i]
    #print(imageSources[i])
    parsedUrl = urllib.parse.urlparse(src)
    newUrl = parsedUrl.scheme + "://www." + parsedUrl.netloc + parsedUrl.path
    imageSources[i] = newUrl

lista = []
for item in imageSources:
    print("me queda: ",item)
    


url_imagen = "https://www.www.lavanguardia.com/r/GODO/LV/p6/WebSite/2019/04/02/Recortada/img_lteixidor_20180727-125926_imagenes_lv_colaboradores_lteixidor_gato_2570_26-300-kLmH--656x656@LaVanguardia-Web.jpg" # El link de la imagen
nombre_local_imagen = "go.jpg" # El nombre con el que queremos guardarla
imagen = requests.get(url_imagen).content
with open(nombre_local_imagen, 'wb') as handler:
	handler.write(imagen)
