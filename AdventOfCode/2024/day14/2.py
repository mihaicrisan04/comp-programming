import re
import os
from PIL import Image

with open('input.txt', 'r') as f:
    data= f.read()

n, m = 103, 101
a = [[0 for i in range(m)] for j in range(n)]
robots = []
velocities = []

height, width = n, m
image = Image.new('RGB', (width, height), 'white')

pattern = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"
matches = re.findall(pattern, data)
for match in matches:
    px, py = int(match[0]), int(match[1])
    vx, vy = int(match[2]), int(match[3])
    robots.append((px, py))
    velocities.append((vx, vy))


t = 1
while t < 10: # found the frame from 10000 previous frames
    for i in range(len(robots)):
        x, y = robots[i]
        a[y][x] -= 1
        vx, vy = velocities[i]
        x = (x + vx) % m
        y = (y + vy) % n
        robots[i] = (x, y)
        a[y][x] += 1

    pixels = image.load()
    for i in range(height):
        for j in range(width):
            if a[i][j] > 0:
                pixels[j, i] = (255, 255, 255)
            else:
                pixels[j, i] = (0, 0, 0)

    file_name = 'frame' + str(t) + '.bmp'
    image.save('frames/' + file_name)

    t += 1

