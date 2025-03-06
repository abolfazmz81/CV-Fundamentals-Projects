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


def reconstruct_image(magnitude, phase):
    # Combine magnitude and phase to form complex spectrum
    complex_spectrum = magnitude * np.exp(1j * phase)

    # Shift back the zero frequency component
    complex_spectrum_shifted = np.fft.ifftshift(complex_spectrum)

    # Compute the inverse Fourier Transform
    reconstructed_img = np.fft.ifft2(complex_spectrum_shifted).real

    return reconstructed_img


# Example usage:
image_A_path = 'wallpaperflare.com_wallpaper.jpg'
image_B_path = 'wallpaperflare.com_wallpaper (25).jpg'

magnitude_A, phase_A = fourier_transform_analysis(image_A_path, 'Picture A')
magnitude_B, phase_B = fourier_transform_analysis(image_B_path, 'Picture B')

# Swap phases
reconstructed_A = reconstruct_image(magnitude_A, phase_B)
reconstructed_B = reconstruct_image(magnitude_B, phase_A)

# Display results
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(reconstructed_A, cmap='gray')
plt.title('Reconstructed Image A (with B Phase)')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(reconstructed_B, cmap='gray')
plt.title('Reconstructed Image B (with A Phase)')
plt.axis('off')

plt.show()
