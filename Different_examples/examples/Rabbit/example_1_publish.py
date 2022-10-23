import rabbitpy

with rabbitpy.Connection('amqp://guest:guest@localhost:5672/%2F') as conn:
    with conn.channel() as channel:

        exchange = rabbitpy.Exchange(channel, 'arz')
        exchange.declare()

        queue = rabbitpy.Queue(channel, 'qqq')
        queue.declare()

        queue.bind(exchange, 'www-route')

        for i in range(10):
            messsage = rabbitpy.Message(channel,
                                        'Image %i' % i,
                                        {'content_type': 'text/plain'},
                                        opinionated=True)
            messsage.publish(exchange, 'www-route')