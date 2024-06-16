# Taking text input from user
text0 = input("Title: ")

text1 = list(text0)
text1[0] = text1[0].upper()

for i in range(1, len(text1), 1):
    if((text1[i - 1]) == ' '):
        text1[i] = text1[i].upper()

change_text = ''.join(map(str, text1))
print(change_text)