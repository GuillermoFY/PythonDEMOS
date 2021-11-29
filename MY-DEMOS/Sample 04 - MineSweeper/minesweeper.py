mines = [[0,-1,0,0,-1],
        [-1,0,-1,0,0],
        [0,0,0,-1,-1]]

mines2 = [[0,0,-1,0],[0,-1,-1,0]]

#Checking if the length of the lines is ok
xlen = 0
for i in range(len(mines)):
    if i == 0:
        xlen = len(mines[i])
    else:
        line = mines[i]
        if len(line) != xlen:
            print(" ERROR: the length of the lines is not correct.")

def mineCounter(mC):
    m = mC.copy()
    for i in range(len(m)):
        for j in range(len(m[i])):
            counter = 0
            if(m[i][j] != -1):
                if(j == 0): #if is the left column
                    if(i == 0):
                        #count down
                        if(m[i+1][j] == -1): counter+=1
                        #count down + right
                        if(m[i+1][j+1] == -1): counter+=1 
                        #count right
                        if(m[i][j+1] == -1): counter+=1
                    elif(i == (len(m)-1)):
                        #count right
                        if(m[i][j+1] == -1): counter+=1
                        #count up
                        if(m[i-1][j] == -1): counter+=1
                        #count up + right
                        if(m[i-1][j+1] == -1): counter+=1
                    else:
                        #count right
                        if(m[i][j+1] == -1): counter+=1
                        #count up
                        if(m[i-1][j] == -1): counter+=1
                        #count up + right
                        if(m[i-1][j+1] == -1): counter+=1
                        #count down
                        if(m[i+1][j] == -1): counter+=1
                        #count down + right
                        if(m[i+1][j+1] == -1): counter+=1 
                elif(j == len(m[i])-1): #if is the right column
                    if(i == 0): 
                        #count down
                        if(m[i+1][j] == -1): counter+=1
                        #count down + left
                        if(m[i+1][j-1] == -1): counter+=1 
                        #count left
                        if(m[i][j-1] == -1): counter+=1
                    elif(i == (len(m)-1)):
                        #count left
                        if(m[i][j-1] == -1): counter+=1
                        #count up
                        if(m[i-1][j] == -1): counter+=1
                        #count up + left
                        if(m[i-1][j-1] == -1): counter+=1
                    else:
                        #count left
                        if(m[i][j-1] == -1): counter+=1
                        #count up
                        if(m[i-1][j] == -1): counter+=1
                        #count up + left
                        if(m[i-1][j-1] == -1): counter+=1
                        #count down
                        if(m[i+1][j] == -1): counter+=1
                        #count down + left
                        if(m[i+1][j-1] == -1): counter+=1 

                elif(i == 0): #if is the first 
                    if(j == 0): counter = counter
                    elif(j == (len(m[i])-1)): counter = counter
                    else:
                        #count left
                        if(m[i][j-1] == -1): counter+=1
                        #count right
                        if(m[i][j+1] == -1): counter+=1
                        #count down
                        if(m[i+1][j] == -1): counter+=1
                        #count down + left
                        if(m[i+1][j-1] == -1): counter+=1 
                        #count down + right
                        if(m[i+1][j+1] == -1): counter+=1 
                elif(i == (len(m)-1)):
                    if(j == 0): counter = counter
                    elif(j == (len(m[i])-1)): counter = counter
                    else:
                        #count left
                        if(m[i][j-1] == -1): counter+=1
                        #count right
                        if(m[i][j+1] == -1): counter+=1
                        #count up
                        if(m[i-1][j] == -1): counter+=1
                        #count up + left
                        if(m[i-1][j-1] == -1): counter+=1
                        #count up + right
                        if(m[i-1][j+1] == -1): counter+=1
                else:
                    if(j == 0): counter = counter
                    elif(j == (len(m[i])-1)): counter = counter
                    elif(i == 0): counter = counter
                    elif(i == (len(m)-1)): counter = counter
                    else:
                        #count left
                        if(m[i][j-1] == -1): counter+=1
                        #count right
                        if(m[i][j+1] == -1): counter+=1
                        #count up
                        if(m[i-1][j] == -1): counter+=1
                        #count up + left
                        if(m[i-1][j-1] == -1): counter+=1
                        #count up + right
                        if(m[i-1][j+1] == -1): counter+=1
                        #count down
                        if(m[i+1][j] == -1): counter+=1
                        #count down + left
                        if(m[i+1][j-1] == -1): counter+=1 
                        #count down + right
                        if(m[i+1][j+1] == -1): counter+=1
            elif(m[i][j]==-1):
                counter = -1
            
            m[i][j] = counter
    
    return m

#Checking if the counter is going okay
l = mineCounter(mines2)
for line in l:
    print(line)