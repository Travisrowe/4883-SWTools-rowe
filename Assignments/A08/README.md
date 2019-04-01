This assignment pastes sub_images over an original image as an image mosaic. It displays the image and saves to the local mosaics\ folder

## Notes on running the program
To properly execute this code, the user should supply either two or four arguments after 

    $ python mosaics.py

This program requires four parameters to be passed.
- input_file - the image file name in ~\input_images\ (i.e. rainbow.png), 
- input_folder - the folder which contains sub_images, which will be pasted over the original image (i.e. emojis/)
- output_folder - the output folder name (i.e. mosaics/)
- size - the size of the "chunks" within the images. (i.e. 16)

So to run the program, the user might type

    $ python mosaic.py input_file=google_icon.png input_folder=emojis/ output_folder=mosaics/ size=16

to specify the image to convert and the font to use in conversion