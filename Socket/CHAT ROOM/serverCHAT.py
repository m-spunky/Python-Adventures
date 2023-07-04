from socket import *
from threading import *


clients = []


def clientThread(clientSocket, clientAddress):
    while True:
        global clients
        messagefull = clientSocket.recv(1024).decode("utf-8")

        message1 = messagefull.split(':')

        message_name = message1[0]
        message = message1[1]

        full_message = message_name + ' : ' + message

        for client in clients:
            # if client is not clientSocket:
            if client is not clientSocket:
                client.send((full_message).encode("utf-8"))

        if not message:
            clients.remove(clientSocket)
            print(clientAddress[0] + ":" +
                  str(clientAddress[1]) + " disconnected")
            break

    clientSocket.close()


hostSocket = socket(AF_INET, SOCK_STREAM)
hostSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

ip = gethostname()
port = 46609

hostSocket.bind((ip, port))

print('socket has bounded with:', ip)

hostSocket.listen(4)

print("Waiting for connection...")


while True:
    clientSocket, clientAddress = hostSocket.accept()
    clients.append(clientSocket)
    thread = Thread(target=clientThread, args=(clientSocket, clientAddress, ))
    thread.start()
