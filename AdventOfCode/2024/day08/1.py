
# with open('test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

a = [[c for c in line.strip()] for line in lines]
n = len(a)

def inMatrix(i, j): return 0 <= i < n and 0 <= j < n

m = {}
b = {}

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
            p1 = [-1, -1]
            p2 = [-1, -1]
            if x[0] <= y[0]: # x is hiher than y
                p1[0] = x[0] - dh
                p2[0] = y[0] + dh
            else:
                p1[0] = x[0] + dh
                p2[0] = y[0] - dh
            if x[1] <= y[1]: # x is on the left of y
                p1[1] = x[1] - dl
                p2[1] = y[1] + dl
            else:
                p1[1] = x[1] + dl
                p2[1] = y[1] - dl
            if inMatrix(p1[0], p1[1]): b[(p1[0], p1[1])] = None
            if inMatrix(p2[0], p2[1]): b[(p2[0], p2[1])] = None
            
print(len(b))

