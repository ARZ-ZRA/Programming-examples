import zmq
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect('tcp://localhost:5050')
socket.send(b'time')
response_bytes = socket.recv()
response_bytes_decode = response_bytes.decode('utf-8')
print("It's ", response_bytes_decode, 'now')
socket.close()
