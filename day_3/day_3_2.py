from typing import List

with open("./input.txt") as file:
    lines: List[str] = list(map(lambda l: l.strip(), file.readlines()))

bit_index = 0
while len(lines) > 1:
    print(lines)
    print(bit_index)
    zeros = 0
    ones = 0
    for line in lines:
        selected_bit = line[bit_index]

        if selected_bit == "0":
            zeros += 1
        else:
            ones += 1

    if zeros > ones:
        least_common = "0"
    else:
        least_common = "1"

    kept_lines = []
    for line in lines:
        if line[bit_index] == least_common:
            kept_lines.append(line)

    lines = kept_lines
    bit_index += 1

print(lines)
oxygen_generator_rating = int(lines[0], 2)
print(oxygen_generator_rating)

with open("./input.txt") as file:
    lines: List[str] = list(map(lambda l: l.strip(), file.readlines()))

bit_index = 0
while len(lines) > 1:
    print(lines)
    print(bit_index)
    zeros = 0
    ones = 0
    for line in lines:
        selected_bit = line[bit_index]

        if selected_bit == "0":
            zeros += 1
        else:
            ones += 1

    if zeros <= ones:
        least_common = "0"
    else:
        least_common = "1"

    kept_lines = []
    for line in lines:
        if line[bit_index] == least_common:
            kept_lines.append(line)

    lines = kept_lines
    bit_index += 1

print(lines)
co2_scrubber_rating = int(lines[0], 2)
print(co2_scrubber_rating)
life_supporting_rate = oxygen_generator_rating * co2_scrubber_rating
print(life_supporting_rate)