from os import name
import sys
import csv
import barcode
from barcode import EAN13
from barcode.writer import ImageWriter

#We have to obligate to only put one parameter
if(len(sys.argv)>2):
    print(" ERROR: You entered more than one parameter!!!")
    exit()
elif(len(sys.argv)<=1):
    print(" ERROR: You have to enter the file parameter!!!")
    exit()

csvFile = sys.argv[1]

#now, we create a students with the parameters of the csv file and then create a list of files
class Student:
    name = ""
    id = 0

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return "Name: " + self.name + ", ID: " + self.id

students = []

#we are using csv to opening it, reading all the file and finally, creating a student with name = row 0 and id = row 1
with open(csvFile) as csv_file:
    reader = csv.reader(csv_file,delimiter=",")
    lineCount = 0
    for row in reader:
        if lineCount != 0: #if the line count is 0 it means that are the columns name
            studentF = Student(row[0],row[1])
            students.append(studentF)
        lineCount+=1       



for i in range(len(students)):
    #EAN13 is a key which has 13 numbers so, I putted 20 zeros and add the id of the student (because there are only two)
    ean = "000000000000"+str(students[i].id)
    #Now we use the .get and add the type of codification which is ean13, then we put our ean13 code and then we use the ImageWriter to write the barcode
    img = barcode.get('ean13',ean,writer=ImageWriter())
    #Finally, we used we use img.save to create the png images on our folder
    fileN = img.save(students[i].name)
    