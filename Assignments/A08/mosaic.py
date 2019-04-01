import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import matplotlib.pyplot as plt
import numpy as np
import random
#import colors.py as colors


def show_two_images(imageA, imageB, title, subtitle):
	fig = plt.figure(title)
	plt.suptitle(subtitle)

	# show imageA
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(imageA, cmap = plt.cm.gray)
	plt.axis("off")
 
	# # show the second image
	# ax = fig.add_subplot(1, 2, 2)
	# plt.imshow(imageB, cmap = plt.cm.gray)
	# plt.axis("off")
 
	# show the images
	plt.show()

"""
Returns a random image from a folder of images

Arguments:
    sub_img_path   -- folder of images
Returns:
    PIL image
"""
def get_rand_subimg(sub_img_path):
    im = random.choice([x for x in os.listdir(sub_img_path)])
    # print(os.path.join(sub_img_path, im))
    # sys.exit()
    rand_im = Image.open(os.path.join(sub_img_path, im))
    return rand_im


def img_to_mosaic(**kwargs):
    #Get arguments that were passed
    file_name = kwargs.get('file_name',None)
    img_Path = kwargs.get('img_Path',None)
    sub_img_path = kwargs.get('sub_img_path',None)
    output_folder_path = kwargs.get('output_folder_path', os.path.dirname(os.path.abspath(__file__)) + '\\output_images\\output.png')
    size = int(kwargs.get('size',16))

    out_file_name = file_name
    #check if file will be overwritten by mosaic
    if(img_Path == output_folder_path):
        #file_name needs to have _mosaic added to it
        temp_f_name = out_file_name.split('.')
        temp_f_name[-2] = temp_f_name[-2] + '_mosaic' #do not alter the file type (.png, etc.)
        out_file_name = ""
        for n in temp_f_name:
            out_file_name += n + '.'
        out_file_name = out_file_name[0 : -1] # remove the final .
    
    im = Image.open(img_Path + file_name)
    
    w,h = im.size
    im = resize(im, w * size) 
    w,h = im.size
    

    rgba_im = im.convert('RGBA')

    # # Open a new image using 'RGBA' (a colored image with alpha channel for transparency)
    # #              color_type      (w,h)     (r,g,b,a) 
    # #                   \           /            /
    # #                    \         /            /
    # newImg = Image.new('RGBA', im.size, (255,255,255,255))

    #loop through pixels of original image and write to rgba_im
    for x in range(8, w, 16):
        for y in range(8, h, 16):
            sub_im = get_rand_subimg(sub_img_path)
            sub_im = resize(sub_im, size)
            r, g, b, a = rgba_im.getpixel((x, y)) #get rgb value at this pixel
            if(((r + g + b) // 3) > 10 and ((r + g + b) // 3) < 246):
                sub_im = sub_im.convert('RGBA') #convert to RGBA so the image can be masked
                rgba_im.paste(sub_im, (x, y), sub_im)
            y+=16
        x+=16
    
    # Save the image.
    rgba_im.save(output_folder_path + out_file_name)
    rgba_im.show()

    return #void function

    

def resize(img,width):
    """
    This resizes the img while maintining aspect ratio. Keep in 
    mind that not all images scale to ascii perfectly because of the
    large discrepancy between line height line width (characters are 
    closer together horizontally then vertically)
    """
    
    wpercent = float(width / float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((width ,hsize), Image.ANTIALIAS)

    return img


if __name__=='__main__':
    """
    This program requires four parameters to be passed.
    input_file - the image file name in ~\input_images\ (i.e. rainbow.png), 
    input_folder - the folder which contains sub_images, which will be pasted over the original image (i.e. emojis/)
    output_folder - the output folder name (i.e. mosaics/)
    size - the size of the "chunks" within the images. (i.e. 16)
    """
    # This assumes arguments are like: key1=val1 key2=val2 (with NO spaces between key equal val!)
    args = {}

    for arg in sys.argv[1:]:
        k,v = arg.split('=')
        args[k] = v
    #we should now have a dictionary with the following keys:
    #input_file, input_folder, output_folder, size

    #make sure paths starts with a /
    # if(args["input_file"][0] != '/'):
    #     args["input_file"] = '/' + args["input_file"]
    # if(args["input_folder"][0] != '/'):
    #     args["input_folder"] = '/' + args["input_folder"]
    # if(args["output_folder"][0] != '/'):
    #     args["output_folder"] = '/' + args["output_folder"]

    img_Path = args["input_file"]
    sub_img_path = args["input_folder"]
    output_folder_path = args["output_folder"]

    #if the arguments are absolute file paths, don't treat them as relative file paths
    if(not (os.path.isfile(args["input_file"]))):
        img_Path = os.path.dirname(os.path.abspath(__file__)) + '\\orig_imgs\\' + args["input_file"]
    if(not (os.path.isdir(args["input_folder"]))):
        sub_img_path = os.path.dirname(os.path.abspath(__file__)) + args["input_folder"]
    if(not (os.path.isdir(args["output_folder"]))):
        output_folder_path = os.path.dirname(os.path.abspath(__file__)) + args["output_folder"]

    #split file name and file path
    path_arr = img_Path.split('\\')
    file_name = path_arr[-1]
    leng = len(img_Path) - len(file_name)
    img_Path = img_Path[0 : int(leng)]

    img_to_mosaic(file_name=file_name, img_Path=img_Path, sub_img_path=sub_img_path, output_folder_path=output_folder_path, size=args["size"])