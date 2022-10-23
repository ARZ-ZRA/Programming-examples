# Применение режима no-ack для быстрей пропускной способности
import rabbitpy

with rabbitpy.Connection() as conn:
    with conn.channel() as channel:
        queue = rabbitpy.Queue(channel,
                               'test-msg')

        for msg in queue.consume_messages(no_ack=True):
            msg.pprint()
