# A7 Script for Cropping Images from Annotations

'''
For a dataset containing images and annotations,
some further data mining might be required to extract
specific data from both images (as pixels) and XML (as text).

This script has parses for txt and XML files.
'''
image_folder = "/home/a7md/New/Datasets/test/AC/test/jpeg"
annot_folder = "/home/a7md/New/Datasets/test/AC/test/xml"

files = glob.glob(os.path.join(image_folder, "*"))

# Set range for selective files
for i in range(0,5):
    file = files[i]
    filename = os.path.basename(file)
    filenameonly = os.path.splitext(filename)[0]
    # Set type of files and their formats: "JPG" / "XML"
    imagefile = str(glob.glob(os.path.join(image_folder, filenameonly+".jpg")))[2:-2]
    annotationfile = str(glob.glob(os.path.join(annot_folder, filenameonly+".xml")))[2:-2]
    
#     # For text files
#     readannot = open(annotationfile,'r')
#     line = readannot.read()
#     line = line.split()
#     x1 = int(line[1])
#     y1 = int(line[2])
#     x2 = int(line[3])+int(line[1])
#     y2 = int(line[4])+int(line[2])

    # For XML files
    tree = ET.parse(annotationfile)
    root = tree.getroot()
    plate = [] # to extract ground truth   
    objects = root.find('object')
    bndbox = objects.find('bndbox')
    x1 = int(bndbox.find('xmin').text)
    y1 = int(bndbox.find('ymin').text)
    x2 = int(bndbox.find('xmax').text)
    y2 = int(bndbox.find('ymax').text)
    
    #OpenCV to resize image based on crop info
    img = cv2.imread(imagefile)
    crop_img = img[y1:y2, x1:x2]
    cv2.imshow('plate',crop_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(imagefile, crop_img);

    print("Images have been cropped and overwritten !")
