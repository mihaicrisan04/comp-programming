from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(heights)
        m = len(heights[0])

        for i in range(n):
            for j in range(m):
                if self.canFlow(i, j, n, m, heights):
                    res.append([i, j])

        return res
    
    def canFlow(self, i, j, n, m, heights):
        a = p = False
        if i == 0 or j == 0: p = True
        if i == n-1 or j == m-1: a = True
        if a and p: return True

        di = [-1, 0, 1, 0]
        dj = [0, 1, 0, -1]
        q = []
        vis = [[False] * m for _ in range(n)]

        q.append((i, j))

        while len(q) > 0:
            i, j = q.pop(0)

            if vis[i][j]: continue
            vis[i][j] = True

            if a and p: return True

            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if self.inside(ni, nj, n, m) and heights[ni][nj] <= heights[i][j] and not vis[ni][nj]:
                    q.append((ni, nj))
                    if ni == 0 or nj == 0: p = True
                    if ni == n-1 or nj == m-1: a = True

        return False

    def inside(self, i, j, n, m): return 0 <= i < n and 0 <= j < m
        


s = Solution()
# print(s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
print(s.pacificAtlantic([[8,12,0,17,8,7,7,1,12,19,12,19,14,1,16,0,14,7,4,14,14,8,17,18,9,14,19,16,19,17,7,14,13,17,2,11,16,8,8,8]]))