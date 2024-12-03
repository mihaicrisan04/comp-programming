import re

with open('input.txt', 'r') as file:
# with open('test.txt', 'r') as file:
    data = file.read().splitlines()

pattern = r'mul\((\d+),\s*(\d+)\)'
sol = 0
for line in data:
    matches = re.findall(pattern, line)
    for match in matches:
        x1, x2 = map(int, match)
        sol += x1 * x2

print(sol)

