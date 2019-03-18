"""
This program searches a folder of images to find one that is most visually similar to
a specific image that is passed in.
It takes two arguments to run properly: folder and image
e.g. python3 match.py folder=emoticons image=boom.png
Note that arguments MUST be passed in using 'folder' and 'image' as the key AND there must NOT
be a space on either side of the '='
"""

import sys
from skimage.transform import resize
from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os

"""
Calculates the Mean Squared Error between two images. This is a method
to determine how visually similar two images are. An MSE of 0 means the
images are perfectly similar. While an MSE of greater than 1 means that
the images are more different as MSE increases.
"""
def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err
 
"""
Compares two images using both their Mean Squared Error and Structural 
Similarity Measure (ssim). Ssim uses a different equation to "attempt 
to model the perceived change in the structural information 
of the image, whereas MSE is actually estimating the perceived errors."

Ssim returns a value from -1 to 1 where 1 is a perfectly similar image.
Mse returns a value from 0 to infinity, 
	where 0 is a perfectly similar image.

parameters:
	-imageA: an RGB image read in using openCV
	-imageB: an RGB image read in using openCV

returns:
	-tuple containing two results:
		1) the ssim comparison result: a double from -1 to 1
		2) the mse comparison result: a double from 0 to infinity
"""
def compare_images(imageA, imageB):
	# compute the mean squared error and structural similarity
	# index for the images
	s = ssim(imageA, imageB)
	m = mse(imageA, imageB)

	return (s, m)
 
	#in our case, we won't plot every image we compare
	# # setup the figure
	# fig = plt.figure(title)
	# plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
 
	# # show first image
	# ax = fig.add_subplot(1, 2, 1)
	# plt.imshow(imageA, cmap = plt.cm.gray)
	# plt.axis("off")
 
	# # show the second image
	# ax = fig.add_subplot(1, 2, 2)
	# plt.imshow(imageB, cmap = plt.cm.gray)
	# plt.axis("off")
 
	# # show the images
	# plt.show()

def show_two_images(imageA, imageB, title, subtitle):
	fig = plt.figure(title)
	plt.suptitle(subtitle)

	# show imageA
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(imageA, cmap = plt.cm.gray)
	plt.axis("off")
 
	# show the second image
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(imageB, cmap = plt.cm.gray)
	plt.axis("off")
 
	# show the images
	plt.show()

"""
This is main. It will run first when the program is run
"""
if __name__=='__main__':
	# This assumes arguments are like: key1=val1 key2=val2 (with NO spaces between key equal val!)
	args = {}

	for arg in sys.argv[1:]:
		k,v = arg.split('=')
		args[k] = v

	#make sure image path starts with a /
	if(args["image"][0] != '/'):
		args["image"] = '/' + args["image"]
	if(args["folder"][0] != '/'):
		args["folder"] = '/' + args["folder"]

	#read image into original_img and convert to RGB
	orig_fp = os.path.dirname(os.path.abspath(__file__)) + args["image"]
	original_img = cv2.imread(orig_fp)
	h,w,channels = original_img.shape
	print(h,w,channels)
	original_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)
	

	# (comparison_result, RGB image)
	closest_file_ssim = (-1, "")
	closest_file_mse = (-1, "")

	#Loop through the images in the comparison folder
	for file in os.listdir(args["folder"]):
		#read image into compare and convert to RGB
		file = os.path.dirname(os.path.abspath(__file__)) + str(args["folder"] + file)
		print(file)
		sys.exit()
		compare_img = cv2.imread(file)
		compare_img = cv2.cvtColor(compare_img, cv2.COLOR_BGR2RGB)
		compare_img = resize(compare_img, (h,w))

		#returns a tuple with the mse and ssim comparison results
		current_file = compare_images(original_img, compare_img)
		if(current_file[1] > closest_file_ssim[0]):
			closest_file_ssim = (current_file[0], compare_img)
		if(current_file[0] > closest_file_mse[0]):
			closest_file_mse = (current_file[0], compare_img)
	# show our results
	# plot closest match using MSE
	title = "closest image match using MSE"
	subtitle = "MSE: %.2f" % (closest_file_mse[0])
	show_two_images(original_img, closest_file_mse[1], title, subtitle)

	#plot closest match using SSIM
	title = "closest image match using SSIM"
	subtitle = "MSE: %.2f" % (closest_file_ssim[0])
	show_two_images(original_img, closest_file_ssim[1], title, subtitle)
	# fig = plt.figure("closest image match using MSE")
	# plt.suptitle("MSE: %.2f" % (closest_file_mse[0]))
 
	# # show original image
	# ax = fig.add_subplot(1, 2, 1)
	# plt.imshow(original_img, cmap = plt.cm.gray)
	# plt.axis("off")
 
	# # show the second image
	# ax = fig.add_subplot(1, 2, 2)
	# plt.imshow(closest_file_mse[1], cmap = plt.cm.gray)
	# plt.axis("off")
 
	# # show the images
	# plt.show()



	sys.exit()

	# load the images -- the original, the original + contrast,
	# and the original + photoshop
	original = cv2.imread("images/jp_gates_original.png")
	contrast = cv2.imread("images/jp_gates_contrast.png")
	shopped = cv2.imread("images/jp_gates_photoshopped.png")
	
	# convert the images to grayscale
	original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
	contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)
	shopped = cv2.cvtColor(shopped, cv2.COLOR_BGR2GRAY)

	# initialize the figure
	fig = plt.figure("Images")
	images = ("Original", original), ("Contrast", contrast), ("Photoshopped", shopped)
	
	# loop over the images
	for (i, (name, image)) in enumerate(images):
		# show the image
		ax = fig.add_subplot(1, 3, i + 1)
		ax.set_title(name)
		plt.imshow(image, cmap = plt.cm.gray)
		plt.axis("off")
	
	# show the figure
	plt.show()
	
	# compare the images
	compare_images(original, original, "Original vs. Original")
	compare_images(original, contrast, "Original vs. Contrast")
	compare_images(original, shopped, "Original vs. Photoshopped")