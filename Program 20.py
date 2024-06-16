# Prompting user for numbers
list_num = []
num = int(input("Enter number 1: "))
list_num.append(num)
i = 2
while (True):
    choice = input("Another number? (Yes/No) ")
    if (choice.upper() == "NO" or choice.upper() == 'N' ):
        break
    else:
        num = int(input("Enter number {}: ".format(i)))
        list_num.append(num)
        i = i+1

# Calculating sum
sum = 0
for i in list_num:
    sum+=i

print("SUM = ", sum)