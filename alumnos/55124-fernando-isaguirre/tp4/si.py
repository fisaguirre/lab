
#!/usr/bin/python3


import urllib2
def download(url, NOMBRE):
    try:
        furl = urllib2.urlopen(url)
        f = file("%s.png"%NOMBRE,'wb')
        f.write(furl.read())
        f.close()
    except:
        print 'Unable to download file'

print "Descargar imagenes desde internet:\n"
entrada = raw_input("ingrese url: ")
renombrar = raw_input("nombre: ")
download(entrada,renombrar)