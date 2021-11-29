import csv
from kivy.lang import Builder
from kivymd.app import MDApp
import hashlib

#Creating the main app
class MainApp(MDApp):
    #here we do a bidimensional list with userList[i][0] = username and userList[i][1] = password in sha1 from the users.csv
    userList = []

    #now, we do the class parameters for the user and password given in kivy and the password in sha1
    userK = ""
    passwordK = ""
    passwordSha = ""

    #Application Starts and shows the theme, the palette and build the file to show it on screen
    def build(self):
        self.charge() #here, we charge the csv file and add all the users at the userList
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("./kvfiles/login.kv")
        
    #this is a methot that is on a listener of the button clear, and it clears all the text fields and the test label
    def clear(self):
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""
        self.root.ids.test_label.text = ""

    #the logger is other method that is on a listener of the button test
    def logger(self):
        self.userK = self.root.ids.user.text
        self.passwordK = self.root.ids.password.text
        if self.passwordK == "" or self.userK == "": #If there is no password or no user (or both of them) it will appear at the test label this
            self.root.ids.test_label.text = "User or Password are empty"
        else:
            #Changing the password to sha
            sha1 = hashlib.sha1()
            key = self.passwordK.encode('utf-8')
            sha1.update(key)
            self.passwordSha = sha1.hexdigest()

            #Now, check and if there is one user or more (in case of duplicated) will be okay, say OK
            r = self.compare()
            if r >= 1:
                self.root.ids.test_label.text = "OK"
            else:
                self.root.ids.test_label.text = "User or Password are wrong"

    
    def charge(self):
        #we are using csv to opening it, reading all the file and finally, adding to the userList the parameters of the users in the csv file
        # userList[i][0] = username and userList[i][1] = password
        with open("users.csv") as csv_file:
            reader = csv.reader(csv_file,delimiter=",")
            lineCount = 0
            for row in reader:
                if lineCount != 0: #if the line count is 0 it means that are the columns name
                    list = [row[0],row[1]]
                    self.userList.append(list)
                lineCount=+1
               
    #here we see if there is a user in the csv file (already charged and the userList updated) 
    def compare(self):
        i = 0
        for list in self.userList:
            if(list[0] == self.userK and list[1] == self.passwordSha):
                i+=1
            #if i > 1 there will be duplicated users
        return i   





MainApp().run()