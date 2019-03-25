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

for _,subfolders,files in os.walk(data_path):
	for file in files:
		print('------------------FILE {}--------------------'.format(file))
		img_file = os.path.join(data_path,file)
		img = cv.imread(img_file)
		gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
		edges = cv.Canny(gray_img,100,200)

		op_plt,ax_op = plt.subplots()
		ax_op.imshow(edges,cmap='gray')
		op_plt.savefig(os.path.join(output_path,file),bbox_inches='tight')
		plt.close()

		(_, contours,_) = cv.findContours(edges,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
		
		img_w_contours = cv.drawContours(img, contours[0], -1, (0, 0, 255), 5)

		contour_plt,ax_con = plt.subplots()
		ax_con.imshow(img_w_contours)
		contour_plt.savefig(os.path.join(output_path,'contours-'+file),bbox_inches='tight')
		plt.close()

		print('Found {} objects.'.format(len(contours)))
		for (i, c) in enumerate(contours):
			print('\tSize of contour {}: {}'.format(i, len(c)))