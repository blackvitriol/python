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
::::Python Learning::::::::::::29:12:17:::
:::::::: Image Analysis :::::::::::::::::

Often, when before we process images, we need
to inspect them in different colour spaces to
see if they are worth using for analysis, and
what kind of operations we should apply to them.

"""
import numpy as np
import cv2
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
from skimage import color
from skimage import data
from matplotlib import pyplot as plt

showinfo("A7's Image Conversion", "Welcome! This is version 0.1 alpha, so select your image then pls close the windows to view alternatives. You can also save images.")

# Load the file
loadedfile = askopenfilename()
img = data.load(loadedfile)

# Convert to different styles
img_hsv = color.rgb2hsv(img)
img_yuv = color.rgb2yuv(img)
img_ycbcr = color.rgb2ycbcr(img)
img_lab = color.rgb2lab(img)

# View the image regular
plt.imshow(img)
plt.title('RGB Image', color='black')
plt.axis("off")
plt.show()

# View the HSV image (Hue, Saturation, Value)
plt.imshow(img_hsv)
plt.title('HSV Image', color='black')
plt.axis("off")
plt.show()

# View the YUV image
plt.imshow(img_yuv)
plt.title('YUV Image', color='black')
plt.axis("off")
plt.show()

# View the Y-Cb-Cr image
plt.imshow(img_ycbcr)
plt.title('Y-Cb-Cr Image', color='black')
plt.axis("off")
plt.show()

# View the Lab image
plt.imshow(img_lab)
plt.title('Lab Image', color='black')

plt.axis("off")
plt.show()
