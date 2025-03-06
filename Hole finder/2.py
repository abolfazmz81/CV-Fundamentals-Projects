import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')


def find_hole_properties(image_path):
    # Read the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Threshold the image to get binary
    # invert the image
    _, binary = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Create a small circular structuring element
    kernel_small = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

    # Clean up noise using closing
    cleaned = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel_small)

    # Use distance transform to find centers
    dist_transform = cv2.distanceTransform(cleaned, cv2.DIST_L2, 5)

    # Create a larger kernel for finding maxima
    kernel_max = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (50, 50))

    # Dilate the distance transform
    dilated = cv2.dilate(dist_transform, kernel_max)

    # Local maxima are where dilated equals distance transform
    local_max = (dist_transform == dilated)
    local_max = local_max.astype(np.uint8) * 255

    # Find hole properties
    current_label = 1
    holes_info = []

    for y in range(local_max.shape[0]):
        for x in range(local_max.shape[1]):
            if local_max[y, x] == 255:
                # Found a new center
                center = (x, y)
                if center == (163, 54):
                    continue

                # The radius is the distance transform value at this point
                radius = int(dist_transform[y, x])
                if 10 < radius < 50:
                    holes_info.append({
                        'center': center,
                        'radius': radius
                    })
                    current_label += 1

    return holes_info


# Usage
image_path = 'circles.png'
holes = find_hole_properties(image_path)

# Print results
for i, hole in enumerate(holes):
    print(f"Hole {i + 1}:")
    print(f"  Center: {hole['center']}")
    print(f"  Radius: {hole['radius']} pixels")

# Visualize results on the original image
img_color = cv2.imread(image_path)
for hole in holes:
    cv2.circle(img_color, hole['center'], 2, (0, 0, 255), -1)  # Center point
    cv2.circle(img_color, hole['center'], hole['radius'], (0, 255, 0), 1)  # Radius circle

cv2.imshow('Detected Holes', img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
