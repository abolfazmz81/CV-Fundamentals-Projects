import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')

# Load the image
image_path = "gear.png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Convert to binary image using threshold
_, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Create structuring elements
# For the main gear body
size_large = min(binary.shape) // 6  # Adjust this ratio based on gear size
large_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (size_large, size_large))

# For cleaning up the teeth
small_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# Erosion to remove the teeth
eroded = cv2.erode(binary, large_kernel, iterations=1)

# Dilation to restore the main body size
dilated = cv2.dilate(eroded, large_kernel, iterations=1)

# Subtract the gear body from original to get teeth
teeth = cv2.subtract(binary, dilated)

# Clean up the teeth using opening
teeth = cv2.morphologyEx(teeth, cv2.MORPH_OPEN, small_kernel)


# Display the results
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(binary, cmap='gray')
plt.title("Binary Image")


plt.subplot(1, 2, 2)
plt.imshow(teeth, cmap='gray')
plt.title("Extracted Teeth")
plt.show()
