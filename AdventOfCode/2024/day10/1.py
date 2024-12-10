
with open('input.txt', 'r') as f:
# with open('test.txt', 'r') as f:
    lines = f.read().splitlines()


a = [[int(x) for x in line.strip()] for line in lines]
n = len(lines)
m = len(lines[0])
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def inMat(i, j): return 0 <= i < n and 0 <= j < m

def trail_score(i, j, vis):
    vis.add((i, j))

    if a[i][j] == 9:
        return 1

    s = 0
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if inMat(ni, nj) and a[ni][nj] == a[i][j] + 1 and (ni, nj) not in vis:
            s += trail_score(ni, nj, vis)
    return s

sol = 0 
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            sol += trail_score(i, j, set())

print(sol)

