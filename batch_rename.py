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
:::::::: Batch Rename :::::::::::::::::::::

Linux will sometimes make files without filetype in the name
this should fix it...
"""
print("Welcome to A7's Batch Renaming Tool...")

import glob,os

files = glob.glob('*')

print("Files found:")
print(files)

filetype = input("Enter your file format [example:'.jpg']:")

print("Now renaming all files with following format:", filetype)

for File in files:
    newname = File + filetype
    os.rename(File, newname)

'''
# Undo Rename if you mucked up
for File in files:
    removal = len(filetype)
    newname = File[:-removal]
    os.rename(File, newname)
'''

print("Done renaming files...")
