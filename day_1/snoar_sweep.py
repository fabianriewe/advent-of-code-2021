with open("./day_1/input.txt") as file:
    depths = file.readlines()

# parse inputs
depths = list(map(lambda d: int(d.strip()), depths))
increased = 0
previous_depth = depths[0]
# Exercise 1
for depth in depths:
    if depth > previous_depth:
        increased += 1

    previous_depth = depth

print(increased)

# Exercise 2
increased = 0
previous_depth = depths[0] + depths[1] + depths[2]
for i in range(len(depths) - 2):
    summed_depth = depths[i] + depths[i + 1] + depths[i + 2]

    if summed_depth > previous_depth:
        increased += 1

    previous_depth = summed_depth

print(increased)
# 1523
