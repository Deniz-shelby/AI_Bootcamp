import cv2
import numpy as np
import matplotlib.pyplot as plt

def imshow(img):
    plt.figure(figsize = (10,7))
    plt.imshow(img)
    plt.show()

img = cv2.imread('img/blue-red-flowers.png')
rgb_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
imshow(rgb_img)

h, w = rgb_img.shape[:2]

lower_range = (90,20,0)
upper_range = (140,255,255)

mask = cv2.inRange(hsv_img, lower_range, upper_range)
masked = rgb_img.copy()
masked[mask==0] = [0,0,0]

img_and = cv2.bitwise_and(masked,rgb_img) #order dont change
plt.imshow(img_and, cmap='gray')

background_image = cv2.imread('img/underwater.jpg')
background_image = cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB)

crop_background = background_image[0:h, 0:w]

crop_background[mask != 0] = [0, 0, 0]

final_image = crop_background + img_and
import cv2
import numpy as np
import matplotlib.pyplot as plt
def imshow(img):
    plt.figure(figsize = (10,7))
    plt.imshow(img)
    plt.show()

img = cv2.imread('img/blue-red-flowers.png')
rgb_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
imshow(rgb_img)

h, w = rgb_img.shape[:2]

lower_range = (90,20,0)
upper_range = (140,255,255)

mask = cv2.inRange(hsv_img, lower_range, upper_range)
masked = rgb_img.copy()
masked[mask==0] = [0,0,0]

img_and = cv2.bitwise_and(masked,rgb_img) #order dont change
plt.imshow(img_and, cmap='gray')

background_image = cv2.imread('img/underwater.jpg')
background_image = cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB)

crop_background = background_image[0:h, 0:w]

crop_background[mask != 0] = [0, 0, 0]

final_image = crop_background + img_and
imshow(final_image)