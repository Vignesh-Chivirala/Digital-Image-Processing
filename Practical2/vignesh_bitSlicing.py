import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image in grayscale
img = cv2.imread('Input_Image_Grayscale.jpg', cv2.IMREAD_GRAYSCALE)

# List to store bit planes
bit_planes = []

# Extract each bit plane
for k in range(8):
    # Shift right by k and mask with 1
    bit_plane = np.bitwise_and(np.right_shift(img, k), 1) * 255
    bit_planes.append(bit_plane)

# Display original and bit planes
plt.figure(figsize=(10, 6))
plt.subplot(3, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

for k in range(8):
    plt.subplot(3, 3, k+2)
    plt.imshow(bit_planes[k], cmap='gray')
    plt.title(f'Bit Plane {k+1}')
    plt.axis('off')

plt.tight_layout()
plt.show()
