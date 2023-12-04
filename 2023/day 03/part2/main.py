file = open("input.txt","r")

#see if you can compare in every direction

lines = file.readlines()
numLines = len(lines)
lenOfLine = len(lines[0].strip())

def compareAroundHardCoded(i , j): #8 slots adjacent to my slot
    s = '[@_!#$%^&*()<>?/\|}{~:]+-=' #check if im missing something here
    #---------------------------------------------
    if (i != 0):            #not in the first line
        if (lines[i-1][j] in s): #in the upper slot
            return True
        if (j != 0):
            if (lines[i-1][j-1] in s): # in the upper left slot 
                return True
        if (j != (lenOfLine-1)):
            if (lines[i-1][j+1] in s): # in the upper right slot
                return True
    #----------------------------------------------        
    if (i != (numLines-1)): #not in the last line 
        if (lines[i+1][j] in s): # in the lower slot
            return True
        if (j != 0):
            if (lines[i+1][j-1] in s): # in the lower left slot 
                return True
        if (j != (lenOfLine-1)):
            if (lines[i+1][j+1] in s): # in the lower right slot
                return True
    #----------------------------------------------
    if (j != 0):
        if (lines[i][j-1] in s): #in the left slot
            return True
    if (j != (lenOfLine-1)):
        if (lines[i][j+1] in s): #in the right slot
            return True


def compareAround(i , j):
    dx = [-1, -1,-1, 0, 0, 0, 1, 1, 1]
    dy = [-1,  0, 1,-1, 0, 1,-1, 0, 1]
    s = '*' 
    for x in range(9):
        for y in range(9):
            if ((not (i + dx[x] < 0)) and (not (j + dy[y] < 0)) and \
                (not (j + dy[y] >= lenOfLine)) and \
                (not (i + dx[x] >= numLines)) and (not (dx[x]==0 and dy[y]==0))):
                if (lines[i+dx[x]][j+dy[y]] in s):
                    return True
    return False

i = 0
j = 0
total = 0
num = 0
addFlag = False

print("len of line " + str(lenOfLine))

while(i < numLines):
    j = 0
    while (j < lenOfLine):
        num = 0
        addFlag = False
        if ((j < lenOfLine) and (lines[i][j].isdigit())):
            while ((j < lenOfLine) and (lines[i][j].isdigit())):
                if (compareAround(i, j)):
                    addFlag = True
                num = num*10 + int(lines[i][j])
                j += 1
        else:
            j += 1
        if (addFlag):
            total += num
    i += 1

print("the total is : "+ str(total))

#idea for part2 just 