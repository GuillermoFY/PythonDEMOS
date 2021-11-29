import os
import shutil


#Here, we get the actual path
path = os.path.dirname(os.path.realpath(__file__))

#Now, we do some list that we will use for the path, extension and names
fileExtensions = []
filePaths = []
fileNames = os.listdir(path) #this method creates a list of all the files into the path

#Here, we catch all names and know its extension and then we append to the lists
for name in fileNames:
    extension = name.split(".")[-1] 
    filePaths.append(path+"\\"+name)
    fileExtensions.append(extension)

#Create the folders (if they are created, it will be an exception)
for extension in fileExtensions:
    try:
        os.mkdir(os.path.join(path,extension))
    except OSError as error:
        print(path+"\\"+extension + " Already Exists!!!")

#Move the paths (if they are already moved, it will be an exception)
for i in range(len(filePaths)):
    try:
        shutil.move(filePaths[i],path+"\\"+fileExtensions[i]+"\\"+fileNames[i]) #we use shutil.move(path,newPath)
    except Error as error:
        print(" ERROR: Cannot move a not existing file! Or is already moved.")


