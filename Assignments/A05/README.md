This assignment converts an image to colored ASCII art. It displays the image and saves to the local output_images\ folder

## Notes on running the program
To properly execute this code, the user should supply either two or four arguments after 

    $ python ascii_image.py

- The first parameter should be the image file name in .\input_images\ (i.e. rainbow.png), 
- the second the font name in .\fonts\ (i.e. block_art.ttf),
- the third the output file name in .\output_images\ (i.e. output.png)
- the fourth the font size (i.e. 12)

So to run the program, the user might type

    $ python ascii_image.py rainbow.png block_art.ttf


to specify the image to convert and the font to use in conversion
or

    $ python ascii_image.py rainbow.png block_art.ttf output_1.png 12 
to specify the image to convert, the font to use in conversion, the output file name, and the font size

### ascii_image.py
This script takes images in the input_images folder and converts them to colored ASCII art before saving the new art to the output_images folder
