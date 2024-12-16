import heapq

# with open('test.txt', 'r') as f:
with open('test2.txt', 'r') as f:
# with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

n = len(lines[0])
a = [[c for c in line] for line in lines]
costs =[[int(1e9) for _ in range(n)] for _ in range(n)]
costse =[[int(1e9) for _ in range(n)] for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
prev = {}

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
#     ^  >  v  <


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

            if a[ni][nj] != '#':
                new_cost = cost + (1 if d == direction else 1001)
                if new_cost < costs[ni][nj]:
                    prev[(ni, nj)] = prev.get((ni, nj), []) + [(i, j, d)]
                    heapq.heappush(pq, (new_cost, (ni, nj), d))

    return costs[E[0]][E[1]]


def bfs2(S, E):
    pq = []
    heapq.heapify(pq)

    heapq.heappush(pq, (0, S, 3))
    heapq.heappush(pq, (0, S, 2))

    while pq:
        cost, pos, direction = heapq.heappop(pq)
        i, j = pos

        if cost >= costse[i][j]: continue
        costse[i][j] = cost
        
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if a[ni][nj] != '#':
                new_cost = cost + (1 if d == direction else 1001)
                if new_cost < costse[ni][nj]:
                    heapq.heappush(pq, (new_cost, (ni, nj), d))
        
    return costse[E[0]][E[1]]


for i in range(n):
    for j in range(n):
        if a[i][j] == 'S':
            S = (i, j)
        if a[i][j] == 'E':
            E = (i, j)

answer = bfs(S, E)
answer2 = bfs2(E, S)

for i in range(n):  
    for j in range(n):
        if costs[i][j] == 1e9: print("#######", end="\t")
        else: print(costs[i][j], end="\t")
    print()
print()
for i in range(n):  
    for j in range(n):
        if costs[i][j] == 1e9: print("#######", end="\t")
        else: print(costse[i][j], end="\t")
    print()
 
