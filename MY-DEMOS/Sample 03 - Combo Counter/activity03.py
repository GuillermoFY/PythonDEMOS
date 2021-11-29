
#taking a string typed by command line
st = input("Type a string: ")

#now, we do a new function
def comboNum(st):
    
    #First, we are using the function count() that return the number of times that the value 01, ABC and HO appears in the string parameter
    comboCounter = 0
    comboCounter += st.count("01")
    comboCounter += st.count("ABC")
    comboCounter += st.count("HO")
      
    #we are saving all the letters in an array for searching if there is some 00 combo
    letters = list(st)
    
    """
        now, we go through the list and we see if there is some 00 combos, if there is some, 
        the comboCounter will +1 and the zeroDouble will pass to be a 0 because if there is some 000 the counter will be 2 (000=2)
    """
    zeroDouble = ""
    for i in letters:
        zeroDouble += i
        if(i!="0"):
            zeroDouble = ""
        if(zeroDouble=="00"):
            comboCounter+=1
            zeroDouble = "0"
            
    
    return comboCounter

print("Counter= " + str(comboNum(st)))