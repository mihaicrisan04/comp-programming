class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(0, m):
            for j in range(0, n):
                if i == j == 0:
                    continue
                # should check if i-1 is valid and j-1 is valid
                dp[i][j] = dp[i][j-1] + dp[i-1][j]

        return dp[m-1][n-1]