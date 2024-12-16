import heapq

with open('test.txt', 'r') as f:
# with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

n = len(lines[0])
a = [[c for c in line] for line in lines]
costs =[[int(1e9) for _ in range(n)] for _ in range(n)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def bfs(S, E):
    pq = []
    heapq.heapify(pq)

    heapq.heappush(pq, (0, S, 1))

    while pq:
        cost, pos, direction = heapq.heappop(pq)
        i, j = pos

        if cost >= costs[i][j]: continue
        costs[i][j] = cost
        
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if a[ni][nj] != '#' and costs[ni][nj] > cost + (1 if d == direction else 1001):
                heapq.heappush(pq, (cost + (1 if d == direction else 1001), (ni, nj), d))

    print(costs[E[0]][E[1]])


for i in range(n):
    for j in range(n):
        if a[i][j] == 'S':
            S = (i, j)
        if a[i][j] == 'E':
            E = (i, j)

bfs(S, E)