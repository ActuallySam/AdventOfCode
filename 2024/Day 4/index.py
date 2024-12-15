def part_1(rows, cols, grid):
    target, target_len = "XMAS", 4
    total = 0
    directions = [
        (0, 1),  # right
        (0, -1), # left
        (1, 0),  # bottom
        (-1, 0), # top
        (1, 1),  # diag bottom-right
        (-1, -1),# diag top-left
        (1, -1), # diag bottom-left
        (-1, 1)  # diag top-right
    ]
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def find_word(start_x, start_y, dx, dy):
        for i in range(target_len):
            x = start_x + i * dx
            y = start_y + i * dy
            if not is_valid(x, y) or grid[x][y] != target[i]:
                return False
        return True

    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if find_word(x, y, dx, dy):
                    total += 1

    print(total)

def part_2(rows, cols, grid):
    total = 0
    directions = [
        [-1, -1],
        [-1, 1],
        [1, 1],
        [1, -1]
    ]

    for row in range(1, rows-1):
        for col in range(1, cols-1):
            if grid[row][col] == "A":
                s = ""
                for delrow, delcol in directions:
                    nrow, ncol = row + delrow, col + delcol
                    s += grid[nrow][ncol]
                if s in {"SSMM", "MMSS", "SMMS", "MSSM"}:
                    total += 1
    
    print(total)


def solve():
    with open("input.txt", "r") as file:
        contents = file.read()
        grid = contents.split("\n")
        rows, cols = len(grid), len(grid[0])
        part_1(rows, cols, grid)
        part_2(rows, cols, grid)

solve()