
with open("input.txt") as f:
# with open("test.txt") as f:
    lines = f.readlines()

a = [[c for c in line.strip()] for line in lines]
n = len(a)


def nextMove(i, j, d):
    if d == 0: return i-1, j # ^
    if d == 1: return i, j+1 # >
    if d == 2: return i+1, j # v
    if d == 3: return i, j-1 # <

def inMatrix(i, j): return 0 <= i < n and 0 <= j < n 

def isCycle():
    visited = set()
    i, j = guard
    d = 0 # direction of guard
    visited.add((i, j, d))

    while True:
        ni, nj = nextMove(i, j, d)

        if not inMatrix(ni, nj): return False

        while a[ni][nj] == '#':
            d = (d + 1) % 4
            ni, nj = nextMove(i, j, d)

        if (ni, nj, d) in visited: return True

        visited.add((ni, nj, d))
        i, j = ni, nj


# get guard position
for i in range(n):
    for j in range(n):
        if a[i][j] == '^':
            guard = (i, j)

sol = 0
for i in range(n):
    for j in range(n):
        if a[i][j] != '#' and a[i][j] != '^':
            a[i][j] = '#'
            if isCycle():
                sol += 1
            a[i][j] = '.'

        
print(sol)