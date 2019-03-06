import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def img_to_ascii(**kwargs):
    """ 
    The ascii character set we use to replace pixels. 
    The grayscale pixel values are 0-255.
    0 - 25 = '#' (darkest character)
    250-255 = '.' (lightest character)
    """
    #ascii_chars = [ u'🦍', 'A', '@', '%', 'S', '+', '<', '*', ':', ',', '.']
    ascii_chars = [ '#', 'A', '@', '%', 'S', '+', '<', '*', ':', ',', '.']
  
    #Get arguments that were passed
    imgPath = kwargs.get('imgPath',None)
    fontPath = kwargs.get('fontPath',None)
    outPath = kwargs.get('outPath', os.path.dirname(os.path.abspath(__file__)) + '\\output_images\\output.png')
    fontSize = int(kwargs.get('fontSize',12))

    im = Image.open(imgPath)
    
    #we don't resize the image to allow high resolution images to be viewed in detail. 
    #This does slow runtime as images get larger though
    w,h = im.size
    #im = resize(im,width) 

    rgb_im = im.convert('RGB')

    # Open a new image using 'RGBA' (a colored image with alpha channel for transparency)
    #              color_type      (w,h)     (r,g,b,a) 
    #                   \           /            /
    #                    \         /            /
    newImg = Image.new('RGBA', im.size, (255,255,255,255))

    # Open a TTF file and specify the font size
    fnt = ImageFont.truetype(fontPath, fontSize)

    # get a drawing context for your new image
    drawOnMe = ImageDraw.Draw(newImg)

    #loop through pixels of original image and write to newImg
    for x in range(w):
        for y in range(h):
            r, g, b = rgb_im.getpixel((x, y)) #get rgb value at this pixel
            ch = ascii_chars[(r + g + b) // 3 // 25] #use rgb val to choose character
            drawOnMe.text((x, y), ch, font=fnt, fill=(r, g, b)) #write character to newImg

    newImg.show()
    
    # Save the image.
    newImg.save(outPath)

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
    This program requires either two or four parameters to be passed.
    The first parameter should be the image file name in ~\input_images\ (i.e. rainbow.png), 
    the second the font name in ~\fonts\ (i.e. block_art.ttf),
    the third the output file name in ~\output_images\ (i.e. output.png)
    the fourth the font size (i.e. 12)
    """
    imgPath = os.path.dirname(os.path.abspath(__file__)) + '\\input_images\\'
    imgPath += sys.argv[1]
    fontPath = os.path.dirname(os.path.abspath(__file__)) + '\\fonts\\'
    fontPath += sys.argv[2]
    if(len(sys.argv) > 3):
        outPath = os.path.dirname(os.path.abspath(__file__)) + '\\output_images\\'
        outPath += sys.argv[3]
        fontSize = sys.argv[4]
        img_to_ascii(imgPath=imgPath, fontPath=fontPath, outPath=outPath, fontSize=fontSize)
        sys.exit()
    img_to_ascii(imgPath=imgPath, fontPath=fontPath)
