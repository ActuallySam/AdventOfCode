from collections import defaultdict

def solve_part1():
    pass

def solve_part2():
    pass

class Dependencies:
    def __init__(self):
        self.before_set = set()
        self.after_set = set()

def verify_index(ind, line, n, conditions):
    l, r = ind - 1, ind + 1
    target = line[ind]
    while l >= 0:
        cand = line[l]
        if cand in conditions[target].after_set:
            return False
        l -= 1
    while r < n:
        cand = line[r]
        if cand in conditions[target].before_set:
            return False
        r += 1
    return True

def solve():
    with open("input.txt", "r") as file:
        contents = file.read()
        rules_and_syntaxes = contents.split("\n\n")
        rules = rules_and_syntaxes[0].split("\n")
        syntaxes = rules_and_syntaxes[1].split("\n")

        conditions = defaultdict(Dependencies)
        for rule in rules:
            prev, next = rule.split("|")
            conditions[prev].after_set.add(next)
            conditions[next].before_set.add(prev)

        res = 0
        invalid_lines = []
        for index, syntax in enumerate(syntaxes):
            line = syntax.split(",")
            n = len(line)
            valid = True
            for i in range(n):
                if verify_index(i, line, n, conditions) is False:
                    valid = False

            if valid:
                mid_element = line[n // 2]
                res += int(mid_element)
            else:
                invalid_lines.append(line)

        print(res)

        final_res = 0
        for line in invalid_lines:
            res_arr = []
            elements = set(line)
            while len(elements) > 0:
                for elem in elements:
                    cand_place = True
                    for comparison in elements:
                        if elem == comparison:
                            continue

                        if elem in conditions[comparison].after_set:
                            cand_place = False
                            break
                
                    if cand_place:
                        res_arr.append(elem)
                        elements.remove(elem)
                        break
        
            final_res += int(res_arr[len(res_arr) // 2])

        print(final_res)

solve()