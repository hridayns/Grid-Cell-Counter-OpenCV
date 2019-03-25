import os
import numpy as np
import cv2 as cv
import pandas as pd
from matplotlib import pyplot as plt


root = os.getcwd()
data_folder = 'input'
data_path = os.path.join(root,data_folder)

output_folder = 'output'
output_path = os.path.join(root,output_folder)
if not os.path.exists(output_path):
	os.makedirs(output_path)

def draw(img,fn):
	fig,ax = plt.subplots()
	ax.axis('off')
	ax.imshow(img,cmap='gray')
	fig.savefig(os.path.join(output_path,fn),bbox_inches='tight')
	plt.close()

def draw_hist(data,fn):
	fig,ax = plt.subplots()
	(n,bins,patches) = ax.hist(data)
	fig.savefig(os.path.join(output_path,'hist-'+fn),bbox_inches='tight')
	plt.close()
	print(n)
	print(bins)
	print(patches)

output_dict = {
	'File': [],
	'Number of Cells': []
}

for _,subfolders,files in os.walk(data_path):
	for file in files:
		print('{:-^50}'.format('FILE ' + file))
		img_file = os.path.join(data_path,file)
		if file in ['tiger.jpg','dice.jpg']:
			continue
		img = cv.imread(img_file)
		gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
		gray_data = gray_img.flatten()
		hist_data = np.histogram(gray_data)
		mx_freq_idx = np.argmax(hist_data[0])
		t = hist_data[1][mx_freq_idx] # Lower value of the range of bin (x-axis) with the highest frequency (y-axis)
		# print(hist_data[0].shape,hist_data[1].shape)
		# print(hist_data[0])
		# print(hist_data[1])
		# draw_hist(gray_data,file)
		# edges = cv.Canny(gray_img,100,200) # Canny edge mask instead of blur and threshold to binary image?

		blur_img = cv.GaussianBlur(gray_img, (5, 5), 0)
		# (t, binary_img) = cv.threshold(blur_img, 200, 255, cv.THRESH_BINARY)
		# (t, binary_img) = cv.threshold(blur_img, 240, 255, cv.THRESH_BINARY)
		# (t, binary_img) = cv.threshold(blur_img,240,255, cv.THRESH_BINARY_INV)
		(_, binary_img) = cv.threshold(blur_img,t,255, cv.THRESH_BINARY_INV)
		# binary_img = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
		(_, contours, _) = cv.findContours(binary_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

		num_cells = len(contours) - 1

		print('Number of cells: {}'.format(num_cells))
		output_dict['File'].append(file)
		output_dict['Number of Cells'].append(num_cells)

		# for (i, c) in enumerate(contours):
			# c_img = cv.drawContours(img, [c], 0, (0,255,0), 3)
			# draw(c_img,'contour-' + str(i) + '-' + file)
			# print('\tSize of contour {}: {}'.format(i, len(c)))

		contour_img = cv.drawContours(img, contours, -1, (0, 0, 255), 3)
		draw(contour_img,file)

print(output_dict)
df = pd.DataFrame(output_dict)
df.to_csv(os.path.join(output_path,'output.csv'),index=False)#index_label='ID')