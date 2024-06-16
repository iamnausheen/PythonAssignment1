# Prompt user for string and prefix and suffix
checking_string = input("Enter string to check - ")
prefix = input("Enter prefix to check for - ")
suffix = input("Enter suffix to check for - ")

checking_list = [prefix, suffix]

# Checking for presence of prefix and suffix

for i in checking_list:
    check = i.upper() in checking_string.upper()
    if (check == True):
        print(i, "Found")
    else :
        print(i, "Not found")



