from collections import defaultdict, Counter

def get_new_stones(stones):
    new_stones = []
    for i, stone in enumerate(stones):
        stone_length = len(stone)
        if int(stone) == 0:
            new_stones.append("1")
        elif stone_length % 2 == 0:
            first_half = stone[0:stone_length//2]
            second_half = stone[stone_length//2:]
            new_stones.append(str(int(first_half)))
            new_stones.append(str(int(second_half)))
        else:
            new_stones.append(str(int(stone) * 2024))
    return new_stones

def solve_part1(stones):
    for i in range(25):
        stones = get_new_stones(stones)
    print(len(stones))


def get_new_stone_counts(stone_counts):
    new_counts = Counter()
    for stone, count in stone_counts.items():
        stone_value = int(stone)
        if stone_value == 0:  # Stone is 0
            new_counts["1"] += count
        elif len(stone) % 2 == 0:  # Even-length stone
            mid = len(stone) // 2
            left_half = stone[:mid].lstrip("0") or "0"
            right_half = stone[mid:].lstrip("0") or "0"
            new_counts[left_half] += count
            new_counts[right_half] += count
        else:  # Odd-length stone
            multiplied_value = str(stone_value * 2024)
            new_counts[multiplied_value] += count
    return new_counts

def solve_part2(stones):
    stone_counts = Counter(stones)
    for _ in range(75):
        stone_counts = get_new_stone_counts(stone_counts)
    print(sum(stone_counts.values()))

def solve():
    with open("input.txt", "r") as file:
        contents = file.read()
        initial_stones = contents.split(" ")

        solve_part1(initial_stones)
        solve_part2(initial_stones)

solve()