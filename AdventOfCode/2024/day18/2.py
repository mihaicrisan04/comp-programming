import heapq

# with open('test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

n = 71
# n = 7
a = [[0 for _ in range(n)] for _ in range(n)]
coords = [[int(pair.split(',')[0]), int(pair.split(',')[1])] for pair in lines]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def inside(i, j): return 0 <= i < n and 0 <= j < n

def dijskstra(x, y):
    pq = []
    heapq.heapify(pq)
    d = [[10**9 for _ in range(n)] for _ in range(n)]
    d[x][y] = 0

    heapq.heappush(pq, (0, x ,y))

    while pq:
        dis, i, j = heapq.heappop(pq)

        if dis < d[i][j]: continue

        for o in range(4):
            ni = i + di[o]
            nj = j + dj[o]

            if inside(ni, nj) and a[ni][nj] == 0 and d[ni][nj] > d[i][j] + 1:
                d[ni][nj] = d[i][j] + 1
                heapq.heappush(pq, (d[ni][nj], ni, nj))
    
    return d[n-1][n-1]


for i in range(1024):
# for i in range(12):
    a[coords[i][0]][coords[i][1]] = 1

flag = True
pos = 1024
# pos = 12
while flag:
    a[coords[pos][0]][coords[pos][1]] = 1

    if dijskstra(0, 0) == 10**9:
        print(coords[pos][0], coords[pos][1])   
        flag = False

    pos += 1