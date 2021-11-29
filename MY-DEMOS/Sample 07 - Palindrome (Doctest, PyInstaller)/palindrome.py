import sys
import doctest
import os.path

#Getting out the letters that aren't numbers
def charException(n):
    numbers = "123456789"
    ret = []
    for i in range(len(n)):
        if(numbers.find(n[i]) != -1):
            ret.append(int(n[i]))
    return ret  

#Getting the two files (input and output)
if len(sys.argv) != 3:
    print(" ERROR: You have entered one or more than two parameters!!!")
    exit()

ip = sys.argv[1]
op = sys.argv[2]

#Checking if the two files exist
if not os.path.isfile(ip):
    print(" ERROR: File " + ip + " not exists!!!")
    exit()

if not os.path.isfile(op):
    print(" ERROR: File " + op + " not exists!!!")
    exit()

#opening the file input
fileIp = open(ip,"r")
#and now, we made a list with all the lines of the file
fileTextArray = fileIp.readlines()
#I map the list doing a new one but filtering the exceptions (like spaces or letters)
numberList = list(map(charException,fileTextArray))

#Now, we are doing the palindrome check function
def isPalindrome(nl):
    #this are the testing with doctest
    """
    >>> isPalindrome([2,3,4,3,2])
    True
    
    >>> isPalindrome([2,2,4,3,2])
    False
    """
    res = False
    #if the length of the list is one it means that there is one number inside of it so it's palindrome 
    if len(nl) <= 1:
        res = True
    else:
        #Now, we are doing a list with the reverse() function that reverses one liss
        rev = nl.copy()
        rev.reverse()
        #and if the list is the same of the reversed list, is palindrome
        if(nl == rev):
            res = True
        else:
            res = False
    return res

#the prime function
def isPrime(nl):
    #tests with doctest
    """
    >>> isPrime([13])
    True
    
    >>> isPrime([14])
    False
    """
    res = False
    #if the length is 0 is not prime (obviously)
    if len(nl) == 0:
        res = False 
    elif len(nl) >= 1:
        """now, we are getting the numbers (if the lengths is more than 1), 
            the numbers at the array will paste to do one single number.
        """
        number = ""
        for n in nl:
            number += str(n)
        number = int(number)
        #here, we are doing a recursive prime function
        def p(number, div = 2):
            if div >= number:
                return True
            elif number % div != 0:
                return p(number, div+1)
            else:
                return False
        res = p(number)
    return res
    
#doctest.testmod() (the test)

#Finally we are using the functions to get the numbers which are the both and the numbers that ar pal. and pri.
palipri = []
pal = 0
pri = 0

for number in numberList:
    pali = isPalindrome(number)
    prim = isPrime(number)
    if pali == True:
        pal += 1
    if prim == True:
        pri += 1
    if pali == True and prim == True:
        palipri.append(number)

#finally we open the output file and inserting the data
fileOp = open(op,"w")
fileOp.write("Palindrome numbers: " + str(pal) + "\n" + "Prime numbers: " + str(pri)+ "\n")
for number in palipri:
    num = ""
    for n in number:
        num += str(n)

    fileOp.write(num + "\n")

