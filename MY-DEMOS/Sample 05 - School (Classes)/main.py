from classes.School import School
from classes.Student import Student
from classes.Teacher import Teacher

pepito = Student("Pepito","1st ESO")
juanito = Student("Juanito","2nd ESO")
jaimito = Student("Jaimito","3st ESO")

sergi = Teacher("Sergi","Science")
manolo = Teacher("Manolo","Letters")
paco = Teacher("Paco","Mixed")

pepito.teacher = sergi
juanito.teacher = manolo
jaimito.teacher = paco


iesSerraPerenxisa = School("IES Serra Perenxisa","Torrent","IDK")
madreSacramento = School("Madre Sacramento", "Torrent", "IDK")

iesSerraPerenxisa.newTeacher(sergi)
iesSerraPerenxisa.newTeacher(manolo)
iesSerraPerenxisa.newTeacher(paco)

iesSerraPerenxisa.newStudent(pepito)
madreSacramento.newStudent(juanito)
madreSacramento.newStudent(jaimito)

print("IESSP students:" + str(iesSerraPerenxisa.students) + ", teachers: " + str(iesSerraPerenxisa.teachers))