import cv2
import numpy as np

img = cv2.imread("R.png",cv2.IMREAD_GRAYSCALE)
img_A = cv2.imread("kaneki.jpg",cv2.IMREAD_GRAYSCALE) # hello everybody in this video we ll see how turn our imgs into black and white images like in 99s  lets see


cv2.imshow("Kaneki Ken",img)
cv2.imshow("Kaneki Ken",img_A)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("kanekiInGray.png",img)
cv2.imwrite("kanekiInGray_A.png",img_A) #that s all for now 