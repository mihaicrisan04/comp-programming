
# with open('test.txt', 'r') as f:
# with open('input.txt', 'r') as f:
with open('test2.txt', 'r') as f:
    data = f.read().splitlines()

n = len(data)
vis = [[0 for _ in range(n+2)] for _ in range(n+2)]
a = [[0 for _ in range(n+2)] for _ in range(n+2)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
def inMat(i, j): return 1 <= i <= n and 1 <= j <= n
for i in range(1, n+1):
    for j in range(1, n+1):
        a[i][j] = data[i-1][j-1]

def fill(i, j, p, k):
    q = []
    q.append((i, j))

    while len(q) > 0:
        i, j = q.pop(0)

        if vis[i][j]: continue
        vis[i][j] = k

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if inMat(ni, nj) and a[ni][nj] == p and not vis[ni][nj]:
                q.append((ni, nj))


def AP(i, j, k):
    q = []
    q.append((i, j))
    A = P = 0

    while len(q) > 0:
        i, j = q.pop(0)

        if vis[i][j] == -k: continue
        vis[i][j] = -k
        A += 1

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if vis[ni][nj] != -k and vis[ni][nj] != k: P += 1

            if inMat(ni, nj) and vis[ni][nj] == k:
                q.append((ni, nj))

    return A, P


k = 1
for i in range(1, n+1):
    for j in range(1, n+1):
        if not vis[i][j]:
            fill(i, j, a[i][j], k)
            k += 1

sol = 0
for r in range(1, k):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if vis[i][j] == r:
                A, P = AP(i, j, r)
                sol += A * P


# for i in range(n+2):
#     for j in range(n+2):
#         print(vis[i][j], end=' ')
#     print()

print(sol)

