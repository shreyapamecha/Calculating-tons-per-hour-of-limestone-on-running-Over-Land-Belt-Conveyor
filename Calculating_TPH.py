import numpy as np
import cv2
from matplotlib import pyplot as plt
import sys
#from PIL import Image

filename = 'C:\\Users\\SHREYA\\Desktop\\shreya\\Internship\\Images\\a_9.jpeg'

im = cv2.imread(filename)
#print(im.dtype)
fig, (ax1) = plt.subplots(1)
ax1.imshow(im, cmap='gray')
plt.show()
#img = np.array(im, dtype=np.uint8)

#cv2.imshow(im)
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(im,127,255,0)
#fig, (ax1) = plt.subplots(1)
#ax1.imshow(thresh)
#plt.show()

#im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_FLOODFILL,cv2.CHAIN_APPROX_SIMPLE)
blurred_im = cv2.GaussianBlur(im, (5, 5), 0)
hsv = cv2.cvtColor(blurred_im, cv2.COLOR_BGR2HSV)

#fig, (ax1) = plt.subplots(1)
#ax1.imshow(hsv, cmap='gray')
#plt.show()

lower_blue = np.array([0, 0, 190])
upper_blue = np.array([40, 70, 255])

mask = cv2.inRange(hsv, lower_blue, upper_blue)
cnts, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#cnt = cnts[0]
#area = cv2.contourArea(cnt)
#area = 0
#print(cnts[0])

for contour in cnts:
    cv2.drawContours(im, contour, -1, (0, 255, 0), 2)
    #yo = contour[0]
    #print(yo)
    #area = area + yo
    #print(contour)

#print(area)
#fig, (ax1) = plt.subplots(1)
#ax1.imshow(im)
#plt.show()
#cv2.imshow("Frame", im)
cv2.imshow("Mask", mask)

kernel = np.ones((20,20),np.uint8)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

fig, (ax1) = plt.subplots(1)
ax1.imshow(closing, cmap = 'gray')
plt.show()
#key = cv2.waitKey(1)
#if key == 27:
    #break
        
#cap.release()


#cv2.destroyAllWindows()

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('C:\\Users\\SHREYA\\Desktop\\yeah.jpg', closing)
#im_2 = cv2.imread('C:\\Users\\SHREYA\\Desktop\\yeah.jpg')

#imgray_2 = cv2.cvtColor(im_2,cv2.COLOR_BGR2GRAY)
#ret_2,thresh_2 = cv2.threshold(im_2,127,255,0)

#cnts_2, _ = cv2.findContours(closing, cv2.RETR_FLOODFILL, cv2.CHAIN_APPROX_NONE)
#for contour in cnts_2:
#    cv2.drawContours(closing, contour, -1, (23, 143, 238), 3)

#cv2.imshow('yo', closing) 

#cv2.waitKey(0)
#cv2.destroyAllWindows()

im_BGR_2 = cv2.cvtColor(closing, cv2.COLOR_RGB2BGR)
imgray_2 = cv2.cvtColor(im_BGR_2, cv2.COLOR_BGR2GRAY)
ret_2,thresh_2 = cv2.threshold(imgray_2,127,255,0)

#im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_FLOODFILL,cv2.CHAIN_APPROX_SIMPLE)
blurred_im_2 = cv2.GaussianBlur(im_BGR_2, (5, 5), 0)
hsv_2 = cv2.cvtColor(blurred_im_2, cv2.COLOR_BGR2HSV)
#icc = closing.info.get('icc_profile', '')
#print(icc)

lower_white = np.array([0, 0, 240])
upper_white = np.array([10, 10 , 255])

mask_2 = cv2.inRange(hsv_2, lower_white, upper_white)
cnts_2, _ = cv2.findContours(mask_2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in cnts_2:
    cv2.drawContours(im_BGR_2, contour, -1, (0, 255, 0), 2)

cv2.imshow("Frame", im_BGR_2)
#cv2.imshow("Mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
#print(cnts)

if cnts_2!=[]:
    area = cv2.contourArea(cnts_2[0])
    print('Area:', area)
else:
    print('Area:', 0)
