#!/usr/bin/python
import os

leido = 0
EOF = True

while EOF :
    leido = os.read(0,1000)
    #lee por teclado hasta 1000 bytes
    if len(leido) < 1000:
        #si la longitud de leido(lo que se ingresa por teclado) es menor a 1000 bytes
        #eof es falso y el bucle se va a cortar(o sea, pasa cuando ya no tenemos nada mas para leer)
        EOF = False

    
def reverse(leido):
    i = 0
    leido3 = ""
    cant = 0
    cant = cant + len(leido.strip())
    leido_final = ""
    for f in leido:
        if(leido[i]!= " "):
            leido3 = leido3+leido[i]
        if( (leido[i]== " ") or (i==cant) ):
            leido4=leido3[::-1]
            #[desde:hasta(sin incluir):salto]
            #[inicio:fin(sin incluir):salto]
            leido3=""
            leido_final = leido_final + leido4.strip() + " "
            leido4 = ""
        i+=1
    os.write(1,leido_final + "\n")

reverse(leido)