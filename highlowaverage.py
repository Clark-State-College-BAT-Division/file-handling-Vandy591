#For this assignment use the numbers.txt file.
#A different numbers.txt will be used for grading.
#Read in all the numbers. Display the following information:
#How many numbers in the file
#Total of all the number
#Average
#Highest number
#Lowest number
#Correct answers for the included file: 15

file = open("numbers.txt")
count = 0
total = 0
highest = 0
lowest = 999999
for line in file:
    number = int(line)
    count += 1
    total += number
    if number > highest:
        highest = number
    if number < lowest:
        lowest = number
average = total / count
print("count:", count)
print("total:", total)
print("average:", average)
print("highest:", highest)
print("lowest:", lowest)
file.close()