import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread('Input_Image_Grayscale.jpg', cv2.IMREAD_GRAYSCALE)

# Apply histogram equalization
equalized_img = cv2.equalizeHist(img)

# Display original and equalized histograms
plt.figure(figsize=(10,5))

# Original image
plt.subplot(2,2,1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Histogram of original image
plt.subplot(2,2,2)
plt.hist(img.ravel(), 256, [0,256])
plt.title('Original Histogram')

# Equalized image
plt.subplot(2,2,3)
plt.imshow(equalized_img, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

# Histogram of equalized image
plt.subplot(2,2,4)
plt.hist(equalized_img.ravel(), 256, [0,256])
plt.title('Equalized Histogram')

plt.tight_layout()
plt.show()
