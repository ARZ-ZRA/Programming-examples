# Подтверждение множества сообщений за один раз
import rabbitpy

with rabbitpy.Connection() as conn:
    with conn.channel() as channel:
        channel.prefetch_count(10)
        unacknowleged = 0
        for msg in rabbitpy.Queue(channel, 'test-msg'):
            msg.pprint()
            unacknowleged += 1
            if unacknowleged == 10:
                msg.ack(all_previous=True)
                unacknowleged = 0

