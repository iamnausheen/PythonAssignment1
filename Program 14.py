# Prompt user for multi-line input
lines = []

while (True):
    line = input()
    if line:
        lines.append(line)
    else:
        break
# Print multi line input
for i in lines:
    print(i)

