with open('test.txt', 'r') as f:
# with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

a = [[c for c in line.strip()] for line in lines]
n = len(a)

def inMatrix(i, j): return 0 <= i < n and 0 <= j < n

antennas = {}
antidotes = set()

for i in range(n):
    for j in range(n):
        if a[i][j] != '.':
            if a[i][j] in antennas: antennas[a[i][j]].append((i, j))
            else: antennas[a[i][j]] = [(i, j)]
        
for k, v in antennas.items():
    for l in range(len(v) - 1):
        for r in range(l + 1, len(v)):
            x, y = v[l], v[r]
            dh, dl = abs(x[0] - y[0]), abs(x[1] - y[1])
            p1 = [x[0] - dh if x[0] <= y[0] else x[0] + dh, x[1] - dl if x[1] <= y[1] else x[1] + dl]
            p2 = [y[0] + dh if x[0] <= y[0] else y[0] - dh, y[1] + dl if x[1] <= y[1] else y[1] - dl]
            if inMatrix(p1[0], p1[1]): antidotes.add((p1[0], p1[1]))
            if inMatrix(p2[0], p2[1]): antidotes.add((p2[0], p2[1]))

print(len(antidotes))

