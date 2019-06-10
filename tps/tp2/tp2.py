#!/usr/bin/python3
""" TP2 para ejercitar sincronizacion y sus problemas"""
import threading
import time
import random


lista_bote = []
lista_de_hinchas = []

def a_bordo():
        hincha = random.choice(lista_de_hinchas)
        if(hincha == 'R'):
                print("vamos river")
        else:
                print("vamos boca")
        lista_bote.append(hincha)
        print("el bote queda: ",lista_bote)

def hincha_river():
    #print("vamos river")
    lista_de_hinchas.append('R')
    a_bordo()

def hincha_boca():
    #print("vamos boca")
    lista_de_hinchas.append('B')
    a_bordo()

def barra_brava_river():
    """ Generacion de hinchas de River"""
    asd = 0
    while asd < 20:
        #time.sleep(random.randrange(0, 5))
        r = threading.Thread(target=hincha_river)
        r.start()
        asd = asd + 1

def barra_brava_boca():
    """ Generacion de hinchas de Boca"""
    viajes = 0
    while viajes < 20:
        #time.sleep(random.randrange(0, 5))
        b = threading.Thread(target=hincha_boca)
        b.start()
        viajes = viajes + 1

t1 = threading.Thread(target=barra_brava_river)
t2 = threading.Thread(target=barra_brava_boca)

t1.start()
t2.start()

t1.join()
t2.join()
print("la cola quedo: ",lista_de_hinchas)

print("terminaron los viajes ")
