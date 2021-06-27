import cv2
import os

# drag file for path and clean it
print("~~~ Emission Map Generator by blacknyx ~~~")
imgpath = input("\nDrag and drop your image file (albedo) here: ")
cleanpath = imgpath.strip('"')

# convert to grayscale
reqimg = cv2.imread(cleanpath)
gray = cv2.cvtColor(reqimg, cv2.COLOR_BGR2GRAY)

# convert to black and white
(thresh, bwimg) = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# cv2.imshow('Emission Map', bwimg)
# cv2.imshow('Albedo Map',reqimg)
# cv2.imshow('Gray image', gray)

# save file to chosen folder and end code
cv2.imwrite('emissionMap.png', bwimg)
print("\nEmission map generated and saved successfully!!")
input('Press Any Key To Exit...')

# cv2.waitKey(0)
# cv2.destroyAllWindows()