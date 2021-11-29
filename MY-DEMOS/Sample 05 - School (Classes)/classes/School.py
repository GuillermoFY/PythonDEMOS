from classes.Teacher import Teacher
from classes.Student import Student

class School:
    name = ""
    location = ""
    headmaster = ""
    teachers = {}
    students = {}

    #CONSTRUCTOR     
    def __init__(self,name,location,headmaster,students,teachers):
        self.name=name
        self.location=location
        self.headmaster=headmaster
        if isinstance(students,dict):
            self.students = students
        else:
            print("Students parameter is not a dictionary")
            exit()
        if isinstance(teachers,dict):
            self.teachers = teachers
        else:
            print("Teachers parameter is not a dictionary")
            exit()

    def __init__(self,name,location,headmaster,students):
        self.name=name
        self.location=location
        self.headmaster=headmaster
        if isinstance(students,dict):
            self.students = students
        else:
            print("Students parameter is not a dictionary")
            exit()

    def __init__(self,name,location,headmaster,teachers):
        self.name=name
        self.location=location
        self.headmaster=headmaster
        if isinstance(teachers,dict):
            self.teachers = teachers
        else:
            print("Teachers parameter is not a dictionary")
            exit()

    def __init__(self,name,location,headmaster):
        self.name=name
        self.location=location
        self.headmaster=headmaster
    
    def newStudent(self,student):
        if isinstance(student, Student):
            self.students[student.name] = student
        else:
            print("Students parameter is not a class")
    
    def newTeacher(self,teacher):
        if isinstance(teacher, Teacher):
           
            self.teachers[teacher.name] = teacher
        else:
            print("Students parameter is not a class")
    