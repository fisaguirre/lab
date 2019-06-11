#!/usr/bin/python3
""" TP2 para ejercitar sincronizacion y sus problemas"""
import threading
import time
import random


lista_bote = []
lista_de_hinchas = []
condition = threading.Condition()

def a_bordo(hincha):
        #hincha = random.choice(lista_de_hinchas)
        #lista_de_hinchas.remove(hincha)
        hincha_a_subir = lista_de_hinchas.pop()
        #print("se saco un: ",hincha_a_subir)

        if hincha_a_subir == 'R':
                print("vamos river")
        else:
                print("vamos boca")

        lista_bote.append(hincha_a_subir)
        print("el bote es: ",lista_bote)
        #condition.acquire()

        if len(lista_bote) == 4:
                a_remar()
        condition.release()
                #condition.notify()
                #time.sleep(1)
        #condition.release()

        #if( len(lista_bote) == 4 ):
        #        capitan = threading.Thread(target=a_remar())
        #print("el bote queda: ",lista_bote)

def a_remar():
        print("----------------")
        print("Empiezan a remar")
        while True:
                #condition.acquire()
                #condition.wait()
                for personas in range(4):
                        print("se saca del bote: ",lista_bote.pop())
                if len(lista_bote) == 0:
                        break
                #condition.release()                        

def hincha_river():
    condition.acquire()
    hincha = "R"
    lista_de_hinchas.append(hincha)
    a_bordo(hincha)
    if len(lista_bote) == 4:
            print("hay 4")
            condition.wait()
    #while True:
            #condition.acquire()
            #hincha = "R"
            #lista_de_hinchas.append(hincha)
            #a_bordo(hincha)
            #if len(lista_bote) == 4:
            #        condition.wait()

def hincha_boca():
    condition.acquire()
    hincha = "B"
    lista_de_hinchas.append(hincha)
    a_bordo(hincha)
    if len(lista_bote) == 4:
            print("hay 4")
            condition.wait()
    #while True:
    #        condition.acquire()
    #        hincha = "B"
    #        lista_de_hinchas.append(hincha)
    #        a_bordo(hincha)
    #        if len(lista_bote) == 4:
    #                condition.wait()

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

