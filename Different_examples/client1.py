import socket
from time import sleep
server = ('127.0.0.1', 4060)
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Client connected')
while True:
    sleep(5)
    soc.connect(server)
    soc.sendto(b'time', server)
    data = soc.recv(1024)
    print('Now', data, 'date')
    soc.close()
