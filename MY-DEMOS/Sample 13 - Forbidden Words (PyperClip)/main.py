import sys
import os.path
import pyperclip

#Getting the files (input)
if len(sys.argv) != 2:
    print(" ERROR: You have to enter only one parameter!!!")
    exit()

ip = sys.argv[1]

#Checking if the file exists
if not os.path.isfile(ip):
    print(" ERROR: File " + ip + " not exists!!!")
    exit()

#opening the file input
fileIp = open(ip,"r")
#and now, we made a list with all the lines of the file
forbidden = []

#Another way to open the files, and mapping the list, deleting the \n sentence
with open(ip, "r") as file:
    forbidden = list(map(str.rstrip, file))

#Checking if there is more than one word in the forbidden words list
for line in forbidden:
    if(len(line.split(" ")) != 1):
        print(" ERROR: You have to separate the words with a line break. Line: " + line)
        exit()

#Now we do this infinite bucle (it won't close until you put ctrl+c at the command line)
newV = ""
while True:
    #wait for a new paste and then replace the stars and copy the string
    newV = pyperclip.waitForNewPaste()
    for words in forbidden:
        stars = ""
        for i in range(len(words)):
            stars += "*"
        newV.replace(words,stars)
    pyperclip.copy(newV)

