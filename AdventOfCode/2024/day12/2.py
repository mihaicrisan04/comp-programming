
with open('input.txt', 'r') as f:
# with open('test.txt', 'r') as f:
# with open('test2.txt', 'r') as f:
# with open('test3.txt', 'r') as f:
    data = f.read().splitlines()

n = len(data)
vis = [[0 for _ in range(n+2)] for _ in range(n+2)]
a = [[0 for _ in range(n+2)] for _ in range(n+2)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
dirs = ['UP', 'RIGHT', 'DOWN', 'LEFT']
#    UP, R, DWN, L
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


def AS(i, j, k):
    q = []
    q.append((i, j))
    A = S = 0

    h = [[[] for _ in range(4)] for _ in range(n+2)]
    v = [[[] for _ in range(4)] for _ in range(n+2)]

    while len(q) > 0:
        i, j = q.pop(0)

        if vis[i][j] == -k: continue
        vis[i][j] = -k
        A += 1

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if vis[ni][nj] != -k and vis[ni][nj] != k:
                # horizontal
                if len(h[ni][d]) == 0:
                    h[ni][d].append((nj, nj))
                else:
                    extended = False
                    for p in range(len(h[ni][d])):
                        l = h[ni][d][p][0]
                        r = h[ni][d][p][1]
                        if nj == l - 1:
                            h[ni][d][p] = (nj, r)
                            extended = True
                            break
                        if nj == r + 1:
                            h[ni][d][p] = (l, nj)
                            extended = True
                            break
                    
                    if not extended:
                        h[ni][d].append((nj, nj))

                    h[ni][d] = sorted(h[ni][d])
                    unified = []
                    for p in range(len(h[ni][d])):
                        if p < len(h[ni][d]) - 1:
                            if h[ni][d][p][1] == h[ni][d][p+1][0] - 1:
                                unified.append((h[ni][d][p][0], h[ni][d][p+1][1]))
                                p += 1
                            else:
                                unified.append(h[ni][d][p])
                        else:
                            unified.append(h[ni][d][p])
                    h[ni][d] = unified
                
                # vertical
                if len(v[nj][d]) == 0:
                    v[nj][d].append((ni, ni))
                else:
                    extended = False
                    for p in range(len(v[nj][d])):
                        l = v[nj][d][p][0]
                        r = v[nj][d][p][1]
                        if ni == l - 1:
                            v[nj][d][p] = (ni, r)
                            extended = True
                            break
                        if ni == r + 1:
                            v[nj][d][p] = (l, ni)
                            extended = True
                            break

                    if not extended:
                        v[nj][d].append((ni, ni))
                    
                    v[nj][d] = sorted(v[nj][d])
                    unified = []
                    for p in range(len(v[nj][d])):
                        if p < len(v[nj][d]) - 1:
                            if v[nj][d][p][1] == v[nj][d][p+1][0] - 1:
                                unified.append((v[nj][d][p][0], v[nj][d][p+1][1]))
                                p += 1
                            else:
                                unified.append(v[nj][d][p])
                        else:
                            unified.append(v[nj][d][p])
                    v[nj][d] = unified
 

            if inMat(ni, nj) and vis[ni][nj] == k:
                q.append((ni, nj))


    for row in range(n+2):
        # print('row ', row)
        for d in range(4):
            # print('\t', dirs[d], end=' ')
            if d == 0 or d == 2: S += len(h[row][d])
            # for l, r in h[row][d]:
            #     print(f'({l}-{r})', end=' ')
            # print()

    for col in range(n+2):
        # print('col ', col)
        for d in range(4):
            # print('\t', dirs[d], end=' ')
            if d == 1 or d == 3: S += len(v[col][d])
            # for l, r in h[col][d]:
            #     print(f'({l}-{r})', end=' ')
            # print()

    # print(S)

    return A, S


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
                A, S = AS(i, j, r)
                sol += A * S

print(sol)

# my result 888017
# sol 887932
