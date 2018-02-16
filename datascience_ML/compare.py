import os, glob

'''
Python code to compare two different files.
Usage:  1. enter path in folder1 and folder2
        2. in i_list and a_list edit file format as needed
Ackno: Dev by a7md
'''

folder1 = "/home/simplicity/a7md/ALPR/Data/NewData/Resized"
folder2 = "/home/simplicity/a7md/ALPR/Data/NewData/CSVAnnotations"

# Create a list of all image files and annotation files 
i_list = glob.glob(os.path.join(folder1, "*"))
a_list = glob.glob(os.path.join(folder2, "*.csv"))

# Sort all files in a similar fashion
i_list.sort()
a_list.sort()

print("Files found in folder 1: {} and folder 2: {}".format(len(i_list), len(a_list)))

for i in range(0,len(a_list)):

    filename1 = os.path.basename(i_list[i])  # returns 'helpers_image.tif'
    filename2 = os.path.basename(a_list[i]) # return 'helpers_image.qml'

    # Thanks to Cyrbil for noticing a bug here
    name1 = filename1.rsplit('.', 1)[0]  # returns 'helpers_image'
    name2 = filename2.rsplit('.', 1)[0]  # return 'helpers_image'

    if name1 == name2:  # This is True for this exact case
        print(i,"{} matches {}".format(name1,name2))
    else:
        print(i,"No match found for",name1)
