# Prompting user for numbers
list0 = []
element = (input("Enter an element: "))
list0.append(element)
while (True):
    choice = input("Another one? (Yes/No) ")
    if (choice.upper() == "NO" or choice.upper() == 'N' ):
        break
    else:
        element = input("Enter an element: ")
        list0.append(element)

count = input("Which element to count? ")
n = 0
for i in list0:
    if(i.upper() == count.upper()):
        n+=1
print("Appeared {} times".format(n))




