from datetime import datetime
import socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('127.0.0.1', 4060))
socket.listen(5)
conn, addr = socket.accept()
print('Connected', addr)

while True:
    data = conn.recv(1024)
    print(data)
    if data == b'time':
        f = datetime.now()
        conn.send(bytes(f.isoformat(), encoding='utf-8'))
    socket.close()
