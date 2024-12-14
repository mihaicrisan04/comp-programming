import re
import math

# with open('test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    data = [line for line in f.read().splitlines() if len(line)]

class ClawMachine:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

# find an n, m pair that satisfies the equation
# a.x * n + b.x * m == t.x 
# a.y * n + b.y * m == t.y
# return n * 3 + m

# apply Cramers determinant formula to find n, m
# n = (det1 / det) and m = (det2 / det)
# n, m are valid if they are integers and n, m >= 0

def cost(a, b, t):
    det = a.x * b.y - a.y * b.x
    if det == 0: return 0 # no solution exists

    det1 = t.x * b.y - t.y * b.x
    det2 = a.x * t.y - a.y * t.x

    n = det1 / det
    m = det2 / det

    if n < 0 or m < 0 or int(n) != n or int(m) != m: return 0 # only integer solutions which are >= 0 are valid

    return int(3 * n + m)


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
        t.x += 10000000000000
        t.y += 10000000000000

        sol += cost(a, b, t)

    print(sol)


solve()