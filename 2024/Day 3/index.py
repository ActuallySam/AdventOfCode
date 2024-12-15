import re

def first(contents, pattern):
    total = 0
    matches = re.findall(pattern, contents)
    total = sum(int(a) * int(b) for a, b in matches)
    print(total)

def second(contents, pattern):
    enabled, total = True, 0
    control_pattern = r"(do\(\)|don't\(\))"
    instructions = re.findall(fr"{control_pattern}|{pattern}", contents)
    for instruction in instructions:
        if instruction[0]:
            if instruction[0] == "do()":
                enabled = True
            elif instruction[0] == "don't()":
                enabled = False
        elif enabled:
            a, b = instruction[1], instruction[2]
            total += int(a) * int(b)
    print(total)

def solve():
    with open("input.txt", "r") as file:
        contents = file.read()
        pattern = r"mul\((\d+),(\d+)\)"
        first(contents, pattern)
        second(contents, pattern)

solve()