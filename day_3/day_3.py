with open("./input.txt") as file:
    lines = list(map(lambda l: l.strip(), file.readlines()))

transposed = [""] * len(lines[0])

for line in lines:
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

# revision 2
gamma = ""
epsilon = ""

for bit_index in range(len(lines[0])):
    zeros = 0
    ones = 0
    for line in lines:
        if line[bit_index] == "0":
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
