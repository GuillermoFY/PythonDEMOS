class Teacher:
    name = ""
    type = "" #the type can be (science, letters, or mixed)
    
    def __init__(self,name,type,school):
        self.name = name
        if(type.lower() == "science" or type.lower() == "letters" or type.lower() == "mixed"):
            self.type = type
        else:
            print("Teacher's type is not Science|Letters|Mixed!!!")
        if isinstance(school,School):
            self.school = school
        else:
            print("School is not in the class named School")
            exit()

    def __init__(self,name,type):
        self.name = name
        self.type = type

    #toString
    def __str__(self):
        return "Teacher: " + self.name() + ", Type: " + self.type() + ", School name: " + school.name()