# A7 Script for Cropping Images from Annotations

folder = "/home/a7md/Datasets/test/OALPR_benchmarks/endtoend/br"
files = glob.glob(os.path.join(folder, "*"))
for i in range(0,115):
    file = files[i]
    filename = os.path.basename(file)
    filenameonly = os.path.splitext(filename)[0]
    imagefile = str(glob.glob(os.path.join(folder, filenameonly+".jpg")))[2:-2]
    annotationfile = str(glob.glob(os.path.join(folder, filenameonly+".txt")))[2:-2]
    
    readannot = open(annotationfile,'r')
    line = readannot.read()
    line = line.split()
    x1 = int(line[1])
    y1 = int(line[2])
    x2 = int(line[3])+int(line[1])
    y2 = int(line[4])+int(line[2])
    
    img = cv2.imread(imagefile)
    crop_img = img[y1:y2, x1:x2]
    cv2.imwrite(imagefile, crop_img);
    print("Images have been cropped and overwritten !")
