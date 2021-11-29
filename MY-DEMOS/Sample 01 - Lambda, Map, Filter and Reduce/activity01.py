import functools

#We can do a lambda which is a simple anonymous function, it cant take any number of args but it will have only one expression
areaTriangle = lambda base, height: (base * height) / 2
#The result variable will call the ariaTriangle which will call the lambda inside of it
result = areaTriangle(2,3)
print(result)

#We ask for the numbers in the console
string = input("Type numbers separated by spaces: ")
#Now, with list() we made a list made of the numbers but removing the spaces with the split()
stringNoSpace = list(string.split())

#this function recieves a element in the stringNoSpace and it scrolls all the element, if there is a element which is not a number, it will show a error message and it close the program
def charException(n):
    numbers = "0123456789"
    ret = ""
    for i in range(len(n)):
        if(numbers.find(n[i]) == -1):
            print(" ERROR: There is a letter in the number string")
            exit()
        else:
            ret += n[i]
    return ret        

#now, we do a list with the map(), this function scrolls all the list but it implements the function charException for all the elements at the list
fullString = list(map(charException,stringNoSpace))
#here, i'm doing a new list which is a copy of fullString but the type of the values now are int
fullInt = []
[fullInt.append(int(i)) for i in fullString]

#for now, we filter the fullInt list and remove the numbers < 10
fullIntFiltered = list(filter(lambda n: n >= 10, fullInt))

#now, we use the reduce with a lambda to multiply the numbers at the list filtered
resultL = functools.reduce(lambda n1, n2: n1*n2,fullIntFiltered)
print("The result is: " + str(resultL))
