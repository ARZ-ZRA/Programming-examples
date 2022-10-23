# Подтверждение издателю как альтернатива с малым весом транзакциям

import rabbitpy

with rabbitpy.Connection() as conn:
    with conn.channel() as channel:
        exchange = rabbitpy.Exchange(channel, 'exhg')
        exchange.declare()
        channel.enable_publisher_confirms()
        message = rabbitpy.Message(channel,
                                   '  |:-)',
                                   )
        if message.publish('exhg', 'important_msg'):
            print('The msg was confirmed')