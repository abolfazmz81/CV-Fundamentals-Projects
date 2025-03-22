# CV-Fundamentals-Projects

Welcome to the **CV-Fundamentals-Projects** repository! This collection showcases various projects developed as part of the Fundamental of computer vision university course, each focusing on different aspects of Computer Vision.

## Table of Contents

- [Project Overview](#project-overview)
- [Project Details](#project-details)
- [Installation and Usage](#installation-and-usage)
- [License](#license)

## Project Overview

This repository contains multiple projects that explore various Computer Viosion techniques and concepts. Each project is organized into its own directory with detailed documentation and source code.

## Project Details

### Project 1: Front-view extractor

**Description:**  
This project provides a program that can extract the front view of a place, even when the picture is taken from a semi-side angle rather than directly from the front.

**Features:**
- Allows the user to select four source and destination points on an image for perspective transformation.
- Computes the homography matrix and applies a perspective warp to generate a front view.
- Uses OpenCV to handle image processing, including mouse interactions for point selection.
- Supports dynamic user interaction to map semi-side angles to a frontal view.

**Directory:** [`./Front-view extractor`](./Front-view%20extractor)

### Project 2: Gaussian noise simulator

**Description:**  
This project provides a program that simulates **Gaussian noise** on an image, generating 20 images with a mean of 0 and a variance of 1. It then attempts to find a solution to the problem and determine the optimal value of **K**.

**Features:**
- Simulates Gaussian noise on a grayscale image, with a mean of 0 and a variance of 1.
- Generates 20 noisy images, each with different noise patterns.
- Calculates and displays the mean image for varying values of K (1, 5, 10, 15, and 20).
- Computes the reconstruction error for different values of K, measuring how well the noisy images approximate the original image.
- Plots a graph showing the relationship between the number of noisy images (K) and the reconstruction error.

**Directory:** [`./Gaussian noise simulator`](./Gaussian%20noise%20simulator)

### Project 3: Gear teeth extractor

**Description:**  
This project provides a program that extracts the teeth of a gear from an image using **structural elements**.

**Features:**
- Loads a grayscale image of a gear and converts it to a binary image using Otsu’s thresholding method.
- Creates structuring elements for the main gear body and teeth extraction:
  - A large elliptical kernel to represent the main gear body.
  - A smaller rectangular kernel to clean up the extracted teeth.
- Uses erosion to remove the gear body and dilation to restore the body’s size.
- Subtracts the dilated image from the original binary image to extract the teeth.
- Applies morphological opening to clean the extracted teeth.
- Displays the binary image and the extracted gear teeth side by side for visual comparison.

**Directory:** [`./Gear teeth extractor`](./Gear%20teeth%20extractor)

### Project 4: Hole finder

**Description:**  
This project provides a program that detects and extracts the holes and circles in a coin-like shape, printing their positions and radii based on the image.

**Features:**
- Reads a grayscale image and applies thresholding to obtain a binary representation of the image.
- Inverts the binary image and uses morphological operations (closing) to clean up noise.
- Uses distance transform to detect the centers of the holes (or circles) in the image.
- Identifies local maxima in the distance transform to find the centers of the holes.
- Calculates the radius of each hole using the distance transform value at the center.
- Filters the holes based on radius (between 10 and 50 pixels) and stores their center positions and radii.
- Displays the detected holes by drawing circles around their centers and radii on the original image.
- Prints the position and radius of each detected hole.

**Directory:** [`./Hole finder`](./Hole%20finder)

### Project 5: Image sharpener

**Description:**  
This project provides a program that sharpens and enhances the quality of an X-ray image, making objects and details more clear and distinguishable.

**Features:**
- Loads a grayscale X-ray image and performs a Fourier Transform to move into the frequency domain.
- Applies a Gaussian High-Pass Filter (HPF) to enhance the high-frequency components of the image, which helps sharpen details and edges.
- Displays the original image, the result of applying the Gaussian HPF, and the enhanced image after inverse Fourier transformation.
- Increases the quality of the X-ray image by making objects and details clearer and more distinguishable.

**Directory:** [`./Image sharpener`](./Image%20sharpener)

### Project 6: Logo embedder

**Description:**  
This project provides a program that embeds a binary logo into the bitplane of another image by replacing parts of the main image with the logo.

**Features:**
- Loads a grayscale main image and a binary logo image.
- Resizes the logo to match the dimensions of the main image.
- Converts the logo to a binary image (0 or 255) for embedding.
- Embeds the binary logo into the selected bit-plane of the main image.
- Extracts the logo from the embedded image by isolating the corresponding bit-plane.
- Saves and displays both the embedded images and extracted logos for each bit-plane (0 to 7).
- Computes and displays the Peak Signal-to-Noise Ratio (PSNR) for each embedded image to measure the quality of the embedding

**Directory:** [`./Logo embedder`](./Logo%20embedder)

### Project 7: Low contrast

**Description:**  
This project provides a program that implements the histogram equalization method to enhance low-contrast images, aiming to provide an optimal solution for improving image contrast.

**Features:**
- Histogram Equalization:
  - Loads a low-contrast grayscale image and computes its histogram.
  - Normalizes the histogram to ensure it sums to 1 and plots it.
  - Calculates the Cumulative Distribution Function (CDF) of the histogram and normalizes it to span the full range of pixel intensities [0, 255].
  - Applies the CDF to the original image, creating an equalized image with improved contrast.
  - Displays both the original and equalized images for comparison.
- Image Enhancement with Gaussian Filtering:
  - Applies Gaussian smoothing to the image using a Gaussian kernel, which helps to reduce noise and enhance image details.
  - Computes the result image r(x, y) by dividing the original image by the smoothed image (f(x, y) / g(x, y)), further enhancing contrast.
  - Displays the smoothed image and the final enhanced image for comparison.

**Directory:** [`./Low contrast`](./Low%20contrast)

## Installation and Usage

To run any of these projects locally:

1.**Clone the repository:**
   ```bash
   git clone https://github.com/abolfazmz81/CV-Fundamentals-Projects.git
   cd CV-Fundamentals-Projects
   ```

2.**Navigate to the project directory:**
  ```bash
  cd [ProjectDirectory]
  ```
Replace [ProjectDirectory] with the specific project folder.

3.**Install dependencies:** 
Ensure you have Python installed. Install the required packages using:
  ```bash
  pip install -r requirements.txt
  ```
Each project directory contains its own requirements.txt file with the necessary dependencies(except knn).

4.**Run the project:** 
Execute the main script for the project:
  ```bash
  python main.py
  ```
Sometimes it is not main.py, so be cautious. 

## License
This repository is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more information.


