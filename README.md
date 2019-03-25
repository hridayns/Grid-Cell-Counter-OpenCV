# Introduction
This project **counts grid cells** from spreadsheet-like images, even with slight variations in angles (~5 to 10 degrees). Will be extended to perform **OCR** on extracted text. 

# Prerequisites and Installation
- [**Python 3.6.3 or higher**](https://www.python.org/downloads/)
- **numPy 1.16.0 or higher**: `pip install numpy`
- **OpenCV 3.4.0 or higher**: `pip install opencv-python`
- **pandas 0.20.3 or higher**: `pip install pandas`
- **matplotlib 2.1.0 or higher**: `pip install matplotlib`

# Usage

Run the main file `python soln.py` from the project directory. Make sure to rename/delete the existing **output** folder if you want to obtain your own results. Any image added to the **input** directory will automatically be considered for processing.

Apart from the results being printed out, the generated **output.csv** file holds the results of the number of grid cells for each image in the **input** folder. The **output** folder also holds images of contours drawn over the original image along with histograms to fine-tune threshold values used in creation of intermediate binary image.