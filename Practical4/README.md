
## 📁 Practical 4 – JPEG & Arithmetic Coding

This practical focuses on **lossy and entropy-based compression techniques** using:

* **JPEG Compression (DCT + Quantization + IDCT)**
* **Arithmetic Coding**

Both techniques are implemented in Python and demonstrate how images can be compressed (lossy) and how data can be efficiently represented using arithmetic coding (lossless).

---

### 📄 Files

| File                          | Description                                                                 |
| ----------------------------- | --------------------------------------------------------------------------- |
| `vignesh_img_compression_jpeg.py` | JPEG compression using **DCT, Quantization, and Inverse DCT** with visualization |
| `vignesh_ArithmeticCoding.py`     | Arithmetic Coding implementation with encoding/decoding example           |
| `Sample_Input_lena.jpg`           | Sample input image used for testing JPEG compression                      |
| `/Output Images/`                 | Folder containing **compressed/reconstructed images**                     |

---

### 🖼️ Output Images

Results generated during execution of the scripts:


| JPEG Compression Output                                   | Arithmetic Coding Output                                    |
|-----------------------------------------------------------|------------------------------------------------------------|
| ![JPEG](./Output%20Images/Output_JPEG.png)                | ![Arithmetic](./Output%20Images/Output_Arithmetic.png)     |

---

### 📚 Concepts Covered

* **JPEG Compression**
  - Discrete Cosine Transform (DCT)
  - Quantization using Standard Luminance Table
  - Inverse DCT for Reconstruction
  - Compression Ratio Estimation

* **Arithmetic Coding**
  - Interval-based Encoding
  - Probability Distribution Mapping
  - Decoding from Floating-Point Tag
  - Lossless Compression Efficiency

