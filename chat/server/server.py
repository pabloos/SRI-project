#!/usr/bin/env python3

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

import db

clients = {}
addresses = {}

BUFSIZ = 1024
ADDR = ('', 33000)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s se ha contectado" % client_address)
        client.send(bytes('\n===================\nBienvenido al pyChat\n===================', "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()

def handle_client(client):
    name = ''
    welcome = '\nSelecciona una opcion: \na) Login\nb) Crear usuario'

    client.send(bytes(welcome,"utf8"))

    option = client.recv(BUFSIZ).decode("utf8")

    if option == 'a':
        client.send(bytes('introduce tu nombre:',"utf8"))
        name = client.recv(BUFSIZ).decode("utf8")
        client.send(bytes('introduce tu contrasena:',"utf8"))
        passwd = client.recv(BUFSIZ).decode("utf8")

        if db.login(name, passwd):
            print('exito en autenticacion')
            client.send(bytes('Empieza a escribr. Pulsa ENTER para enviar', "utf8"))

        else:
            print('fallo de autenticacion')
            client.send(bytes('Pass incorrecta', "utf8"))

    elif option == 'b':
        client.send(bytes('introduce tu nombre:',"utf8"))
        name = client.recv(BUFSIZ).decode("utf8")
        client.send(bytes('introduce tu contrasena:',"utf8"))
        passwd = client.recv(BUFSIZ).decode("utf8")
        db.createUser(name, passwd)

    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("exit", "utf8"):
            broadcast(msg, name+": ")
            db.addMessage(msg.decode("utf8"), name)
        else:
            client.send(bytes("exit", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s ha salido de la sala" % name, "utf8"))
            break

def broadcast(msg, prefix=""):
    for sock in clients:
        sock.send(bytes(prefix, "utf8") + msg)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()