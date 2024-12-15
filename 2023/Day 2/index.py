
def solve_first():
    pass

def solve_second():
    pass

def solve():
    with open("first.txt", "r") as file:
        contents = file.read()
        arr = contents.split("\n")
        
        solve_first(arr)
        solve_second(arr)

solve()