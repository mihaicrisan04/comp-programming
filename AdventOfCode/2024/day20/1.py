import heapq

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def inside(i, j, n): return 0 <= i < n and 0 <= j < n

def dijkstra(i, j, S, E, n, a):
    pq = []
    dis = [[10**9 for _ in range(n)] for _ in range(n)]
    heapq.heapify(pq)

    heapq.heappush(pq, (0, i, j))
    dis[i][j] = 0

    while pq:
        dist, i, j = heapq.heappop(pq)

        if dist > dis[i][j]: continue

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if inside(ni, nj, n) and a[ni][nj] == '.' and dis[ni][nj] > dis[i][j] + 1:
                dis[ni][nj] = dis[i][j] + 1
                heapq.heappush(pq, (dis[ni][nj], ni, nj))

    # for i in range(n):
    #     for j in range(n):
    #         if dis[i][j] == 10**9: print('#', end=' ')
    #         else: print(dis[i][j], end=' ')
    #     print()
    
    return dis[S[0]][S[1]], dis[E[0]][E[1]]

def solve():
    # with open('input.txt') as f:
    with open('test.txt') as f:
        lines = f.read().splitlines()
    

    a = [[c for c in line] for line in lines]
    n = len(lines)

    for i in range(n):
        for j in range(n):
            if a[i][j] == 'S': S = (i, j); a[i][j] = '.'
            if a[i][j] == 'E': E = (i, j); a[i][j] = '.'

    # for i in range(n):
    #     for j in range(n):
    #         print(a[i][j], end='')
    #     print()

    _, official = dijkstra(S[0], S[1],S, E, n, a)

    cheats = {}

    for i in range(n):
        for j in range(n):
            if a[i][j] == '#':
                for d in range(4):
                    ni = i + di[d]
                    nj = j + dj[d]

                    if inside(ni, nj, n):
                        old = a[ni][nj]
                        a[ni][nj] = '.'

                        ts, te = dijkstra(i, j, S, E, n, a)
                        
                        if ts + te >= official: continue

                        if ts + te in cheats: cheats[ts + te] += 1
                        else: cheats[ts + te] = 1
        
                        a[ni][nj] = old

    ans = 0
    for time, k in reversed(sorted(cheats.items())):
        print(k, official - time)
        if official - time >= 100: ans += 1

    print(ans)

solve()
    