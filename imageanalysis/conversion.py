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
from skimage import colour
from matplotlib import pyplot as plt

# Load the file
loadedfile = askopenfilename()

# Convert to different styles
img = cv2.imread(loadedfile,0)

img_hsv = skimage.color.rgb2hsv(img)
img_yuv = skimage.color.rgb2yuv(img)
img_ycbcr = skimage.color.rgb2ycbcr(img)
img_lab = skimage.color.rgb2lab(img)


# View the image
plt.imshow(cv_img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.title('Is this the best color?', color='#afeeee')
plt.show()

