Open a text file with file names in it, find these files in a mixture of multiple files and copy them to a folder.

import os, glob
from shutil import copyfile

destination = "/home/a7md/New_Work/Datasets/test/PAK20k"
source = "/home/data/VOCdevkit/VOC2007/JPEGImages"

files_list = glob.glob(os.path.join(source, "*.jpg"))

with open("/home/a7md/New_Work/Datasets/test/PAK20k/test.txt","r") as selection_list:
        for line in selection_list:
            filename = str(line).strip()+".jpg"
            copyfile(source+"/"+filename, destination+"/"+filename)
            
            print(filename, "has been copied...")
