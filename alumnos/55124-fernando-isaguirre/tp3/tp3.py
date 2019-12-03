#!/usr/bin/python
import socket
import threading

def http_request(host):
    socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_servidor.connect((host, 80))
    #socket_servidor.send("GET / HTTP/1.0\r\n\r\n")
    request_header = 'GET / HTTP/1.0\r\nHost: www.'+host+'\r\n\r\n'
    #no funciona con version 1.1
    socket_servidor.send(request_header)
    return socket_servidor

def http_response(socket_servidor):
    response = ""
    while True:
        recv = socket_servidor.recv(4096)
        #conn_cliente.send(recv)
        if not recv:
            break
        response += recv 
    return response

def proxy(conn_cliente):
    leido = str(conn_cliente.recv(2048))
    print leido
    host = leido.split("Host: ")[1]
    host = host.splitlines()[0]

    socket_servidor = http_request(host)
    
    response = http_response(socket_servidor)

    conn_cliente.send(response)

    socket_servidor.close
    conn_cliente.close()
print("hola")
socket_cliente = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
# para que no diga address already in use ...
socket_cliente.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#socket_cliente.bind(("127.0.0.1", 8080))
socket_cliente.bind(("192.168.1.40", 8000))
socket_cliente.listen(5)

while True:
    conn_cliente,address_cliente = socket_cliente.accept()
    print("---------------------------")
    cliente_1 = threading.Thread(target = proxy, args = (conn_cliente,))
    cliente_1.start()
