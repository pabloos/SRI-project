#!/usr/bin/env python3

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

BUFSIZ = 1024

import sys

def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            print(msg)
        except OSError:
            break

ADDR = ('localhost', 33000)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()

while True:
    mensaje = input()
    if mensaje == "exit":
        client_socket.send(bytes(mensaje, "utf8"))
        client_socket.close()
        sys.exit()
    
    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[K") #clear line
    client_socket.send(bytes(mensaje, "utf8"))