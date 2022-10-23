from time import sleep
import zmq
context = zmq.Context()
publisher = context.socket(zmq.PUB)
host = '127.0.0.1'
port = '9090'
publisher.bind(f'tcp://{host}:{port}')
sleep(1)
poem = ''' We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.
All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.
Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.
May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great world's show at Paris.
Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek, then songs or glees
We could not sing, oh! queen of cheese.
We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon.
'''
for word in poem.split():
    #sleep(1)
    poem_byte = bytes(word, "utf-8")
    publisher.send(poem_byte)
