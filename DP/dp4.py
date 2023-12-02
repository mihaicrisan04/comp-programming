"""
    4. Given an n * n square matrix with integer values, find the maximum
    length of a snake sequence. A snake sequence begins on the matrix's
    top row (coordinate (0, i), 0 <= i < n). Each element of the 
    sequence, except the first one, must have a value ±1 from the 
    previous one and be located directly below, or directly to the 
    right of the previous element. For example, element (i, j) can be
    succeded by one of the (i, j + 1) or (i + 1, j) elements. Display 
    the length as well as the sequence of coordinates for one sequence 
    of maximum length.
"""

n = 4
a = [
    [1, 2, 3, 4],
    [2, 3, 6, 5],
    [3, 4, 7, 8],
    [4, 5, 8, 9]
]

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

dp[1][1] = 1
max_len = 0
x, y = 1, 1

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j == 1:
            continue

        dp[i][j] = 1

        if abs(a[i-1][j-1] - a[i-2][j-1]) == 1:
            dp[i][j] = max(dp[i][j], dp[i-1][j] + 1)

        elif abs(a[i-1][j-1] - a[i-1][j-2]) == 1:
            dp[i][j] = max(dp[i][j], dp[i][j-1] + 1)
        
        elif abs(a[i-1][j-1] - a[i-2][j-1]) == 1 and abs(a[i-1][j-1] - a[i-1][j-2]) == 1:
            dp[i][j] = max(dp[i][j], max(dp[i-1][j], dp[i][j-1]) + 1)

        if dp[i][j] > max_len:
            max_len = dp[i][j]
            x, y = i, j

print(max_len)

sol = ""
while max_len > 0:
    sol = str(a[x-1][y-1]) + " " + sol
    max_len -= 1
    if x > 0 and dp[x-1][y] + 1 == dp[x][y]:
        x -= 1
    else:
        y -= 1

print(sol)