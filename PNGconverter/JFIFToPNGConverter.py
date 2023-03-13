# import the lib
# official link  https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
from PIL import Image, ImageFilter
import os
from os import listdir
import sys


# get the path/directory " / " should be used in windows as well " \ " will not work
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
# read the file and convert to png
folder_dir = sys.argv[1]
for images in os.listdir(folder_dir):
        file_name, extention = os.path.splitext(images)
        source_path = sys.argv[1] + images
        print(file_name, extention)
        outfile = file_name + ".png"
        if images != outfile:
                destination_file = sys.argv[2] + outfile
                if os.path.exists(sys.argv[2]):
                        pass
                else:
                        os.mkdir(sys.argv[2])

                try:
                        with Image.open(source_path) as im:
                                 im.save(destination_file)
                except OSError:
                        print("cannot convert", destination_file)

