import cv2
import numpy as np
import matplotlib.pyplot as plt

# Open the camera
cap = cv2.VideoCapture(0)  # Change to 1 or another number if needed

# Read a frame from the camera
ret, frame = cap.read()
cap.release()

# Function for grayscale conversion
def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Function for thresholding (binary image)
def thresholding(image, thresh_value=127):
    gray = grayscale(image)
    _, thresh = cv2.threshold(gray, thresh_value, 255, cv2.THRESH_BINARY)
    return thresh

# Function for creating 16-level gray image
def sixteen_gray_levels(image):
    gray = grayscale(image)
    return (gray // 16) * 16

# Function for Sobel filter
def sobel_filter(image):
    gray = grayscale(image)
    grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    return cv2.magnitude(grad_x, grad_y)

# Function for Canny edge detector
def canny_edge_detector(image):
    gray = grayscale(image)
    return cv2.Canny(gray, 100, 200)

# Function to apply Gaussian blur
def gaussian_blur(image):
    return cv2.GaussianBlur(image, (5, 5), 0)

# Function to sharpen the image
def sharpen_image(image):
    kernel = np.array([[0, -1, 0],
                       [-1, 5,-1],
                       [0, -1, 0]])
    return cv2.filter2D(image, -1, kernel)

# Function to convert RGB to BGR
def rgb_to_bgr(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

# Plotting the images in a 2x4 grid
fig, axes = plt.subplots(2, 4, figsize=(15, 8))

# Displaying the images
images = [
    grayscale(frame),  # Grey scaling
    thresholding(frame),  # Thresholding
    sixteen_gray_levels(frame),  # 16 gray levels
    sobel_filter(frame),  # Sobel filter
    canny_edge_detector(frame),  # Canny edge detector
    gaussian_blur(frame),  # Gaussian blur
    sharpen_image(gaussian_blur(frame)),  # Sharpened image
    rgb_to_bgr(frame)  # RGB to BGR
]

titles = [
    "Grayscale",
    "Thresholding",
    "16 Gray Levels",
    "Sobel Filter",
    "Canny Edge Detector",
    "Gaussian Blur",
    "Sharpened Image",
    "RGB to BGR"
]

# Display each image in the grid
for i, ax in enumerate(axes.flat):
    ax.imshow(images[i], cmap='gray' if i < 7 else None)
    ax.set_title(titles[i])
    ax.axis('off')

plt.tight_layout()
plt.show()
