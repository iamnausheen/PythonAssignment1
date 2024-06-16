# Prompt user for how many numbers to generate
n = int(input("How many numbers to generate? "))

# Generate sequence iteratively
# Each element of the fibonacci sequence is the sum of it's previous 2 elements
fibonacci_sequence = [0, 1]
for i in range(2, n, 1):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
print(fibonacci_sequence)
