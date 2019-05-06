#!/usr/bin/python

import csv
 
encabezado = True

with open('archivo.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        if (encabezado == False):
            if float(row[4])>1200 :
                print(row[1])
        encabezado = False