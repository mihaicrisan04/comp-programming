import re

# with open('test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    data = [line for line in f.read().splitlines() if len(line)]



class ClawMachine:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

def cost(a, b, t):
    # a.x * n + b.x * m = t.x
    # find an n, m pair that satisfies the equation
    # a.y * n + b.y * m = t.y
    # return n * 3 + m * 1

    pairs = []

    for n in range(0, 100):
        for m in range(0, 100):
            if a.x * n + b.x * m == t.x and a.y * n + b.y * m == t.y:
                pairs.append((n, m))
    
    min_cost = 0
    for n, m in pairs:
        cost = n * 3 + m * 1
        if min_cost == 0 or cost < min_cost:
            min_cost = cost

    return min_cost




def solve():
    sol = 0
    for i in range(0, len(data), 3):
        A = data[i]
        B = data[i+1]
        T = data[i+2]

        pattern = r'X\+(\d+), Y\+(\d+)'
        a = ClawMachine(*re.findall(pattern, A)[0])
        b = ClawMachine(*re.findall(pattern, B)[0])

        pattern = r'X\=(\d+), Y\=(\d+)'
        t = ClawMachine(*re.findall(pattern, T)[0])

        sol += cost(a, b, t)

    print(sol)


solve()