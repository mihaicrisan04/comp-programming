from typing import Any


# with open('test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

def getValuesFrom(nums: list, acc = 0, values = []):
    if len(nums) == 0: return [acc]
    v1 = getValuesFrom(nums[1:], acc + nums[0])
    v2 = getValuesFrom(nums[1:], acc * nums[0])
    return v1 + v2


sol = 0
for line in lines:
    target, nums = line.split(':')
    target = int(target)
    nums = [int(num) for num in nums.split()]

    values = getValuesFrom(nums[1:], nums[0])

    print(target, values)
    if target in values:
        sol += target


print(sol)