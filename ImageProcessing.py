#Computer vision is achieved in Python with the library OpenCV
#to install the library, pip install opencv-python
#what we can do with OpenCV:
#read the Image, write the image,

import cv2

# Loading the image into a varibale
img = cv2.imread("bolof.jpg",0)
resized_image = cv2.resize(img,(500,700))
cv2.imshow("bolof",resized_image)
cv2.imwrite("bolof_pythonimage.jpg",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
