# Обслуживание отказов узла с помощью очередей HA
import rabbitpy

conn = rabbitpy.Connection()

try:
    with conn.channel() as channel:
        queue = rabbitpy.Queue(channel,
                               'queue_HA',
                               arguments={'x_ha_policy': 'all'})
        if queue.declare():
            print('Queue declare')
except rabbitpy.exceptions.RemoteClosedChannelException as error:
    print('Queue declare failed: %s' % error)