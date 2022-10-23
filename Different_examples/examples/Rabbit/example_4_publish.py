# Использование Альтернативного обмена для не выполнивших маршрут сообщений

import rabbitpy

with rabbitpy.Connection() as conn:
    with conn.channel() as channel:
        exchange_alternate = rabbitpy.Exchange(channel,
                                               'exhg_1_alter',
                                               exchange_type='fanout')
        exchange_alternate.declare()
        exchange = rabbitpy.Exchange(channel,
                                     'exhg_1',
                                     exchange_type='topic',
                                     arguments={'alternate-exchange': 'exchange_alternate.name'})
        exchange.declare()

        queue = rabbitpy.Queue(channel, 'unroutable_msg')
        queue.declare()

        if queue.bind(exchange_alternate, '#'):
            print('Queue bound to alternate-exchange')
