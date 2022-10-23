import cv2
import base64
import numpy as np

# img = cv2.imread('picture_1.jpg')
with open('picture_1.jpg','rb') as img:
    p = img.read()
    # img_base64 = base64.b64encode(img)
    # msg_decode = base64.b64decode(img_base64)
with open('picture_2.jpg','wb') as new:
    new.write(p)
# m = np.array(msg_decode)
# img_w = cv2.imwrite('picture_2.jpg', m)
img_1 = cv2.imread('picture_2.jpg')

cv2.namedWindow('wind1',cv2.WINDOW_AUTOSIZE)
cv2.imshow('wind1', img_1)
cv2.waitKey(0)
cv2.destroyAllWindows()