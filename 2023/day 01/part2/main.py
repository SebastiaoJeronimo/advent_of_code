##need to find the first and last digit of a line and add it to the result
file = open("input.txt", "r") #open the file
# print(file.readline())

numberWord = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def checkIfNumberWord(word):
    for i in range(len(numberWord)):
        wordLen = len(word)
        if ((not (wordLen < len(numberWord[i]))) and (word == numberWord[i] or word.find(numberWord[i]) != -1)):
            return i
    return -1

result = 0
line = file.readline()

while line != "":
    i = 0
    first_digit = -1
    last_digit = -1

    print(line)
    while i < len(line):
        if line[i].isdigit():
            if first_digit == -1:
                first_digit = int(line[i])
            last_digit = int(line[i])
            i += 1
        elif line[i].isalpha():
            word = ""
            while i < len(line) and line[i].isalpha():
                if len(word) < 5:
                    word += line[i]
                else:
                    word = word[1:5] + line[i]
                num = checkIfNumberWord(word)
                if num != -1:
                    if first_digit == -1:
                        first_digit = num
                    last_digit = num
                i += 1
        else:
            i += 1

    print("the first digit is: " + str(first_digit))
    print("the last digit is: " + str(last_digit))
    line = file.readline()
    result += (first_digit * 10) + last_digit

file.close() # close the file
print("the result is: " + str(result))
