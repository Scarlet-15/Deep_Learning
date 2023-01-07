import cv2
import numpy as np
image1= cv2.imread(r'crack2.jpg')
cv2.imshow('Original Image',image1)
image2 = cv2.cvtColor(image1, cv2.COLOR_RGB2GRAY)

clahe= cv2.createCLAHE(clipLimit=3)
contrast_img=clahe.apply(image2)
cv2.imshow('Image After fixing contrast',contrast_img)

image=cv2.GaussianBlur(contrast_img,(5,5),0)
cv2.imshow('B&W image',image)

ret,thresh=cv2.threshold(image,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
cv2.imshow('Image After thresholding',thresh)

kernel = np.ones((5,5),np.uint8)
opening = cv2.erode(thresh, kernel,iterations=1)
cv2.imshow('Image After morphing',opening)

contours,h=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img=image1.copy()

cv2.imshow('Image After drawing contours',img)
tot_area=0
for c in contours:
    if(cv2.contourArea(c)<50):
        continue
    cv2.drawContours(img,c,-1,(255,0,0),4)
#print(tot_area)
cv2.imshow('Image After drawing contours',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

