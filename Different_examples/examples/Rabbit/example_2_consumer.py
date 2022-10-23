import rabbitpy

with rabbitpy.Connection() as conn:
    with conn.channel() as channel:
        for message in rabbitpy.Queue(channel, 'test-msg'):
            message.pprint()
            message.ack
            if message.body == 'stop':
                break


