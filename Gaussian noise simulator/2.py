import matplotlib.pyplot as plt
import cv2
import numpy as np

mean = 0
variance = 1


def make_random(main_img, width, height):
    # Generating noise
    gaussian_noise = np.random.normal(mean, variance, (height, width)).astype(np.uint8)

    # Making the noisy image
    noisy_image = cv2.add(main_img.astype(np.uint8), gaussian_noise)

    return noisy_image


# Initiate set for storing noisy images
noisy_images = []

# k is number of random images we want
k = 20

# Load the original image to get its dimensions
original_image = cv2.imread('2.jpg', cv2.IMREAD_GRAYSCALE)
rheight, rwidth = original_image.shape

# Make and save k noisy photos
for i in range(k):
    noisy_image = make_random(original_image, rwidth, rheight)

    # Save the noisy image on the device
    cv2.imwrite(f'pics2/gaussian_noisy_image_{i}.jpg', noisy_image)

    # Adding image to the set
    noisy_images.append(noisy_image)


required_k = [1, 5, 10, 15, 20]

for i in required_k:
    # Calculating means and showing them
    mean = np.mean(noisy_images[:i], axis=0).astype(np.uint8)
    cv2.imshow(f'Result for K means={i}', mean)

cv2.waitKey(0)
cv2.destroyAllWindows()


errors = []
# Calculate error, for each k from 1 to k
for z in range(1, k + 1):
    means = np.mean(noisy_images[:z], axis=0).astype(np.float32)
    error = np.mean((original_image - means) ** 2)
    print(f"{z} : {error}")
    # Add each error into
    errors.append(error)

# plot the chart
plt.plot(range(1, k + 1), errors)
plt.xlabel('Number of Noisy Images (K)')
plt.ylabel('Image Reconstruction Error')
plt.title('Image Reconstruction Error vs. K')
plt.grid()
plt.show()
