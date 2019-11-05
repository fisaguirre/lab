#!/usr/bin/python3

import array
import os

def azul(ruta):
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