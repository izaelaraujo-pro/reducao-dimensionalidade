import numpy as np
import cv2

from google.colab import files
uploaded = files.upload()

import os
print(os.listdir('.'))

img = cv2.imread('exemplo.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

suave = cv2.GaussianBlur(img, (7,7), 0) # aplica blur
(T, bin) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY)
(T, binI) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY_INV)

resultado = np.vstack([
    np.hstack([suave, bin]),
    np.hstack([binI, cv2.bitwise_and(img, img, mask = binI)])
])

from google.colab.patches import cv2_imshow
cv2_imshow(resultado)
