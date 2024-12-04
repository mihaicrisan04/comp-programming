
with open('input.txt') as f:
# with open('test.txt') as f:
    lines = f.readlines()

a = [[x for x in line.strip()] for line in lines]
n = len(a)

di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

letters = 'XMAS'

def inMat(i, j):
    return 0 <= i < n and 0 <= j < n

def xmas(i, j):
    v = [0] * 8
    for d in range(8):
        for k in range(1, 4):
            ni = i + di[d] * k
            nj = j + dj[d] * k
            if not inMat(ni, nj):
                break
            if a[ni][nj] == letters[k]:
                v[d] += 1
    return sum([1 for x in v if x == 3])

def countXmas():
    count = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] == 'X':
                count += xmas(i, j)
    return count

print(countXmas())
