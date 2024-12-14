import re
import os
import numpy as np
import matplotlib.pyplot as plt

with open('input.txt', 'r') as f:
    data= f.read()

n, m = 103, 101
a = [[0 for i in range(m)] for j in range(n)]
robots = []
velocities = []

pattern = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"
matches = re.findall(pattern, data)
for match in matches:
    px, py = int(match[0]), int(match[1])
    vx, vy = int(match[2]), int(match[3])
    robots.append((px, py))
    velocities.append((vx, vy))


variances = []
threshold = 1000
marked_times = []
marked_variances = []

# sol is at 6512
for t in range(7000):
    for i in range(len(robots)):
        x, y = robots[i]
        a[y][x] -= 1
        vx, vy = velocities[i]
        x = (x + vx) % m
        y = (y + vy) % n
        robots[i] = (x, y)
        a[y][x] += 1

    # Calculate variance
    x_coords = [robot[0] for robot in robots]
    y_coords = [robot[1] for robot in robots]
    variance = np.var(x_coords) + np.var(y_coords) # total variance of x and y coordinates at time t
    variances.append(variance)

    if variance < threshold:
        marked_times.append(t)
        marked_variances.append(variance)


plt.plot(variances)
plt.xlabel('Time')
plt.ylabel('Variance')
plt.title('Variance of Points Over Time')

plt.scatter(marked_times, marked_variances, color='green', label='Marked')  
plt.scatter(6512, variances[6512], color='red', s=100, label='Solution')

plt.savefig('variance_plot.png')

plt.show()
