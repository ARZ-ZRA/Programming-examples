import rabbitpy

queue = rabbitpy.Queue(rabbitpy.Connection().channel(), 'test-msg')
queue.declare()
for i in range(10):
    rabbitpy.publish('amqp://guest:guest@localhost:5672/%2F', '', 'test-msg', ':-) %s'%i)
rabbitpy.publish('amqp://guest:guest@localhost:5672/%2F', '', 'test-msg', 'stop')