# Prompting user for a number

n = int(input("Number: "))

# Calculating factorial

y = 1

for i in range(1, n + 1, 1):
     y *= i

# Printing factorial
print("Factorial of",n, "is", y)
