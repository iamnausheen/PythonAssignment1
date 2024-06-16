# Prompt user for birth year
birth_year = int(input("What is your birth year? "))
this_year = input("Has your birthday already come this year? ")
current_year = 2024
# Calculate age
while (True) :
    if (this_year.upper() == "YES" or this_year.upper() == 'Y'):
        Age = current_year - birth_year
        break
    elif (this_year.upper() == "NO" or this_year.upper == "N"):
        Age = current_year - birth_year - 1
        break
    else :
        pass
print("Age: ", Age)