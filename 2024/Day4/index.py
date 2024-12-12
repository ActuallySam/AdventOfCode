from itertools import permutations

def solve():
    with open("example.txt", "r") as file:
        contents = file.read()
        nums = contents.split("\n")
        rows = []
        total = 0
        for num in nums:
            temp_arr = num.split("\n")
            line = temp_arr[0]
            # rows.append(temp_arr[0])
            word_permutations = set([''.join(p) for p in permutations("XMAS")])
            for i in range(len(line) - 3):
                s = line[i] + line[i + 1] + line[i + 2] + line[i + 3]
                if s in word_permutations:
                    total += 1

            print(total)

solve()