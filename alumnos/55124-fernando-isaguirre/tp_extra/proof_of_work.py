#!/usr/bin/python3
import argparse
import hashlib
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

def ArgsParse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--cantidad", dest="cantidad", nargs = "?", default = 2, type = int, help = "Cantidad hash") # it seems like nargs is not required...
    return parser.parse_args()

argumento = ArgsParse()
cantidad_hash = argumento.cantidad


d = datetime.today()
t = int(d.timestamp())
a = str(t)
print(a)
data = 'Hola Mono!'
prevHash = '0'
maxLoops = 100000000
difficulty = 5
breakCondition = '0' * difficulty

def hasheo(new_prev):
    print("nuevo proceso")
    for idx in range(1, maxLoops):
        s = str(str(t) + data + str(idx) + new_prev).encode('utf-8')
        hash = hashlib.sha256(s)
        hash = hash.hexdigest()
        if hash[0:difficulty] == breakCondition:
            #print('HASH_nuevo: ' + hash)
            #print('Idx_nuevo: ' + str(idx))
            return hash

def pool_executor(new_prev):
    executor = ThreadPoolExecutor(max_workers=4)
    for i in range(0,4):
        future = executor.submit(hasheo, (new_prev))
        if future.result():
            return future.result()

for idx in range(1, maxLoops):
    s = str(str(t) + data + str(idx) + prevHash).encode('utf-8')
    hash = hashlib.sha256(s)
    hash = hash.hexdigest()   
    if hash[0:difficulty] == breakCondition:
        print('HASH: ' + hash)
        print('Idx: ' + str(idx))
        new_prev = hash
        for i in range(cantidad_hash):
            nuevo_hash = pool_executor(new_prev)
            print("HASH ",i,":",nuevo_hash)
        break
