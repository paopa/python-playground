import numpy as np
import skimage
import cv2

image = skimage.data.chelsea()

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 7x7 blur filter
dim = (7, 7)
blur_filter = np.ones(dim, dtype=np.float32) / np.prod(dim)

blurred_image = cv2.filter2D(image, -1, blur_filter)

cv2.imshow("Blurred Image", blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 21x21 blur filter
dim = (21, 21)
blur_filter = np.ones(dim, dtype=np.float32) / np.prod(dim)

blurred_image = cv2.filter2D(image, -1, blur_filter)

cv2.imshow("Blurred Image", blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
