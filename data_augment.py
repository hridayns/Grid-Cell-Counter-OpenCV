
import os
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def rotateImage(img, angle):
	rows = img.shape[0]
	cols = img.shape[1]
	img_center = (cols / 2, rows / 2)
	rot_mat = cv.getRotationMatrix2D(img_center, angle, 1.0)
	result = cv.warpAffine(img, rot_mat,(cols,rows),borderValue=(255,255,255))
	return result

root = os.getcwd()
data_folder = 'input'
data_path = os.path.join(root,data_folder)

def draw(img,fn):
	fig,ax = plt.subplots()
	ax.axis('off')
	ax.imshow(img,cmap='gray')
	fig.savefig(os.path.join(data_path,fn),bbox_inches='tight')
	plt.close()

for _,subfolders,files in os.walk(data_path):
	for file in files:
		print('{:-^50}'.format('FILE ' + file))
		img_file = os.path.join(data_path,file)
		if file in ['tiger.jpg','dice.jpg']:
			continue
		img = cv.imread(img_file)

		# rotleft_5_img = rotateImage(img,5)
		print('10 degree left rotation...')
		rotleft_10_img = rotateImage(img,10)
		'''
		print('10 degree right rotation...')
		rotleft_10_img = rotateImage(img,10)

		print('5 degree left rotation...')
		rotleft_10_img = rotateImage(img,10)

		print('5 degree right rotation...')
		rotleft_10_img = rotateImage(img,10)
		'''
		# draw(rotleft_5_img,'rotLeft-5-'+file)
		draw(rotleft_10_img,'rotLeft-10-'+file)