#which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

blue_limit  = 14
green_limit = 13
red_limit   = 12

file = open('input.txt', 'r')
lines = file.readlines()
size = len(lines)
i = 0
num_cubes = 0
result = 0

while (i < size):
    gameAllowed = True #its a flag that indicates if the game is allowed or not 
    #print(lines[i]) #for debugging
    gameSets = lines[i].split(':')
    #print(gameSets[0])
    sizeSet = len(gameSets[1])
    j = 0
    while (j < sizeSet):
        #print(gameSets[1][j] , end='') #end ='' is to avoid the new line
        if (gameSets[1][j].isdigit()):
            while(gameSets[1][j].isdigit()):
                num_cubes = num_cubes*10 + int(gameSets[1][j])
                j += 1
            print ("the number of cuber is: " + str(num_cubes)) #DEBUG number of cubes with a specific color
            if (gameSets[1][j + 1] == 'r' and num_cubes > red_limit) or \
                (gameSets[1][j + 1] == 'g' and num_cubes > green_limit) or \
                (gameSets[1][j + 1] == 'b' and num_cubes > blue_limit):
                gameAllowed = False
            num_cubes = 0
        else:
            j += 1
    print (gameAllowed) #prints if the game is allowed of not
    if (gameAllowed):
        result = result + (i+1) 
    i += 1
print ('\n')
print ("the result is : "+ str(result)) #result