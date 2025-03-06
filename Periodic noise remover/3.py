import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')


def fourier_transform_analysis(image_path, title):
    # Load image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print(f"Error: Could not load image {image_path}")
        return

    # Compute the 2D Fourier Transform
    f_transform = np.fft.fft2(img)

    # Shift the zero frequency component to the center
    f_transform_shifted = np.fft.fftshift(f_transform)

    # Compute the magnitude and phase spectra
    magnitude_spectrum = np.abs(f_transform_shifted)
    phase_spectrum = np.angle(f_transform_shifted)

    # Log transformation for better visualization
    magnitude_spectrum_log = np.log(1 + magnitude_spectrum)

    # Display results
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 3, 1)
    plt.imshow(img, cmap='gray')
    plt.title(f'Original Image - {title}')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(magnitude_spectrum_log, cmap='gray')
    plt.title(f'Magnitude Spectrum - {title}')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(phase_spectrum, cmap='gray')
    plt.title(f'Phase Spectrum - {title}')
    plt.axis('off')

    plt.show()
    return magnitude_spectrum, phase_spectrum


def remove_periodic_noise(image_path):
    # Load image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Error: Could not load image")
        return

    # Compute the Fourier Transform
    f_transform = np.fft.fft2(img)
    f_transform_shifted = np.fft.fftshift(f_transform)

    # Visualize the Fourier spectrum
    magnitude_spectrum_log = np.log(1 + np.abs(f_transform_shifted))

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(magnitude_spectrum_log, cmap='gray')
    plt.title('Fourier Spectrum')
    plt.axis('off')
    plt.show()

    # Create a raw mask
    rows, cols = img.shape
    crow, ccol = rows // 2, cols // 2
    mask = np.ones((rows, cols))
    radius = 4

    # Add noise points
    mask[251, 251] = 0
    mask[261, 261] = 0
    mask[256, 240] = 0
    mask[256, 272] = 0

    # Extract phase and Magnitude
    magnitude_spectrum = np.abs(f_transform_shifted)
    phase_spectrum = np.angle(f_transform_shifted)

    # Apply mask
    filtered_magnitude = magnitude_spectrum * mask

    # Create and Inverse
    complex_spectrum = filtered_magnitude * np.exp(1j * phase_spectrum)
    complex_spectrum_shifted = np.fft.ifftshift(complex_spectrum)
    reconstructed_img = np.fft.ifft2(complex_spectrum_shifted).real

    # Plot the result
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 3, 1)
    plt.imshow(img, cmap='gray')
    plt.title('original image')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(np.log(1 + filtered_magnitude), cmap='gray')
    plt.title('filtered magnitude')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(reconstructed_img, cmap='gray')
    plt.title('filtered picture')
    plt.axis('off')
    plt.show()


image_A_path = "HW06 Fig 03.jpg"
fourier_transform_analysis(image_A_path, 'Picture A')
remove_periodic_noise(image_A_path)
