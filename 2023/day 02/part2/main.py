#which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

#print (blue_min) 
#print (green_min)
#print (red_min)

file = open('input.txt', 'r')
lines = file.readlines()
size = len(lines)
i = 0
result = 0
num_cubes = 0


while (i < size):
    gameSets = lines[i].split(':')
    sizeSet = len(gameSets[1])
    blue_min  = 0
    green_min = 0
    red_min   = 0
    j = 0

    print ("Game number : "+ str(i+1))
    while (j < sizeSet):
        if (gameSets[1][j].isdigit()):
            while(gameSets[1][j].isdigit()):
                num_cubes = num_cubes*10 + int(gameSets[1][j])
                j += 1
            print ("the number of cuber is: " + str(num_cubes)) #DEBUG number of cubes with a specific color
            if (gameSets[1][j + 1] == 'r' and num_cubes > red_min):
                red_min = num_cubes
            elif (gameSets[1][j + 1] == 'g' and num_cubes > green_min):
                green_min = num_cubes
            elif (gameSets[1][j + 1] == 'b' and num_cubes > blue_min):
                blue_min = num_cubes
            num_cubes = 0
        else:
            j += 1
    result = result + (red_min * green_min * blue_min)
    i += 1
print ('\n')
print ("the result is : "+ str(result)) #result
