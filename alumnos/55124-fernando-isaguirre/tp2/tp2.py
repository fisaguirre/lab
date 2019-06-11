#!/usr/bin/python3

""" TP2 para ejercitar sincronizacion y sus problemas"""

import threading
import time
import random

lista_bote = []
lista_de_hinchas = []
condition = threading.Condition()

def no_patotear():
        while lista_bote.count("R") == 3 or lista_bote.count("B") == 3:
                lista_de_hinchas.append(lista_bote.pop(0))
                lista_bote.append(lista_de_hinchas.pop(0))
        else:
                print("Bote despues de la distribucion pareja:", lista_bote)

def a_bordo():
        #print("Estan esperando:", lista_de_hinchas)
        hincha_a_subir = lista_de_hinchas.pop()

        if hincha_a_subir == 'R':
                print("vamos river")
        else:
                print("vamos boca")
        time.sleep(1)
        lista_bote.append(hincha_a_subir)
        if len(lista_bote) == 4:
                no_patotear()
                print("¡bote lleno!")
                time.sleep(1)
                a_remar()
                time.sleep(1)
                #condition.notify()
        condition.release()

def a_remar():
        print("----------------")
        print("¡A REMAR!")
        print(lista_bote)
        while True:
                for personas in range(4):
                        print("se baja del bote:", lista_bote.pop())
                        time.sleep(1)
                if len(lista_bote) == 0:
                        print("Bote libre")
                        print("-------------")
                        break

def hincha_river():
    hincha = "R"
    lista_de_hinchas.append(hincha)
    condition.acquire()
    a_bordo()
    if len(lista_bote) == 4:
            condition.wait()


def hincha_boca():
    hincha = "B"
    lista_de_hinchas.append(hincha)
    condition.acquire()
    a_bordo()
    if len(lista_bote) == 4:
            condition.wait()

def barra_brava_river(cantidad_hinchas):
    """ Generacion de hinchas de River"""
    for cantidad in range(cantidad_hinchas):
        time.sleep(random.randrange(0, 5))
        river = threading.Thread(target=hincha_river)
        river.start()

def barra_brava_boca(cantidad_hinchas):
    """ Generacion de hinchas de Boca"""
    for cantidad in range(cantidad_hinchas):
        time.sleep(random.randrange(0, 5))
        boca = threading.Thread(target=hincha_boca)
        boca.start()

if __name__ == "__main__":
        barra_river = threading.Thread(target=barra_brava_river, args=(20,))
        barra_boca = threading.Thread(target=barra_brava_boca, args=(20,))

        barra_river.start()
        barra_boca.start()

        barra_river.join()
        barra_boca.join()

        #print("terminaron los viajes ")

