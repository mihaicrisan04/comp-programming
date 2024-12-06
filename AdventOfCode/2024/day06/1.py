import sys

sys.setrecursionlimit(10000)

# with open("input.txt") as f:
with open("test.txt") as f:
    lines = f.readlines()

a = [[c for c in line.strip()] for line in lines]
n = len(a)

# print(a)

d = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^' 
}

def nextMove(i, j, c):
    if c == '^':
        return i-1, j
    if c == '>':
        return i, j+1
    if c == 'v':
        return i+1, j
    if c == '<':
        return i, j-1

def inMatrix(i, j):
    return 0 <= i < n and 0 <= j < n 

def path(i, j, c):
    if not inMatrix(i, j):
        return

    a[i][j] = 'X'

    ni, nj = nextMove(i, j, c)
    if inMatrix(ni, nj):
        if a[ni][nj] == '#':
            ni, nj = nextMove(i, j, d[c])
            path(ni, nj, d[c])
        else:
            path(ni, nj, c)


def start():
    for i in range(n):
        for j in range(n):
            if a[i][j] == '^':
                path(i, j, '^')
                return 

def solve():
    start()

    k = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] == 'X':
                k += 1

    print(k)

solve()