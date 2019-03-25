import os
import cv2 as cv
import numpy as np
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

for _,subfolders,files in os.walk(data_path):
	for file in files:
		print('------------------FILE {}--------------------'.format(file))
		img_file = os.path.join(data_path,file)
		if file == 'tiger.jpg':
			continue
		img = cv.imread(img_file)

		gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

		gray_y = gray_img.flatten()
		draw_hist(gray_y,file)

		blur_img = cv.GaussianBlur(gray_img, (5, 5), 0)

		# (t, binary_img) = cv.threshold(blur_img, 200, 255, cv.THRESH_BINARY)
		# (t, binary_img) = cv.threshold(blur_img, 240, 255, cv.THRESH_BINARY)
		(t, binary_img) = cv.threshold(blur_img,240,255, cv.THRESH_BINARY_INV)
		# binary_img = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)

		# draw(binary_img,file)

		(_, contours, _) = cv.findContours(binary_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

		print('Found {} objects.'.format(len(contours)))
		for (i, c) in enumerate(contours):

			print('\tSize of contour {}: {}'.format(i, len(c)))

		# contour_img = cv.drawContours(img, contours, -1, (0, 0, 255), 3)
		# draw(contour_img,file)
		# edges = cv.Canny(gray_img,100,200)