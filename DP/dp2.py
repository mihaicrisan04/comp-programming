"""
    2. Given the set of positive integers S and the natural number k,
    display one of the subsets of S which sum to k. For example, if 
    S = { 2, 3, 5, 7, 8 } and k = 14, subset { 2, 5, 7 } sums to 14.
"""

def subset_sum(S, k):
    n = len(S)
    
    # Create a 2D array to store the solution to subproblems
    dp = [[False for _ in range(k + 1)] for _ in range(n + 1)]

    # Initialize the first column to True, as there is always an empty subset with sum 0
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the dp array using bottom-up dynamic programming
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if S[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - S[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    # If there exists a subset with sum k, reconstruct the subset
    if dp[n][k]:
        subset = []
        i, j = n, k
        while i > 0 and j > 0:
            if dp[i - 1][j]:
                i -= 1
            else:
                subset.append(S[i - 1])
                j -= S[i - 1]
                i -= 1

        print("Subset with sum", k, ":", subset[::-1])
    else:
        print("No subset found with sum", k)

# Example usage:
S = [2, 3, 5, 7, 8]
k = 14
subset_sum(S, k)
