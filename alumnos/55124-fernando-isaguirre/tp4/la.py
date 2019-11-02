
#!/usr/bin/python3
import request

"""
for url in imageSources:
    cantidad = len(url)
    print("la url es: ",url)
    if (url[cantidad-3::] == "png"):
        nombre_local_imagen = "go.png" 
        imagen = requests.get(url).content
        with open(nombre_local_imagen, 'wb') as handler:
            handler.write(imagen)
        break
"""


url_imagen = "https://www.www.lavanguardia.com/r/GODO/LV/p6/WebSite/2019/04/02/Recortada/img_lteixidor_20180727-125926_imagenes_lv_colaboradores_lteixidor_gato_2570_26-300-kLmH--656x656@LaVanguardia-Web.jpg" # El link de la imagen
nombre_local_imagen = "go.jpg" # El nombre con el que queremos guardarla
imagen = requests.get(url_imagen).content
with open(nombre_local_imagen, 'wb') as handler:
	handler.write(imagen)
