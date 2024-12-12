from collections import Counter

def common(file_name):
    left, right = [], []
    with open(f"{file_name}.txt", "r") as file:
        contents = file.read()
        s = contents.replace("\n", "   ").split("   ")
        for i, num in enumerate(s):
            if i % 2 == 0:
                left.append(int(num))
            else:
                right.append(int(num))
        
        left.sort()
        right.sort()
    return left, right

def first():
    left, right = common("first")
    total = 0
    for i in range(len(left)):
        diff = abs(left[i] - right[i])
        total += diff

    print(total)

def second():
    left, right = common("second")
    right_mapper = dict(Counter(right))
    total = 0
    for num in left:
        product = 1
        if right_mapper.get(num, False):
            product = num * right_mapper[num]
        else:
            product = 0
        total += product
    
    print(total)

first()
second()
