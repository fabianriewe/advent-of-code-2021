with open("./input.txt") as file:
    commands = list(map(lambda l: l.strip().split(" "), file.readlines()))

# Exercise 1
depth = 0
horizontal = 0

for [direction, amount] in commands:
    if direction == "forward":
        horizontal += int(amount)
    elif direction == "up":
        depth -= int(amount)
    elif direction == "down":
        depth += int(amount)

print(depth * horizontal)
# 2117664

# Exercise 2
aim = 0
depth = 0
horizontal = 0

for [direction, amount] in commands:
    if direction == "forward":
        horizontal += int(amount)
        depth += aim * int(amount)
    elif direction == "up":
        aim -= int(amount)
    elif direction == "down":
        aim += int(amount)

print(depth * horizontal)
# 2073416724
