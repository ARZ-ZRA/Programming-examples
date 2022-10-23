import hashlib
import rabbitpy
import os

conn = rabbitpy.Connection()
channel = conn.channel()
queue_name = 'hasihg_worker_%s' % os.getpid()
queue = rabbitpy.Queue(channel,
                       queue_name,
                       auto_delete=True,
                       durable=False,
                       exclusive=True)
if queue.declare():
    print('Queue worker declare')

if queue.bind('fanout_rpc_request'):
    print('Queue worker bound')

for msg in queue.consume_messages():
    print(1)
    hash_obj = hashlib.md5(msg.body)
    print('Image of correlation id %s has a hash of %s'%
          (msg.properties['correlation_id'],hash_obj.hexdigest()))
msg.ack
