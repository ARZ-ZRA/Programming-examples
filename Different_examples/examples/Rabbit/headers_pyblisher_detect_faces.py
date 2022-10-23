import time
import rabbitpy
import os
import cv2

conn = rabbitpy.Connection()
channel = conn.channel()

conn = rabbitpy.Connection()
channel = conn.channel()

queue_name = 'response_queue_%s'%os.getpid()
response_queue = rabbitpy.Queue(channel,
                                queue_name,
                                auto_delete=True,
                                durable=False,
                                exclusive=True)

if response_queue.declare():
    print('Response queue declare')

if response_queue.bind('rpc_replies', queue_name):
    print('Response queue bound')

# Request block
with open('picture_1.jpg','rb') as img:
    pict = img.read()

    msg = rabbitpy.Message(channel,
                           pict,
                           {'content_type': 'image/jpeg',
                            'correlation_id': str(os.getpid()),
                            'headers':{'source': 'profile',
                                       'object': 'image',
                                       'action': 'new'},
                            'reply_to': str(queue_name)},
                           opinionated=True)
    msg.publish('headers_rpc_request')
    print('Msg published')

# Response block
# msg = None
# while not msg:
time.sleep(3)
msg = response_queue.get()
msg_1 = msg.body
with open('picture_3.jpg', 'wb') as new:
    new.write(msg_1)
duration = (time.time() - time.mktime(msg.properties['headers']['first_publish']))
print('Facial detection RPC call for image %s total duration: %s'
            %(msg.properties['correlation_id'], duration))
img_detect = cv2.imread('picture_3.jpg')
cv2.imshow(f'Detected Faces in ', img_detect)
# The window will close as soon as any key is pressed (not a mouse click)
cv2.waitKey(0)
cv2.destroyAllWindows()
msg.ack()
if os.path.isfile('picture_3.jpg'):
    os.remove('picture_3.jpg')
channel.close()
conn.close()
