from shlex import join

punctuation = [',', '.', '?', ';', ':', '!']

text_before = input("Enter text from which to remove punctuation marks: ")

list0 = list(text_before)

for i in list0:
    for j in punctuation:
        if(i == j):
            list0.remove(i)

text_after =''.join(map(str, list0))
print("AFTER: ", text_after)

