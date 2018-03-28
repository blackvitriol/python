#!/usr/bin/env python
__author__ = 'blackvitriol'


"""                                       
                o  8                   
                8  8                   
.oPYo. o    o  o8P 8oPYo. .oPYo. odYo. 
8    8 8    8   8  8    8 8    8 8' `8 
8    8 8    8   8  8    8 8    8 8   8 
8YooP' `YooP8   8  8    8 `YooP' 8   8 
8 ....::....8 ::..:..:::..:.....:..::..
8 :::::::ooP'.:::::::::::::::::::::::::
..:::::::...:::::::::::::::A7MD0V:::::::
::::Python Learning::::::::::::28:03:18:::
:::::::: Batch Resize Images :::::::::::::::::

Give it a folder and it will resize all JPG images in it

"""
print("Welcome to A7's Image Batch Resizing Tool...")


import cv2
import glob,os

imgs = glob.glob('*.jpg')
imgs.extend(glob.glob('*.jpeg'))

print("Images found:")
print(imgs)

width = 300
height = 300
print("Resizing all images to 300x300:")

folder = 'resized'
if not os.path.exists(folder):
    os.makedirs(folder)

for img in imgs:
    pic = cv2.imread(img, cv2.IMREAD_UNCHANGED)
    pic = cv2.resize(pic, (width, height))
    cv2.imwrite(folder + '/' + img, pic)
