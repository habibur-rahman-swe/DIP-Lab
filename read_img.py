import cv2

image = cv2.imread('me.jpg', cv2.IMREAD_GRAYSCALE)

# Check image type
print(type(image))  # Should print <class 'numpy.ndarray'>

# Display the image
cv2.imshow('image', image)
cv2.waitKey(0)  # Wait for a key press
cv2.destroyAllWindows()  # Close all windows
