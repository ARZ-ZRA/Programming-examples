import xmlrpc.client
with xmlrpc.client.ServerProxy('http://localhost:6060/') as proxy:
    value='time'
    print('It time is ', proxy.time(value))


