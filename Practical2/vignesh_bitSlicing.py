import cv2
import numpy as np
import matplotlib.pyplot as plt

def vignesh_bitSlicing(image_path):
    # Read image
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    # Convert to grayscale if RGB
    if len(img.shape) == 3:
        img = np.uint8(np.mean(img, axis=2))

    # Get dimensions
    rows, cols = img.shape

    # Initialize bit planes
    bit_planes = np.zeros((rows, cols, 8), dtype=np.uint8)

    # Traverse each pixel
    for i in range(rows):
        for j in range(cols):
            pixel_val = img[i, j]

            # Convert to 8-bit binary string
            binary_val = format(pixel_val, '08b')  # e.g., '00110111'

            # Extract bits (MSB first)
            for count in range(8):
                binary_bit_value = int(binary_val[count])
                bit_planes[i, j, count] = binary_bit_value

    # Display bit planes (MSB → LSB)
    plt.figure(figsize=(10, 6))
    for k in range(8):
        plt.subplot(2, 4, k+1)
        plt.imshow(bit_planes[:, :, k], cmap='gray')
        plt.title(f'Bit Plane {8-k}')  # Reverse numbering for MSB=8
        plt.axis('off')

    plt.tight_layout()
    plt.show()

vignesh_bitSlicing("Input_Image_Grayscale.jpg")
