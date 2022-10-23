import rabbitpy
import cv2
import os
import time

conn = rabbitpy.Connection()
channel = conn.channel()

queue_name = 'rpc_worker %s' % os.getpid()
queue = rabbitpy.Queue(channel,
                       queue_name,
                       auto_delete=True,
                       durable=False,
                       exclusive=True)

if queue.declare():
    print('Worker queue declare')

if queue.bind('direct_rpc_request', 'detect_faces'):
    print('Worker queue bound')

for msg in queue.consume_messages():
    duration = time.time() - int(msg.properties['timestamp'].strftime('%S'))
    print('Received RPC request published %.2f seconds ago' % duration)
    with open('picture_2.jpg', 'wb') as new:
        new.write(msg.body)

    def draw_found_faces(detected, image, color: tuple):
        for (x, y, width, height) in detected:
            cv2.rectangle(
                image,
                (x, y),
                (x + width, y + height),
                color,
                thickness=2)

    path_to_image = 'picture_2.jpg'
    original_image = cv2.imread(path_to_image)

    if original_image is not None:
        # Convert image to grayscale
        image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

        # Create Cascade Classifiers
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        profile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_profileface.xml")

        # Detect faces using the classifiers
        detected_faces = face_cascade.detectMultiScale(image=image,
                                                       scaleFactor=1.3,
                                                       minNeighbors=5)
        detected_profiles = profile_cascade.detectMultiScale(image=image,
                                                             scaleFactor=1.3,
                                                             minNeighbors=5)

        # Filter out profiles
        profiles_not_faces = [x for x in detected_profiles if x not in detected_faces]

        # Draw rectangles around faces on the original, colored image
        draw_found_faces(detected_faces, original_image, (0, 255, 0))  # RGB - green
        draw_found_faces(detected_profiles, original_image, (0, 0, 255))  # RGB - red
        cv2.imwrite('picture_2.jpg', original_image)
        # # Open a window to display the results
        # cv2.imshow(f'Detected Faces in {path_to_image}', original_image)
        # # The window will close as soon as any key is pressed (not a mouse click)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
    else:
        print(f'En error occurred while trying to load {path_to_image}')

    properties = {'app_id': 'ARZ',
                  'content_type': msg.properties['content_type'],
                  'correlation_id': msg.properties['correlation_id'],
                  'headers': {
                      'first_publish': msg.properties['timestamp']},}
    with open(path_to_image, 'rb') as file:
        body = file.read()
    # if os.path.isfile('picture_2.jpg'):
    #     os.remove('picture_2.jpg')


    # os.unlink(temp_file)
    # os.unlink(faces)

    response = rabbitpy.Message(channel,
                                body,
                                properties)
    response.publish('rpc_replies', msg.properties['reply_to'])
    msg.ack
    print('Message send')
