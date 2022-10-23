import string

import zmq
ctx = zmq.Context()
subsc_2 = ctx.socket(zmq.SUB)
host = '127.0.0.1'
port = '9090'
subsc_2.connect(f'tcp://{host}:{port}')
subsc_2.setsockopt(zmq.SUBSCRIBE, b'')
while True:
    response_bytes = subsc_2.recv()
    response = response_bytes.decode('utf-8')
    response = response.replace("'", '')
    response = response.strip(string.punctuation)
    if len(response) == 5:
        print(response)