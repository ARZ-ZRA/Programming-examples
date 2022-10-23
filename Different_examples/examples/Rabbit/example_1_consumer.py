import rabbitpy

url = 'amqp://guest:guest@localhost:5672/%2F'
with rabbitpy.Connection(url) as conn:
    with conn.channel() as channel:

        queue = rabbitpy.Queue(channel, 'qqq')

        while len(queue) > 0:
            message = queue.get()
            print('     Massage:')
            print('ID: %s' % message.properties['message_id'])
            print('Time: %s' % message.properties['timestamp'].isoformat())
            print('Body: %s' % message.body)
            message.ack()
