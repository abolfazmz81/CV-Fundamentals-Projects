import cv2
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Read the image
f = cv2.imread('lowcontrast.png', cv2.IMREAD_GRAYSCALE)
plt.figure(figsize=(10, 6))
plt.imshow(f, cmap='gray')

# Define the kernel size and standard deviation (sigma) for the Gaussian filter
kernel_size = 401  # Kernel size must be odd (e.g., 3, 5, 7, etc.)
sigma = 1.0      # Standard deviation for Gaussian distribution

# Create the Gaussian kernel using OpenCV
kernel = cv2.getGaussianKernel(kernel_size, sigma)
gaussian_kernel = kernel @ kernel.T  # Create a 2D Gaussian kernel

# Print the kernel
print("Gaussian Kernel:")
print(gaussian_kernel)

# Apply Gaussian smoothing to the image
g = cv2.filter2D(f, -1, gaussian_kernel)

# Display the smoothed image
plt.figure(figsize=(10, 6))
plt.title("Smoothed Image (g(x, y))")
plt.imshow(g, cmap='gray')
plt.axis('off')
plt.show()

# Small constant to avoid division by zero
epsilon = 1e-5

# Compute r(x, y) = f(x, y) / (g(x, y) + epsilon)
r = np.divide(f, g + epsilon)

# Normalize the result to be in the range [0, 255]
r = np.clip(r, 0, 255)

# Display the result
plt.figure(figsize=(10, 6))
plt.title("Image r(x, y) = f(x, y) / (g(x, y) + epsilon)")
plt.imshow(r, cmap='gray')
plt.axis('off')
plt.show()
