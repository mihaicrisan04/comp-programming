
   
def solve():
    # with open('test.txt', 'r') as f:
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()   

    towels = lines[0].split(', ')
    designs = lines[2:]

    results = []

    for design in designs:
        n = len(design)
        dp = [0] * (n + 1)
        dp[0] = 1 # Base case: an empty design can always be formed

        for i in range(1, n + 1):
            for pattern in towels:
                if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                    dp[i] += dp[i - len(pattern)]

        results.append(dp[n])

    return results


results = solve()
print(sum(results))