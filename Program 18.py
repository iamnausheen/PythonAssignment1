# Prompting for strings
str0 = input("First word: ")
str1 = input("Second word: ")

if len(str0) == len(str1):
    count = 0
    for i in str0.upper():
        if i in str1.upper():
            count += 1
    if count == len(str0):
        print("Anagrams")
    else:
        print("Not Anagrams")
else :
    print("Not Anagrams")