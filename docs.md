# Algorithmic Approach
- Read image using OpenCV as **grayscale** (only 1 channel)
- Flatten the grayscale values and **generate histogram values** for ~30 bins (arbitrary).
- Find the index of the **most frequently occurring pixel intensity bin** and pick the **lower bound** of that bin as the **chosen threshold**.
- Perform a **Gaussian Blur operation** to smoothen the image.
- Perorm a **Binary Inverse Threshold operation** with the **chosen threshold** above.
- Using the **binary mask**, find the **contours** of the image to recursively find nested contours as well.
- Since the contours also includes the whole box inside which each cell resides, the total number of cells = **number of contours - 1**

# Possible Extensions
- Integration of OCR using **Google's Tesseract OCR engine**.
- Streamlining of intermediate **binary mask creation** using a more **robust algorithm** for determining optimal threshold value.
- Using **Canny Edge Detection** as the binary mask, instead of thresholding.
