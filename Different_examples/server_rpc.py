from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime


def time(value):
    if value == 'time':
        return datetime.isoformat(datetime.now())


server = SimpleXMLRPCServer(('127.0.0.1', 6060))
server.register_function(time, 'time')
server.serve_forever()
