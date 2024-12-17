import matplotlib.pyplot as plt
from PIL import Image

def show(name, n, m, i, Title):
    """
    Displays an image in a subplot grid.

    Parameters:
    - name: Image data to be displayed (2D or 3D array).
    - n: Number of rows in the subplot grid.
    - m: Number of columns in the subplot grid.
    - i: Index of the subplot (1-based indexing).
    - Title: Title for the image.
    """
    plt.subplot(n, m, i)
    plt.imshow(name, cmap='gray')  # Using grayscale colormap
    plt.title(Title)
    plt.axis('off')


# Load custom images
image_paths = ["C:\\Users\\ADMIN\\OneDrive\\download (2).jpeg"]  # Replace with your file paths
images = []

# Using PIL to load images
for path in image_paths:
    try:
        img = Image.open(path).convert("L")  # Convert to grayscale
        images.append(img)
    except FileNotFoundError:
        print(f"Error: File not found at {path}")

# Display images in a grid
plt.figure(figsize=(10, 8))
for idx, img in enumerate(images, start=1):
    show(img, 1, len(images), idx, f"Image {idx}")  # Adjust grid dimensions dynamically
plt.tight_layout()
plt.show()

