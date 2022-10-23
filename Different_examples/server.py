import zmq
import pickle
import json

def run_daemon():
    memory={}
    context=zmq.Context()
    socket=context.socket(zmq.REP)
    socket.bind('tcp://127.0.0.1:4040')
    
    while True:
        try:
            command,key,data=pickle.loads(socket.recv())
            if command=='set':
                memory[key]=data
                socket.send(b'all right')
            elif command=='get':
                result=memory.get(key,None)
                socket.send(pickle.dumps(result))
            else:
                print('Error')
        except Exception as e:
            print(e)
if __name__=='__main__':
    run_daemon()