
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
    vis[i][j] += 1

    if a[i][j] == 9: return 

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if inMat(ni, nj) and a[ni][nj] == a[i][j] + 1:
            trail_score(ni, nj, vis)

sol = 0 
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            vis = [[0 for _ in range(m)] for _ in range(n)]
            trail_score(i, j, vis)
            sol += sum(vis[l][c] for l in range(n) for c in range(m) if a[l][c] == 9)

print(sol)
