# Prompting user for string input
text = input("TEXT: ")

# Opening text file
writing_file = open("C:/Users/mcss/PycharmProjects/pythonAssignment1/PythonAssignment_1/Program 5", 'w')

# Printing to the console
print(text,sep = " ",end = "\n", file = writing_file)