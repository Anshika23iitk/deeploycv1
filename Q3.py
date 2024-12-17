import cv2
import numpy as np
import requests
from io import BytesIO
import matplotlib.pyplot as plt


# Function to load an image from a URL
def load_image_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if request was successful
        image = np.asarray(bytearray(response.content), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        if image is None:
            print(f"Failed to load image from URL: {url}")
        return image
    except Exception as e:
        print(f"Error loading image: {e}")
        return None


# Function to apply High-pass filter
def high_pass_filter(image):
    # Use Laplacian kernel for high-pass filter
    kernel = np.array([[0, -1, 0],
                       [-1, 4, -1],
                       [0, -1, 0]])
    return cv2.filter2D(image, -1, kernel)


# Function to apply Low-pass filter
def low_pass_filter(image):
    # Use Gaussian blur for low-pass filter
    return cv2.GaussianBlur(image, (11, 11), 0)


# Load two images from URLs
url1 = 'https://i.pinimg.com/736x/1f/e7/e5/1fe7e58662e627bb8f974abf8e5265bc.jpg'
url2 = 'https://static.vecteezy.com/system/resources/previews/029/214/620/non_2x/hand-holding-colorful-arrangements-flowers-bright-and-sunny-day-with-simple-aesthetic-romantic-vibes-perfect-for-wedding-greeting-card-flower-card-and-more-photo.jpg'

image1 = load_image_from_url(url1)
image2 = load_image_from_url(url2)

# Check if images are loaded properly
if image1 is None or image2 is None:
    print("Error: Could not load one or both images. Please check the URLs.")
else:
    # Convert images to grayscale for filtering
    image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Resize images to the same dimensions
    height, width = min(image1_gray.shape[0], image2_gray.shape[0]), min(image1_gray.shape[1], image2_gray.shape[1])
    image1_gray = cv2.resize(image1_gray, (width, height))
    image2_gray = cv2.resize(image2_gray, (width, height))

    # Apply filters
    image1_high = high_pass_filter(image1_gray)
    image2_low = low_pass_filter(image2_gray)

    # Combine images
    combined_image = cv2.addWeighted(image1_high, 0.5, image2_low, 0.5, 0)

    # Plot all images
    fig, axes = plt.subplots(1, 5, figsize=(20, 10))
    axes[0].imshow(image1_gray, cmap='gray')
    axes[0].set_title("Original Image 1")

    axes[1].imshow(image2_gray, cmap='gray')
    axes[1].set_title("Original Image 2")

    axes[2].imshow(image1_high, cmap='gray')
    axes[2].set_title("High-Pass Filtered Image")

    axes[3].imshow(image2_low, cmap='gray')
    axes[3].set_title("Low-Pass Filtered Image")

    axes[4].imshow(combined_image, cmap='gray')
    axes[4].set_title("Combined Image")

    # Hide axes
    for ax in axes:
        ax.axis('off')

    plt.tight_layout()
    plt.show()
