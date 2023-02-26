import socket
from socket import AF_INET,SOCK_STREAM
from threading import Thread

HOST = socket.gethostbyname(socket.gethostname())
PORT = 55555
ADDR = (HOST,PORT)
BUFFERSIZE = 1024
FORMAT = 'ascii'

try:
    SERVER = socket.socket(AF_INET,SOCK_STREAM)
    SERVER.bind(ADDR)
    #SERVER.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    print("[SERVER is ONLINE]")
    SERVER.listen()
    print("[SERVER is LISTENING...]")

except socket.error as E:
    print(E)
    print("[SERVER CAN'T STARTED!]")

clients = []
nicknames = []
clients_addr = []


def broadcast(message):
    for client in clients:
        client.send(message)
    print(message.decode(FORMAT))

def handle(client):
    while True:
        try:
            message = client.recv(BUFFERSIZE)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"[{nickname} LEFT THE CHAT!]".encode(FORMAT))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client,addr = SERVER.accept()
        print(f"[{addr} CONNECTED to SERVER]")
        nickname = client.recv(BUFFERSIZE).decode(FORMAT)
        clients.append(client)
        nicknames.append(nickname)

        client.send(f"[WELCOME to PANDORA7 {nickname}]".encode(FORMAT))

        handle_Thread = Thread(target=handle,args=(client,))
        handle_Thread.start()

receive()