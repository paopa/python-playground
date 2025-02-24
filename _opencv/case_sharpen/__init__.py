import numpy as np
import skimage
import cv2

image = skimage.data.chelsea()

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# sharpen filter
sharpen_filter = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

sharpened_image = cv2.filter2D(image, -1, sharpen_filter)

cv2.imshow("Sharpened Image", sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
