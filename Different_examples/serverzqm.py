import zmq
from datetime import datetime
#saddr = ('localhost', 5050)
context = zmq.Context()
#socket = context.socket()
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:5050")
requests_bytes = socket.recv()
requests_bytes_decode = requests_bytes.decode('utf-8')
print('Client request key = '+requests_bytes_decode+', at time ', datetime.now())
if requests_bytes_decode == 'time':
    socket.send((datetime.isoformat(datetime.now())).encode('utf-8'))


