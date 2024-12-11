
with open('test.txt', 'r') as f:
# with open('input.txt', 'r') as f:
    nums = [int(x) for x in f.read().strip().split()]

def rule(num, k):
    if k == 0: return 1
    if num == 0: return rule(1, k-1)
    elif len(str(num)) % 2 == 0:
        num1 = int(str(num)[:len(str(num))//2])
        num2 = int(str(num)[len(str(num))//2:])
        return rule(num1, k-1) + rule(num2, k-1)
    else: return rule(num * 2024, k-1)

sol = sum([rule(num, 25) for num in nums])
print(sol)