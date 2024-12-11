
# with open('test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    nums = [int(x) for x in f.read().strip().split()]

dp = {}

def solve(num, k):
    if (num, k) in dp:
        return dp[(num, k)]

    if k == 0: ret = 1
    elif num == 0: ret = solve(1, k-1)
    elif len(str(num)) % 2 == 0: 
        num1 = int(str(num)[:len(str(num))//2])
        num2 = int(str(num)[len(str(num))//2:])
        ret = solve(num1, k-1) + solve(num2, k-1)
    else: ret = solve(num * 2024, k-1)
    dp[(num, k)] = ret
    return ret

print(sum(solve(num, 75) for num in nums))



