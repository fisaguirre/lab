#!/usr/bin/python3
""" TP2 para ejercitar sincronizacion y sus problemas"""
import threading
import time
import random


lista_bote = []
lista_de_hinchas = []
condition = threading.Condition()

def a_bordo(hincha):
        hincha = random.choice(lista_de_hinchas)
        lista_de_hinchas.remove(hincha)
        hincha_a_subir = lista_de_hinchas.pop(hincha)

        if hincha_a_subir == 'R':
                print("vamos river")
        else:
                print("vamos boca")
        lista_bote.append(hincha_a_subir)

        if len(lista_bote) == 4:
                a_remar()
        #if( len(lista_bote) == 4 ):
        #        capitan = threading.Thread(target=a_remar())
        #print("el bote queda: ",lista_bote)

def a_remar():
        print("----------------")
        print("Empiezan a remar")
        while True:
                lista_bote.pop()
                if len(lista_bote) == 0:
                        break;

def hincha_river():
    #lista_de_hinchas.append('R')
    #a_bordo()
    while True:
            condition.acquire()
            hincha = 'R'
            lista_de_hinchas.append(hincha)
            a_bordo(hincha)

def hincha_boca():
    #lista_de_hinchas.append('B')
    #a_bordo()
    while True:
            hincha = 'B'
            lista_de_hinchas.append(hincha)
            a_bordo(hincha)

def barra_brava_river(cantidad_hinchas):
    """ Generacion de hinchas de River"""
    viajes = 0
    while viajes < cantidad_hinchas:
        #time.sleep(random.randrange(0, 5))
        river = threading.Thread(target=hincha_river)
        river.start()
        viajes = viajes + 1

def barra_brava_boca(cantidad_hinchas):
    """ Generacion de hinchas de Boca"""
    viajes = 0
    while viajes < cantidad_hinchas:
        #time.sleep(random.randrange(0, 5))
        boca = threading.Thread(target=hincha_boca)
        boca.start()
        viajes = viajes + 1

barra_boca = threading.Thread(target=barra_brava_river, args=(8,))
t2 = threading.Thread(target=barra_brava_boca, args=(8,))

barra_boca.start()
t2.start()

barra_boca.join()
t2.join()

print("terminaron los viajes ")


lista = ['1','2','3','4']

def hola(var):
        print("var es: ",var)
        print("lo voy a sacar")
        nuevo = lista.pop(int(var))
        print("el nuevo es: ",nuevo)

var = '4'
lista.append(var)
print("var:",var)
print("lista:",lista)
hola(var)
print("quedo: ",lista)