import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')

image_path = "image_2023_12_20T05_20_18_580Z.png"
# Load image in grayscale
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if img is None:
    print("Error: Could not load image")
else:
    # getting the images shape
    rows, cols = img.shape
    crow, ccol = rows // 2, cols // 2  # Center coordinates

    # Compute the 2D Fourier Transform
    f_transform = np.fft.fft2(img)
    f_transform_shifted = np.fft.fftshift(f_transform)

    # Create Gaussian High-Pass Filter
    x = np.linspace(-ccol, ccol, cols)
    y = np.linspace(-crow, crow, rows)
    X, Y = np.meshgrid(x, y)
    radius = np.sqrt(X ** 2 + Y ** 2)
    sigma = 10  # Adjust for different levels of filtering
    gaussian_hpf = 1 - np.exp(-(radius ** 2) / (2 * sigma ** 2))

    # Apply filter
    filtered_spectrum = f_transform_shifted * gaussian_hpf
    filtered_spectrum_changed = filtered_spectrum + f_transform_shifted

    # Inverse Fourier Transform of high-pass result
    filtered_spectrum_reshifted = np.fft.ifftshift(filtered_spectrum)
    highpass_result = np.fft.ifft2(filtered_spectrum_reshifted).real

    # Inverse Fourier Transform
    filtered_spectrum_shifted = np.fft.ifftshift(filtered_spectrum_changed)
    enhanced_img = np.fft.ifft2(filtered_spectrum_shifted).real

    # Display results
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 3, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(highpass_result, cmap='gray')
    plt.title('Gaussian Result')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(enhanced_img, cmap='gray')
    plt.title('Enhanced Image (Gaussian HPF)')
    plt.axis('off')

    plt.show()
