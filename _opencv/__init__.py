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
