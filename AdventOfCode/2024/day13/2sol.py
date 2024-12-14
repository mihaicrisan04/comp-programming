import re
import math
import sympy
import z3

# with open('test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    data = [line for line in f.read().splitlines() if len(line)]

# find an n, m pair that satisfies the equation
# a.x * n + b.x * m = t.x
# a.y * n + b.y * m = t.y
# return n * 3 + m * 1
# note to self: look into the diophantine equation, the bezout's identity and the extended euclidean algorithm

class ClawMachine:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

def cost(a, b, t):
    t1 = z3.Int('t1')
    t2 = z3.Int('t2')
    S = z3.Solver()
    S.add(t1 > 0)
    S.add(t2 > 0)
    S.add(a.x * t1 + b.x * t2 == t.x)
    S.add(a.y * t1 + b.y * t2 == t.y)
    if S.check() == z3.sat:
        m = S.model()
        return m.eval(3*t1 + t2).as_long()
    return 0

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