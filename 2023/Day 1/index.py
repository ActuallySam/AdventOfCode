def solve():
    with open("first.txt", "r") as file:
        contents = file.read()
        nums = contents.split("\n")
        total, s = 0, ""
        for num in nums:
            for ch in num:
                if "0" <= ch <= "9":
                    s += ch
            total += int(s[0]) * 10 + int(s[-1])
            s = ""
        
        print(total)

solve()