# Importing libraries and collecting tools
from PIL import Image
import os, glob
from tqdm import tqdm

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
::::Python Learning::::::::::::15:05:18:::
:::::::: RGB Conversion  :: :::::::::::::::
"""
# Data Integrity in ML datasets:
# To convert images to RGB for equal 3 layers

# Defining paths and allocating resources
imagepath = "/home/a7md/Datasets/train/Collective/JPEGImages"
imagelist = glob.glob(os.path.join(imagepath, "*.jpg"))

print("You have {} images..".format(len(imagelist)))

for image in tqdm(imagelist):
    img = Image.open(image)
    rgbimg = img.convert('RGB')
    rgbimg.save(image)
    
print("Converted all images succesfully !")




