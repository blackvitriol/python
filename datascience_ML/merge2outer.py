'''
                o  8                   
                8  8                   
.oPYo. o    o  o8P 8oPYo. .oPYo. odYo. 
8    8 8    8   8  8    8 8    8 8' `8 
8    8 8    8   8  8    8 8    8 8   8 
8YooP' `YooP8   8  8    8 `YooP' 8   8 
8 ....::....8 ::..:..:::..:.....:..::..
8 :::::::ooP'.:::::::::::::::::::::::::
..:::::::...:::::::::::::::A7MD0V:::::::
::::Python Learning::::::::::::23:04:18:::
:::::::: File Tree Dispersal :: ::::::::::::

Sometimes, we have one directory containing many
subdirectories which further contain many files.

One may wish to extract all the files in subdirectories
and move them to one folder.
'''

image_folder = "/home/simplicity/Downloads/UFPR-ALPR dataset/testing"

destination = "/home/simplicity/Downloads/UFPR-ALPR dataset/testing/collective/"

pngfiles = [os.path.join(root, name)
             for root, dirs, files in os.walk(image_folder)
             for name in files
             if name.endswith(".png")]

for file in pngfiles:
    filename = os.path.basename(file)
    filenameonly = os.path.splitext(filename)[0]
    os.rename(file, destination+filenameonly+".png")
