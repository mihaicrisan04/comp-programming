import re

with open('input.txt', 'r') as file:
# with open('test.txt', 'r') as file:
    data = file.read()

pattern = r'(do\(\)|don\'t\(\))|mul\((\d+),(\d+)\)'
matches = re.findall(pattern, data)
   
sol = 0
flag = True

for match in matches:
    if match[0] == 'do()':
        flag = True
    elif match[0] == 'don\'t()':
        flag = False
    else:
        x1, x2 = map(int, match[1:])
        if flag:
            sol += x1 * x2

print(sol)

