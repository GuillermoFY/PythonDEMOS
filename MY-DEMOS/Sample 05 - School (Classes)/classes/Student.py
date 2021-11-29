class Student:
    name = ""
    year = ""

    def __init__(self,name,year,teacher,school):
        self.name = name
        self.year = year
        if isinstance(teacher,Teacher):
            self.teacher = teacher
        else:
            print("Teacher is not in the class named Teacher")
            exit()
        
        if isinstance(school,School):
            self.school = school
        else:
            print("School is not in the class named School")
            exit()
    
    def __init__(self,name,year,school):
        self.name = name
        self.year = year
        if isinstance(school,School):
            self.school = school
        else:
            print("School is not in the class named School")
            exit()
    
    def __init__(self,name,year,teacher):
        self.name = name
        self.year = year
        if isinstance(teacher,Teacher):
            self.teacher = teacher
        else:
            print("Teacher is not in the class named Teacher")
            exit()

    def __init__(self,name,year):
        self.name = name
        self.year = year

    #toString
    def __str__(self):
        return "Student: " + self.name() + ", year: " + self.year() + ", School name: " + self.school.name() + ", Teacher's name: " + self.teacher.name()