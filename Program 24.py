num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operator = input("Enter operator from : +, -, /, * ")

if (operator == "+"):
    result = num1 + num2
    print("Sum of {} and {} is {}".format(num1, num2, result))
elif (operator == "-"):
    result = num1 - num2
    print("Difference of {} from {} is {}".format(num1, num2, result))
elif (operator == "/"):
    result = num1/num2
    print("Result on dividing {} by {} is {}".format(num1, num2, result))
elif (operator == "*"):
    result = num1*num2
    print("Result on multiplying {} and {} is {}".format(num1, num2, result))
else:
    print("INVALID OPERATION")