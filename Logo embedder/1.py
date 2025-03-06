import math

import cv2
import numpy as np
from matplotlib import pyplot as plt

### Section A ###
# Load the grayscale main image (8-bit resolution)
main_image = cv2.imread('2.jpg', cv2.IMREAD_GRAYSCALE)

# Load the logo image
logo_image = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)

# Resize the logo to fit the main image dimensions
logo_resized = cv2.resize(logo_image, (main_image.shape[1], main_image.shape[0]))

# Threshold the logo to make sure it's binary (0 or 255)
_, binary_logo = cv2.threshold(logo_resized, 170, 1, cv2.THRESH_BINARY)  # 170 is a treshold for degree of changing


# gray colors to black


def embed_logo(main_img, logo_img, bit_plane):
    # First, clear the target bit plane of the main image
    mask = 255 - (1 << bit_plane)  # Create a mask to zero out the selected bit-plane
    main_img_cleared = main_img & mask

    # Now shift the binary logo to the position of the selected bit-plane
    logo_shifted = logo_img << bit_plane

    # Combine the cleared image with the shifted logo to embed the binary logo
    embedded_image = main_img_cleared | logo_shifted

    return embedded_image


def extract_logo(embedded_img, bit_plane):
    # Extract the specific bit-plane where the logo was embedded
    extracted_logo = (embedded_img >> bit_plane) & 1  # Shift right and isolate bit-plane
    # Scale the extracted bits back to 0 and 255 to display
    extracted_logo_display = extracted_logo * 255
    return extracted_logo_display


embedded_images = []
# Embed the logo in all the bit planes
for bit_plane_to_embed in range(8):
    embedded_image = embed_logo(main_image, binary_logo, bit_plane_to_embed)

    # Save and display the embedded image
    cv2.imwrite(f'pics/embedded_image_{bit_plane_to_embed}.jpg', embedded_image)
    #cv2.imshow("embedded image", embedded_image)
    embedded_images.append(embedded_image)
    # Extract the logo from the embedded image
    extracted_logo = extract_logo(embedded_image, bit_plane_to_embed)

    # Save and display the extracted logo
    #cv2.imshow("Extracted Logo", extracted_logo)
    cv2.imwrite(f'pics/extracted_logo_{bit_plane_to_embed}.jpg', extracted_logo)
    cv2.waitKey(0)

cv2.destroyAllWindows()

### Section ###

PSNRs = []
for  i, image in enumerate(embedded_images):
    cv2.imshow(f"embedded {i}", image)
    cv2.waitKey(0)
    # Calculate PSNR
    PSNR = cv2.PSNR(main_image,image)
    print(f"{i} : {PSNR}")
    PSNRs.append(PSNR)

plt.plot(range(8), PSNRs)
plt.xlabel('Bit Plane embedded')
plt.ylabel('PSNR eroor value')
plt.title('PSNR values on Bit Plane')
plt.grid()
plt.show()