##need to find the first and last digit of a line and add it to the result
file = open("input.txt", "r") #open the file
# print(file.readline())

result = 0
line = file.readline()

while (line != ""):
    i = 0
    first_digit = -1
    last_digit = -1

    print(line)
    while (i < len(line)):
        if (line[i] >= '0' and line[i] <= '9'):
            if first_digit == -1:
                first_digit = int(line[i])
            last_digit = int(line[i])
        i += 1
    #print("the first digit is: " + str(first_digit))
    #print("the last digit is: " + str(last_digit))
    line = file.readline()
    result = result + ((first_digit*10) + last_digit) 
    #print("the value of the result until here is: " + str(result))

file.close() #close the file
print ("the result is: " + str(result))