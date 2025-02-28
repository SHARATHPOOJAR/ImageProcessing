import cv2

# Read the image
image = cv2.imread('image.jpg')

# Resize the image
resized_image = cv2.resize(image, (400, 400))

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Show the images
cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resized_image)
cv2.imshow('Grayscale Image', gray_image)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
