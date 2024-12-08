
with open('test.txt', 'r') as f:
# with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

a = [[c for c in line.strip()] for line in lines]
n = len(a)
m = {}

def inMatrix(i, j): return 0 <= i < n and 0 <= j < n

for i in range(n):
    for j in range(n):
        if a[i][j] != '.':
            if a[i][j] in m: m[a[i][j]].append((i, j))
            else: m[a[i][j]] = [(i, j)]
        
for k, v in m.items():
    for l in range(len(v) - 1):
        for r in range(l+1, len(v)):
            x, y = v[l], v[r]
            dh = abs(x[0] - y[0])
            dl = abs(x[1] - y[1])

            fx = x[0] <= y[0]
            fy = x[1] <= y[1]

            k = 1
            while True: # look for points in one direction
                px = x[0] - k*dh if fx else x[0] + k*dh
                py = x[1] - k*dl if fy else x[1] + k*dl

                if not inMatrix(px, py): break
                if a[px][py] == '.': a[px][py] = '#' # mark antidote
                k += 1

            k = 1
            while True: # look for points in the other direction
                px = y[0] + k*dh if fx else y[0] - k*dh
                py = y[1] + k*dl if fy else y[1] - k*dl

                if not inMatrix(px, py): break
                if a[px][py] == '.': a[px][py] = '#' # mark antidote
                k += 1

sol = 0
for i in range(n):
    for j in range(n):
        if a[i][j] != '.': sol += 1 # everything counts as an antitode now
        print(a[i][j], end=' ')
    print()
            
print(sol)
