"""
    1. Determine the longest commo subsequence of two given sequences.
    Subsequence elements are not required to occupy consecutive positions.
    For example, if X = "MNPNQMN" and Y = "NQPMNM", the longest common
    subsequence has length 4, and can be one of "NQMN", "NPMN" or "NPNM". 
    Determine and display both the length of the longest common 
    subsequence as well as at least one such subsequence.
"""

x = "MNPNQMN"
y = "NQPMNM"

n = len(x)
m = len(y)

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if x[i-1] == y[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

length = dp[n][m]

i = n
j = m
sol = ""

while i > 0 and j > 0:
    if x[i-1] == y[j-1]:
        sol = x[i-1] + sol
        i -= 1
        j -= 1
    elif dp[i][j-1] > dp[i-1][j]:
        j -= 1
    else:
        i -= 1

print(length)
print(sol)

