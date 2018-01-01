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
:::::::: String Parsing :: :::::::::::::::::

For ML tasks: we need to often provide a list 
of labels while training neural networks with 
supervised learning. this program aims to extract
labels from the file names.

"""
import os 
import time

print("Welcome to the Filename String Parser and Generator") 
time.sleep(0.5)

dir_select = input('Please enter a folder name in "double quotes": ')
time.sleep(0.5)
file_list = os.listdir(dir_select)

print("Files that are present in the selected directory:")
print("--------------------------------------------------") 
time.sleep(0.5)
for filename in file_list:
	  print(os.path.join(filename))

print("License plate extraction")
print("--------------------------------------------------") 

f = open('labels.txt','w')

for platenumber in file_list:
# Remove first 20 and last 35 characters in the string
	platenumber = platenumber[20:-36]
# Rightmost split from the 2nd _underscore character and read 3rd array cell 
	platenumber = platenumber.rsplit('_',2)[2]	 
	print(os.path.join(platenumber))
	f.write(platenumber)
	f.write(" ")

f.close()	
