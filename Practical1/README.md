# 🧪 Digital Image Processing – Practical 1

This folder contains MATLAB scripts and sample data for **Practical 1** of the Digital Image Processing Laboratory, part of the academic curriculum at IIIT Nagpur.

---

## 📌 Practical Overview

**Objective:**  
To perform basic image processing operations on an RGB image, including:

- Conversion to Grayscale
- Extraction of RGB color planes
- Conversion to Black and White (Binary)

---

## 📂 Contents

| File Name               | Description                               |
|-------------------------|-------------------------------------------|
| `Avengers.jpg`          | Input RGB image used for processing       |
| `Vignesh_RGBtoGray.m`   | Converts the RGB image to grayscale       |
| `Vignesh_RGBPlanes.m`   | Extracts and displays R, G, B color planes|
| `Vignesh_RGBtoBW.m`     | Converts the RGB image to black & white   |
| `Output Images/`        | Folder containing resulting image outputs |


---

## 🖼 Image Comparison

| Original Image           | Grayscale Image           |
|--------------------------|---------------------------|
| ![Original](./Avengers.jpg) | ![Grayscale](./Output%20Images/GrayScale_Image.jpg) |

| RGB Planes               | Black & White Image       |
|--------------------------|---------------------------|
| ![RGB Planes](./Output%20Images/RGBPlanes_Image.jpg) | ![B&W](./Output%20Images/Black%26White_Image.jpg) |



---

## 🚀 How to Run

1. Open MATLAB.
2. Navigate to this folder (`Practical-1`).
3. Run the scripts one by one:
   ```matlab
   run('Vignesh_RGBtoGray.m');
   run('Vignesh_RGBPlanes.m');
   run('Vignesh_RGBtoBW.m');
