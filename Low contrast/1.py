import cv2
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Read the input image in grayscale
image = cv2.imread('lowcontrast.png', cv2.IMREAD_GRAYSCALE)
#plt.imshow(image,cmap="gray")

# Calculate the histogram of the grayscale image
histogram = cv2.calcHist([image], [0], None, [256], [0, 255])

# Normalize the histogram so it sums to 1
histogram = histogram / histogram.sum()
#print(histogram.sum())

# Plot the histogram
plt.figure(figsize=(10, 6))
plt.title("Original Image Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.plot(histogram)
plt.xlim([0, 255])
plt.show()

# Compute the cumulative distribution function (CDF)
cdf = histogram.cumsum()

# Normalize the CDF to make sure it spans the full range [0, 255]
cdf_normalized = cdf * 255 / cdf[-1]

# Plot the CDF
plt.figure(figsize=(10, 6))
plt.title("Cumulative Distribution Function (CDF)")
plt.xlabel("Pixel Intensity")
plt.ylabel("Cumulative Frequency")
plt.plot(cdf_normalized)
plt.xlim([0, 256])
plt.show()

# Create an empty array for the equalized image
equalized_image = np.zeros_like(image)

# Map each pixel value in the original image to the new value using the CDF
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        equalized_image[i, j] = cdf_normalized[image[i, j]]


# Display the original and equalized images side by side
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Equalized Image")
plt.imshow(equalized_image, cmap='gray')
plt.axis('off')
plt.show()

