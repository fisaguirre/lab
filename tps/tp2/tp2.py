#!/usr/bin/python3
""" TP2 para ejercitar sincronizacion y sus problemas"""
import threading
import time
import random

lista_bote = []
lista_de_hinchas = []
condition = threading.Condition()

def a_bordo(hincha):
        hincha_a_subir = lista_de_hinchas.pop()

        if hincha_a_subir == 'R':
                print("vamos river")
        else:
                print("vamos boca")
        time.sleep(1)

        lista_bote.append(hincha_a_subir)
        
        if len(lista_bote) == 4:
                print("¡bote lleno!")
                time.sleep(1)
                a_remar()
                time.sleep(1)
        condition.release()
                #

def a_remar():
        print("----------------")
        print("A REMAR")
        print(lista_bote)
        while True:
                for personas in range(4):
                        print("se baja del bote: ",lista_bote.pop())
                        time.sleep(1)
                if len(lista_bote) == 0:
                        print("Bote libre")
                        print("-------------")
                        break

def hincha_river():
    condition.acquire()
    hincha = "R"
    lista_de_hinchas.append(hincha)
    a_bordo(hincha)
    if len(lista_bote) == 4:
            print("hay 4")
            condition.wait()

def hincha_boca():
    condition.acquire()
    hincha = "B"
    lista_de_hinchas.append(hincha)
    a_bordo(hincha)
    if len(lista_bote) == 4:
            print("hay 4")
            condition.wait()

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

barra_river = threading.Thread(target=barra_brava_river, args=(8,))
barra_boca = threading.Thread(target=barra_brava_boca, args=(8,))

barra_river.start()
barra_boca.start()

barra_river.join()
barra_boca.join()

print("terminaron los viajes ")

