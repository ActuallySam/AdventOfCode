def is_safe_sequence(sequence):
    if all(sequence[i+1] - sequence[i] >= 1 and sequence[i+1] - sequence[i] <= 3 for i in range(len(sequence)-1)):
        return True
    
    if all(sequence[i] - sequence[i+1] >= 1 and sequence[i] - sequence[i+1] <= 3 for i in range(len(sequence)-1)):
        return True
    
    return False

def solve_part1(reports):
    total = sum(1 for report in reports if is_safe_sequence(report))
    print("Part 1:", total)

def solve_part2(reports):
    total = 0
    for report in reports:
        if is_safe_sequence(report):
            total += 1
            continue

        for i in range(len(report)):
            test_arr = report[:i] + report[i+1:]
            if is_safe_sequence(test_arr):
                total += 1
                break
    print("Part 2:", total)

def solve():
    with open("first.txt", "r") as file:
        contents = file.read()
        nums = contents.split("\n")
        reports = []
        for num in nums:
            temp_arr = num.split(" ")
            int_arr = [int(x) for x in temp_arr]
            reports.append(int_arr)
        
        solve_part1(reports)
        solve_part2(reports)

solve()
