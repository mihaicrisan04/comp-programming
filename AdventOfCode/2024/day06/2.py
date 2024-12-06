import sys
from typing import Any

sys.setrecursionlimit(100000)

# with open("input.txt") as f:
with open("test.txt") as f:
    lines = f.readlines()

a = [[c for c in line.strip()] for line in lines]
n = len(a)

path: set[tuple[int, int]] = set()
k = 0

d = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^' 
}
b = {
    '^': 'N',
    '>': 'E',
    'v': 'S',
    '<': 'V' 
}

def printMat():
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
        print()
    print()

def printK(ni, nj):
    for i in range(n):
        for j in range(n):
            if i == ni and j == nj:
                print('O', end=' ')
            else:
                print(a[i][j], end=' ')
        print()
    print()

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

def findPath(i, j, c):
    global k

    if not inMatrix(i, j): return

    a[i][j] = b[c]
    path.add((i, j))

    # printMat()

    ni, nj = nextMove(i, j, c)
    if inMatrix(ni, nj):
        if a[ni][nj] == '#':
            while a[ni][nj] == '#':
                ni, nj = nextMove(i, j, d[c])
            findPath(ni, nj, d[c])
        else:
            findPath(ni, nj, c)




def start():
    for i in range(n):
        for j in range(n):
            if a[i][j] == '^':
                findPath(i, j, '^')
                return 


start()
printMat()
print(k)

for (x, y) in path:
    print(x, y)
