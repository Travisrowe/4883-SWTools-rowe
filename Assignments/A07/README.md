This program loops through a folder of images to compare it to one test images. The program requires two arguments to run:
- folder: a permanent file-path of the folder of images which will be compared to the test image.
- image: a file-path to the test image. This file-path is relative to the directory this program is in.

## Notes on running the program
This program requires two arguments to run. Furthermore, the arguments must be have key words folder and image and be followed by an '=' and the file path. For example, the program can be run with

    $ python match.py folder=comparison_images/ image=test_images/Mexico.png

Please, be sure to not put a space before or after the '=' after key words 'folder' and 'image' as this will cause problems with running the program.
