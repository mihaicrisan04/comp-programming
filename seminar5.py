

def knapsack(w: int, weights: list, values: list) -> int:

    dp = [[0 for _ in range(len(weights) + 1)] for _ in range(w + 1)]

    for i in range(1, w + 1):
        for j in range(1, len(weights) + 1):
            if weights[j - 1] <= i:
                dp[i][j] = max(dp[i][j - 1], values[j - 1] + dp[i - weights[j - 1]][j - 1])
            else:
                dp[i][j] = dp[i][j - 1]
    
    return dp[w][len(weights)]

w = 14
weights = [1, 2, 3, 5, 9]
values  = [2, 8, 6, 4, 9]

print(knapsack(w, weights, values))