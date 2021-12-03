with open("./input.txt") as file:
    lines = file.readlines()

transposed = [""] * len(lines[0].strip())

for line_number, line in enumerate(lines):
    line = line.strip()
    for index, bit in enumerate(line):
        transposed[index] += bit

gamma = ""
epsilon = ""

for binary in transposed:
    zeros = 0
    ones = 0
    for char in binary:
        if char == "0":
            zeros += 1
        else:
            ones += 1

    if zeros > ones:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma * epsilon)
