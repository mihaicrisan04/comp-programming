
with open('input.txt', 'r') as f:
# with open('test.txt', 'r') as f:
# with open('test2.txt', 'r') as f:
    lines = f.read().splitlines()

n = len(lines[0])
a = [[c for c in line] for line in lines[:n]]
lines = lines[n+1:]
moves = "".join(lines)
ri, rj = 0, 0

di = {
    '^': -1,
    'v': 1,
    '<': 0,
    '>': 0
}
dj = {
    '^': 0,
    'v': 0,
    '<': -1,
    '>': 1
}

def inside(i, j):
    return 1 <= i <= n and 1 <= j <= n

def push(i, j, d):
    while a[i][j] == 'O' and inside(i, j):
        i += di[d]
        j += dj[d]
    if not inside(i, j): return None, None# should not happen though because the border is always #
    if a[i][j] == '#': return None, None
    return i, j


for i in range(n):
    for j in range(n):
        if a[i][j] == '@':
            ri, rj = i, j
            a[i][j] = '.'
            break


for m in moves:
    ni = ri + di[m]
    nj = rj + dj[m]

    if a[ni][nj] == '.':
        ri, rj = ni, nj
    elif a[ni][nj] == '#':
        continue
    elif a[ni][nj] == 'O':
        oi, oj = push(ni, nj, m)
        if oi is None: continue
        else :
            a[ni][nj] = '.'
            a[oi][oj] = 'O'
            ri, rj = ni, nj

sol = 0

for i in range(n):
    for j in range(n):
        if a[i][j] == 'O':
            sol += 100 * i + j

print(sol)