import socket
import threading

ip = socket.gethostname()
my_name = input('Enter your name :').upper()
my_name = str(my_name)


# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 46609
client.connect((ip, port))


def receive():
    while True:
        message = client.recv(1024).decode('utf-8')
        print(message)
        print('')


def write():
    while True:
        message = input('')
        print('')
        messages = my_name + ":" + message
        client.send(messages.encode('utf-8'))            


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
