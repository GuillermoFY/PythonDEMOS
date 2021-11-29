import os

#this function recieves a element in the fileTextArray and go through all the element, and it will return a array filtering only the numbers, it will skip if is there a letter or a space
def charException(n):
    numbers = "123456789"
    ret = []
    for i in range(len(n)):
        if(numbers.find(n[i]) != -1):
            ret.append(n[i])
    return ret  

#now, I made a function which return true if the multidimensional list has [9][9] of length and throws a exception if not
def goodLength(oList):
    if(isinstance(oList,list)): #to know the instance of the list
        for i in range(len(oList)):
            if(isinstance(oList[i],list)):
                if(len(oList)==9 and len(oList[i])==9):
                    return True
                else:
                    print("   ERROR: Sudoku format is incorrect!!! (Try to do a 9x9 table separated with spaces)")
                    exit()
            else:
                print("   ERROR: Sudoku format is incorrect!!! (Try to do a 9x9 table separated with spaces)")
                exit()
    else:
        print("   ERROR: Sudoku format is incorrect!!! (Try to do a 9x9 table separated with spaces)")
        exit()


def isSudokuCorrect(oList):
    #we have to know if it's ok the length of the sudoku table
    if(goodLength(oList) == True):
        sameVertical = 0
        sameHorizontal = 0
        #then, I scroll the list
        for i in range(len(oList)):
            #next, I'm through the lists inside the original list
            for j in range(len(oList[i])):
                n = oList[i][j]
                """
                    In this for, I make sure that there is not the same number in the Horizontal line (or the same list), 
                    and then if it's true I add 1 to the Horizontal value (it might be 81 at the end)
                """
                for x in range(len(oList[i])):
                    if(n == oList[i][x]): sameHorizontal+=1
                #Now, it's the same but scrolling the Vertical list (but in the same column place)
                for z in range(len(oList)):
                    if(n == oList[z][j]): sameVertical+=1
        if(sameHorizontal == 81 and sameVertical == 81): return "Correct"
        else: return "Incorrect"

#we get the path and add the name of the file
path = "Sudoku.in"
#opening the file
file = open(path,"r")
#and now, we made a list with all the lines of the file
fileTextArray = file.readlines()

#I map the list doing a new one but filtering the exceptions (like spaces or letters)
sudoku = list(map(charException,fileTextArray))

#Finally, print the result
print(isSudokuCorrect(sudoku))



