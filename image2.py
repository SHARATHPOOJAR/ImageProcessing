import cv2
import numpy as np

image = cv2.imread('input.jpg')
cv2.imshow('Original Image', image)

resized = cv2.resize(image, (400, 300))
cv2.imshow('Resized', resized)

scaled = cv2.resize(image, None, fx=0.5, fy=0.5)
cv2.imshow('Scaled', scaled)

(h, w) = image.shape[:2]
center = (w // 2, h // 2)
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, matrix, (w, h))
cv2.imshow('Rotated', rotated)

contrast = cv2.convertScaleAbs(image, alpha=1.5, beta=0)
cv2.imshow('High Contrast', contrast)

bright = cv2.convertScaleAbs(image, alpha=1.0, beta=50)
cv2.imshow('Brighter Image', bright)

blurred = cv2.GaussianBlur(image, (15, 15), 0)
cv2.imshow('Gaussian Blur', blurred)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', gray)

edges = cv2.Canny(image, 100, 200)
cv2.imshow('Edges', edges)

flipped = cv2.flip(image, 1)
cv2.imshow('Flipped', flipped)

cropped = image[100:400, 200:500]
cv2.imshow('Cropped', cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()
