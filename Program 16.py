# Prompting user for a string
str0 = input("Enter something: ")
repetition = False
for i in range(0, len(str0), 1):
    count = 0
    for k in range(0, i, 1):
        repetition = False
        if str0[i] == str0[k]:
            repetition = True
    for j in range(i, len(str0), 1):
        if repetition == True:
            break
        if str0[i] == str0[j]:
            count += 1
    if repetition == False:
        print(str0[i], ":", count)





