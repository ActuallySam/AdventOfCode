import re

def solve_first(arr):
    total, s = 0, ""
    for line in arr:
        for ch in line:
            if "0" <= ch <= "9":
                s += ch
        total += int(s[0]) * 10 + int(s[-1])
        s = ""
    print(total)


def solve_second(arr):
    total = 0
    regex_pattern = r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))"
    word_mapper = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    for line in arr:
        word_matches = re.findall(regex_pattern, line)
        integer_matches = [
            word_mapper[match.lower()] if match.lower() in word_mapper else match for match in word_matches
        ]
        if len(integer_matches) > 0:
            total += int(integer_matches[0] + integer_matches[-1])
    
    print(total)

def solve():
    with open("first.txt", "r") as file:
        contents = file.read()
        arr = contents.split("\n")
        
        solve_first(arr)
        solve_second(arr)

solve()