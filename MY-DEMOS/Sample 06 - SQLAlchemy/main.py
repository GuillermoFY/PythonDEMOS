from classes import dataToBD
from classes.Student import Student

#now, we create the run function
def run():
    #here, we create two objects of the Studdent class
    guille = Student('Guille',2)
    sori = Student("Sori",2)

    #and then, we add to the session the two objects
    dataToBD.session.add(guille)
    dataToBD.session.add(sori)
    
    #finally, we do the commit to save 
    dataToBD.session.commit()
    print(guille.id)
    print(sori.id)

    """If we run it twice, we will see that the id will change because the new objects added have a new id
        so the first time we run it, the id will be 1 and 2, the second time it will add two new students
        called the same name but with the id like 3 and 4"""

if __name__ == '__main__':
    dataToBD.Base.metadata.create_all(dataToBD.engine)
    run()