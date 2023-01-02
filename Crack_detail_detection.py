import cv2
image1= cv2.imread(r'crack4.jpg')
cv2.imshow('Original Image',image1)
image2 = cv2.cvtColor(image1, cv2.COLOR_RGB2GRAY)
image=cv2.GaussianBlur(image2,(5,5),0)
cv2.imshow('B&W image',image)
ret,thresh=cv2.threshold(image,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
cv2.imshow('Image After thresholding',thresh)
contours,h=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
'''img=image1.copy()
cv2.drawContours(img,contours,-1,(255,0,0),-1)
cv2.imshow('Crack',img)'''
tot_area=0
for c in contours:
    tot_area+=cv2.contourArea(c)
print(tot_area)

cv2.waitKey(0)
cv2.destroyAllWindows()
