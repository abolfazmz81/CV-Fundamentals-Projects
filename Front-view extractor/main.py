import cv2
import numpy as np
from matplotlib import pyplot as plt

points = []
dst_points = []


def select_point(event, x, y,flags , param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Left mouse button click
        if param == "src":
            points.append((x, y))
            cv2.circle(img, (x, y), 2, (0, 0, 255), -1)
            cv2.imshow("Select Points", img)

            # If we're selecting destination points (on blank canvas)
        elif param == "dst":
            dst_points.append((x, y))
            cv2.circle(blank_canvas, (x, y), 5, (255, 0, 0), -1)
            cv2.imshow("Select Destination Points", blank_canvas)


# Load the image
image_path = '1731009460995.JPEG'
img = cv2.imread(image_path)

# Create a window and set the mouse callback
cv2.imshow("Select Points", img)
cv2.setMouseCallback("Select Points", select_point , "src")

print("Please click on four corners in the order: top-left, top-right, bottom-left, bottom-right.")

# Wait until four points are selected
while len(points) < 4:
    cv2.waitKey(1)

# Close the image window
cv2.destroyAllWindows()

# Once we have the four points, we can use them for homography
src_points = np.array(points, dtype="float32")

# Create a blank canvas for destination points (size can be adjusted as needed)
canvas_width, canvas_height = img.shape[1], img.shape[0]  # Define desired size for destination canvas
blank_canvas = np.ones((canvas_height, canvas_width, 3), dtype=np.uint8) * 255

# Select destination points on the blank canvas
cv2.namedWindow("Select Destination Points", cv2.WINDOW_NORMAL)
cv2.imshow("Select Destination Points", blank_canvas)
cv2.setMouseCallback("Select Destination Points", select_point, "dst")

print("Please click on four destination points on the blank canvas.")
while len(dst_points) < 4:
    cv2.waitKey(1)  # Wait until four points are selected

cv2.destroyAllWindows()

# Convert to Numpy array
dst_points = np.array(dst_points, dtype="float32")

# Compute the homography matrix
homography_matrix, status = cv2.findHomography(src_points, dst_points)

# Apply the perspective transformation
front_view = cv2.warpPerspective(img, homography_matrix, (canvas_width, canvas_height))

# Display the transformed image
cv2.namedWindow("Front", cv2.WINDOW_FREERATIO)
cv2.imshow("Front", front_view)
cv2.waitKey(0)
cv2.destroyAllWindows()