import cv2
img = cv2.imread("me.jpg", cv2.IMREAD_GRAYSCALE)

filename = "me-copy.jpg"
v = cv2.imwrite(filename, img)
if v == True:
    print('Image saved successfully')
else:
    print('Image saved failed')
    