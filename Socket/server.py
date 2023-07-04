import socket
import pickle 
from data import *

# localhost or SPECIFIED IP
ip = socket.gethostname()
# port you are concern with 
port = 1234
# Initiallising Socket class 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((ip,port))
# check for new connections
s.listen(5)

# FOR DICT
msg = pickle.dump(MAP_dict)

# FOR LISTS
msg = str(MAP)
msg = msg.encode()


while True:
    # RETURNS client object , client ip
    _client , _addr = s.accept()

    # Send message
    _client.send(msg)
