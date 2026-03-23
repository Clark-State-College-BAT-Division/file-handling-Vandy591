file = open("words.txt")
count = 0
for line in file:
    word = line.strip()
    if word == word[::-1]:
        print(word)
        count += 1
print("Palindrome count:", count)
file.close()