import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def dct2(block):
    """Manual 2D DCT (Discrete Cosine Transform)."""
    N = block.shape[0]
    M = block.shape[1]
    dct_block = np.zeros((N, M))
    
    for u in range(N):
        for v in range(M):
            sum_val = 0
            for x in range(N):
                for y in range(M):
                    sum_val += block[x, y] * \
                               math.cos(((2*x+1)*u*math.pi)/(2*N)) * \
                               math.cos(((2*y+1)*v*math.pi)/(2*M))
            
            cu = 1 / math.sqrt(2) if u == 0 else 1
            cv = 1 / math.sqrt(2) if v == 0 else 1
            
            dct_block[u, v] = 0.25 * cu * cv * sum_val
    return dct_block


def idct2(dct_block):
    """Manual 2D Inverse DCT."""
    N = dct_block.shape[0]
    M = dct_block.shape[1]
    block = np.zeros((N, M))
    
    for x in range(N):
        for y in range(M):
            sum_val = 0
            for u in range(N):
                for v in range(M):
                    cu = 1 / math.sqrt(2) if u == 0 else 1
                    cv = 1 / math.sqrt(2) if v == 0 else 1
                    sum_val += cu * cv * dct_block[u, v] * \
                               math.cos(((2*x+1)*u*math.pi)/(2*N)) * \
                               math.cos(((2*y+1)*v*math.pi)/(2*M))
            
            block[x, y] = 0.25 * sum_val
    return block


def vignesh_img_compression_jpeg(imgg):
    # Load grayscale image
    img = Image.open(imgg).convert("L")
    originalImage = np.array(img)

    # Select 8x8 block
    originalBlock = originalImage[140:148, 60:68].astype(float)

    # Shift pixel values [-128, 127]
    shiftedBlock = originalBlock - 128

    # Step 2: Apply DCT
    dctBlock = dct2(shiftedBlock)

    # Step 3: Quantization
    quantizationTable = np.array([
        [16, 11, 10, 16, 24, 40, 51, 61],
        [12, 12, 14, 19, 26, 58, 60, 55],
        [14, 13, 16, 24, 40, 57, 69, 56],
        [14, 17, 22, 29, 51, 87, 80, 62],
        [18, 22, 37, 56, 68,109,103, 77],
        [24, 35, 55, 64, 81,104,113, 92],
        [49, 64, 78, 87,103,121,120,101],
        [72, 92, 95, 98,112,100,103, 99]
    ])

    quantizedBlock = np.round(dctBlock / quantizationTable)

    # Step 4: De-Quantization
    dequantizedBlock = quantizedBlock * quantizationTable

    # Step 5: Inverse DCT
    reconstructedShiftedBlock = idct2(dequantizedBlock)

    # Step 6: Rescale
    reconstructedBlock = np.round(reconstructedShiftedBlock + 128)
    reconstructedBlock = np.clip(reconstructedBlock, 0, 255).astype(np.uint8)

    # Embed into image
    compressedImage = originalImage.copy()
    compressedImage[140:148, 60:68] = reconstructedBlock

    # Size comparison
    originalSizeBits = originalBlock.size * 8
    nonZeroCoeffs = np.count_nonzero(quantizedBlock)
    estimatedCompressedBits = nonZeroCoeffs * 16
    if nonZeroCoeffs < 64:
        estimatedCompressedBits += 4
    compressionRatio = originalSizeBits / estimatedCompressedBits

    # --- Display results ---
    plt.figure(figsize=(12, 6))
    plt.suptitle("JPEG DCT Logic on an 8x8 Block")

    plt.subplot(2, 3, 1)
    plt.imshow(originalBlock.astype(np.uint8), cmap='gray')
    plt.title("Original Block")

    plt.subplot(2, 3, 4)
    plt.imshow(originalImage, cmap='gray')
    plt.title(f"Original Image\n{originalSizeBits/8:.2f} bytes")

    plt.subplot(2, 3, 2)
    plt.imshow(quantizedBlock, cmap='viridis')
    plt.colorbar()
    plt.title(f"Quantized DCT\n{nonZeroCoeffs} non-zero")

    plt.subplot(2, 3, 3)
    plt.imshow(reconstructedBlock, cmap='gray')
    plt.title("Reconstructed Block")

    plt.subplot(2, 3, 6)
    plt.imshow(compressedImage, cmap='gray')
    plt.title(f"Compressed Image\n{estimatedCompressedBits/8:.2f} bytes")

    plt.show()

    # Print info
    print("\n--- Size Comparison for the 8x8 Block ---")
    print(f"Original Size      : {originalBlock.size} pixels * 8 bits = {originalSizeBits} bits ({originalSizeBits/8} bytes)")
    print(f"Compressed Estimate: {nonZeroCoeffs} non-zero coeffs * ~16 bits = {estimatedCompressedBits} bits ({estimatedCompressedBits/8:.1f} bytes)")
    print(f"Compression Ratio  : {compressionRatio:.1f} : 1")


vignesh_img_compression_jpeg("SampleInput_lena.jpg")
