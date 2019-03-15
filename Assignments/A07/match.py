"""
This program searches a folder of images to find one that is most visually similar to
a specific image that is passed in.
It takes two arguments to run properly: folder and image
e.g. python3 match.py folder=emoticons image=boom.png
Note that arguments MUST be passed in using 'folder' and 'image' as the key AND there must NOT
be a space on either side of the '='
"""

import sys
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
"""
def compare_images(imageA, imageB, title):
	# compute the mean squared error and structural similarity
	# index for the images
	m = mse(imageA, imageB)
	s = ssim(imageA, imageB)
 
	# setup the figure
	fig = plt.figure(title)
	plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
 
	# show first image
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

	orig_fp = os.path.dirname(os.path.abspath(__file__)) + args["image"]
	original_img = cv2.imread(orig_fp)
	original_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)

	fig = plt.figure("Images")
	# show the image
	ax = fig.add_subplot(1, 3, 1 + 1)
	ax.set_title(args["image"])
	plt.imshow(original_img, cmap = plt.cm.gray)
	plt.axis("off")

	plt.show()

	for file in os.listdir(args["folder"]):
		file = str(args["folder"] + file)
		compare = cv2.imread(file)


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