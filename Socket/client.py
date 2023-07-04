import socket
import pickle

ip = socket.gethostname()
port = 1234
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,port))

# Amount of data should pass at 1 chunk = 1024
msg = s.recv(1024)

# FOR DICTS
map = pickle.loads(msg)

# FOR LISTS
map = eval(msg.decode("utf-8"))
for i in map:
    print(i)
