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

# Determine maximum

def maximum(list0):
    m = list0[0]
    for j in range(0, len(list0), 1):
        if (list0[j] > m):
            return list0[j]
        elif (list0[j] < m):
            return m
        else:
            pass

# Determine minimum

def minimum(list0):
    n = list0[0]
    for l in range(0, len(list0), 1):
        if (list0[l] < n):
            return list0[l]
        elif (list0[l] > n):
            return n
        else:
            pass

print("MAXIMUM: ", maximum(list_num))
print("MINIMUM: ", minimum(list_num))