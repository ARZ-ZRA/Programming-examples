import string

import zmq
sub_cont = zmq.Context()
subscr_1 = sub_cont.socket(zmq.SUB)
host = '127.0.0.1'
port = '9090'
subscr_1.connect(f'tcp://{host}:{port}')
subscr_1.setsockopt(zmq.SUBSCRIBE, b'')
while True:
    response_bytes = subscr_1.recv()
    response = response_bytes.decode('utf-8')
    response = response.strip(string.punctuation)
    response = response.replace("'", '')
    if response.startswith(('a','e','i','o','u','A','e','i','o','u')):
        print(response)


