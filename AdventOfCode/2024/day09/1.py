
# with open('input.txt', 'r') as f:
with open('test.txt', 'r') as f:
    data = f.read()


data = [int(c) for c in data]
a = []
i = 0
id = 0

def getNextFreePos(i):
    while a[i] != '.' and i < len(a): i += 1
    return i

def getNextBlockPos(i):
    while a[i] == '.' and i >= 0: i -= 1
    return i

while (i < len(data)):
    c, s = i, i + 1

    if c < len(data): 
        for k in range(data[c]): a.append(id)
    if s < len(data): 
        for k in range(data[s]): a.append('.')
    
    id += 1
    i += 2

l = getNextFreePos(0)
r = getNextBlockPos(len(a) - 1)
while l < r:
    a[l], a[r] = a[r], a[l]

    l = getNextFreePos(0)
    r = getNextBlockPos(len(a) - 1)

sol = 0
for i in range(len(a)):
    if a[i] == '.': break
    sol += i * a[i]

print(sol)