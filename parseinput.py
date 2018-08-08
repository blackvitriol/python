# When using PyQt GUI 

# def browse_dir(self):
#    self.analytic_dir = QtGui.QFileDialog.getExistingDirectory(self, 'Open File', '/')
#    self.lineEdit.setText(self.analytic_dir)

# def func_analytics(self):
#    inputstream = str(self.lineEdit.text())

    inputstream = "/home/ahmad/somerandomplace/file.jpg"

    if os.path.isfile(inputstream) and inputstream.lower().endswith(('.png', '.jpg', '.jpeg')):
        print("Its an image")

    elif os.path.isdir(inputstream):
        print("Its a dir")
        files = [item for sublist in [glob.glob(inputstream + ext) for ext in ["/*.png", "/*.jpg", "/*.JPG", "/*.PNG"]] for item in sublist]
        for everyfile in files:
            print(everyfile)

    elif os.path.isfile(inputstream) and inputstream.lower().endswith(('.mp4', '.avi'))::
        print("Its a video..")

    else:
        print("What are you trying to run ?!")
