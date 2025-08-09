import cv2
import numpy as np
import matplotlib.pyplot as plt

def vignesh_HistEqualization(image_path):
    # Read the image
    I = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    # Convert to grayscale if it's a color image
    if len(I.shape) == 3:
        I = np.uint8(np.mean(I, axis=2))

    M, N = I.shape
    num_pixels = M * N

    # Flatten the image into a 1D array
    I_flat = I.flatten()

    # Initialize histogram array
    histogram = np.zeros(256, dtype=int)

    # Count frequency of each intensity value
    for pixel_val in I_flat:
        histogram[pixel_val] += 1

    # Compute the CDF
    cdf = np.cumsum(histogram)
    cdf_min = np.min(cdf[cdf > 0])  # Minimum non-zero CDF value

    # Apply Histogram Equalization formula
    equalized = np.round((cdf - cdf_min) / (num_pixels - cdf_min) * 255).astype(np.uint8)

    # Map old pixel values to new equalized values
    I_eq_flat = equalized[I_flat]

    # Reshape equalized flat image back to original shape
    I_eq = I_eq_flat.reshape(M, N)
    
    # Compute equalized histogram
    eq_hist = np.zeros(256, dtype=int)
    for pixel_val in I_eq_flat:
        eq_hist[pixel_val] += 1

    # Display results
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 2, 1)
    plt.imshow(I, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.bar(range(256), histogram, color='gray')
    plt.xlim(0, 255)
    plt.title('Histogram of Original Image')

    plt.subplot(2, 2, 3)
    plt.imshow(I_eq, cmap='gray')
    plt.title('Equalized Image')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.bar(range(256), eq_hist, color='gray')
    plt.xlim(0, 255)
    plt.title('Histogram of Equalized Image')

    plt.tight_layout()
    plt.show()

vignesh_HistEqualization("Input_Image_Grayscale.jpg")
