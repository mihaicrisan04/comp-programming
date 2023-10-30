

def knapsack(w: int, weights: list, values: list) -> int:

    dp = [[0 for _ in range(w + 1)] for _ in range(len(weights) + 1)]

    for i in range(1, w + 1):
        for j in range(1, len(weights) + 1):
            if weights[j - 1] <= i:
                dp[j][i] = max(dp[j - 1][i], values[j - 1] + dp[j - 1][i - weights[j - 1]])
            else:
                dp[j][i] = dp[j - 1][i]
    
    return dp[len(weights)][w]

w = 14
weights = [1, 2, 3, 5, 9]
values  = [2, 8, 6, 4, 9]

print(knapsack(w, weights, values))