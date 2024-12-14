import re

with open('input.txt', 'r') as f:
# with open('test.txt', 'r') as f:
    data= f.read()

n, m = 103, 101
# n, m = 7, 11
robots = []
velocities = []

q1, q2, q3, q4 = 0, 0, 0, 0

pattern = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"
matches = re.findall(pattern, data)
for match in matches:
    px, py = int(match[0]), int(match[1])
    vx, vy = int(match[2]), int(match[3])
    robots.append((px, py))
    velocities.append((vx, vy))


for i in range(len(robots)):
    x, y = robots[i]
    vx, vy = velocities[i]
    x = (x + 100 * vx) % m
    y = (y + 100 * vy) % n
    robots[i] = (x, y)

for i in range(len(robots)):
    x, y = robots[i]
    if 0 <= x < m//2 and 0 <= y < n//2: q1 += 1
    if 0 <= x < m//2 and n//2 < y < n: q2 += 1
    if m//2 < x < m and 0 <= y < n//2: q3 += 1
    if m//2 < x < m and n//2 < y < n: q4 += 1

print(q1 * q2 * q3 * q4)
