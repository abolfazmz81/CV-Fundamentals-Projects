import scipy.io
import numpy as np

# File paths for the .mat files
features_2d_path = 'Features2D.mat'  # Replace with your actual file path
features_3d_path = 'Features3D.mat'  # Replace with your actual file path

# Load the .mat files
features_2d_raw = scipy.io.loadmat(features_2d_path)
features_3d_raw = scipy.io.loadmat(features_3d_path)

# Extract the data using the correct keys
features_2d = features_2d_raw['f']  # 2D feature points
features_3d = features_3d_raw['P']  # 3D feature points

# Load your 2D and 3D points
image_points = features_2d  # 2D points (u, v) on the image
scene_points = features_3d[:, :3]  # 3D points (X, Y, Z)


# Normalize 2D and 3D points
def normalize_points(points):
    mean = np.mean(points, axis=0)
    std = np.std(points, axis=0)
    normalized_points = (points - mean) / std
    return normalized_points, mean, std


# Normalize both sets of points
image_points_normalized, image_mean, image_std = normalize_points(image_points)
scene_points_normalized, scene_mean, scene_std = normalize_points(scene_points)

# Construct the matrix for the projection equation
num_points = image_points.shape[0]
A = []

for i in range(num_points):
    X, Y, Z = scene_points_normalized[i]
    u, v = image_points_normalized[i]

    # Add equations for x and y (u and v)
    A.append([X, Y, Z, 1, 0, 0, 0, 0, -u * X, -u * Y, -u * Z, -u])
    A.append([0, 0, 0, 0, X, Y, Z, 1, -v * X, -v * Y, -v * Z, -v])

# Convert to NumPy array
A = np.array(A)

# Perform SVD to find the camera parameters
U, S, Vt = np.linalg.svd(A)
camera_params = Vt[-1]  # Last row corresponds to the solution

# Reshape into 3x4 camera matrix
camera_matrix = camera_params.reshape(3, 4)

# Intrinsic matrix extraction: Using QR decomposition
M = camera_matrix[:, :3]  # Extract the first 3x3 part of the camera matrix
K, R = np.linalg.qr(np.linalg.inv(M))  # QR decomposition

# Ensure positive diagonal elements in K
if K[0, 0] < 0:
    K[:, 0] *= -1
if K[1, 1] < 0:
    K[:, 1] *= -1

# Normalize K to ensure positive scaling
K = K / K[2, 2]

# Extract and denormalize focal lengths
focal_length_x = K[0, 0] * image_std[0]
focal_length_y = K[1, 1] * image_std[1]

# Output the focal lengths
print("Focal Length (fx):", focal_length_x)
print("Focal Length (fy):", focal_length_y)

# Map the 3D points using the camera matrix
mapped_points = []
for point in features_3d:
    X, Y, Z, _ = point  # Extract the 3D point
    mapped_point = camera_matrix @ np.array([X, Y, Z, 1])  # Apply camera matrix
    u_mapped = mapped_point[0] / mapped_point[2]  # Normalize by w
    v_mapped = mapped_point[1] / mapped_point[2]
    mapped_points.append([u_mapped, v_mapped])

# Convert to NumPy array
mapped_points = np.array(mapped_points)

# Calculate the accuracy of the camera model
# Compute pixel-wise Euclidean distance
errors = np.linalg.norm(features_2d - mapped_points, axis=1)  # Pixel-wise error

# Compute error metrics
mse = np.mean(errors**2)  # Mean Squared Error
rmse = np.sqrt(mse)  # Root Mean Squared Error

# Output the results
print("Mapped Points (First 5):", mapped_points[:5])
print("Errors (First 5):", errors[:5])
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)
