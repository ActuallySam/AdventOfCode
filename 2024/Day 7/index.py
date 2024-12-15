from itertools import product

def solve_part1(lines):
    total_sum = 0
    for line in lines:
        # Divide the total and numbers into left and right sections
        sections = line.split(": ")
        total = int(sections[0])
        numbers_list = sections[1].split(" ")
        numbers_list = [int(x) for x in numbers_list]
        total_sum += calculate_sum(total, numbers_list)
    print(total_sum)

def calculate_sum(total, nums):
    max_sum = 0
    operations_combinations = product("+*|", repeat=len(nums) - 1)

    def calculate_expression(operation):
        calculate_val = nums[0]
        for i, op in enumerate(operation):
            if op == "+":
                calculate_val += nums[i + 1]
            elif op == "*":
                calculate_val *= nums[i + 1]
            # Where op == "|"
            # Comment else block to get part 1 solution
            else:   
                calculate_val = int(str(calculate_val) + str(nums[i + 1]))
        return calculate_val

    for ops in operations_combinations:
        if calculate_expression(ops) == total:
            max_sum += total
            break
    return max_sum


def solve_part2():
    pass

def solve():
    with open("input.txt", "r") as file:
        contents = file.read()
        lines = contents.split("\n")
        solve_part1(lines)

solve()