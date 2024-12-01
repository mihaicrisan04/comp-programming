

with open('input.txt', 'r') as f:
    s = f.read()
    a = []
    b = []
    s = s.split('\n')
    for line in s:
        if line:
            n, m = int(line.split()[0]), int(line.split()[1])
            a.append(n)
            b.append(m)

    f = {}

    for i in b:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1

    sol = 0
    for i in range(len(a)):
        sol += f[a[i]] * a[i] if a[i] in f else 0

    print(sol)

