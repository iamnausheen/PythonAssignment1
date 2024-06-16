# Prompt user for a number
n = int(input("Enter a number: "))
d = len(str(n))

# Calculate sum of it's digits
num = 0
sum = 0
for i in range(0, d, 1):
    num = n%10
    n = int(n/10)
    sum = sum + num
print("The sum of the digits is {}".format(sum))
