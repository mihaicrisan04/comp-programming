

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

    a.sort()
    b.sort()

    sol = 0
    for i in range(len(a)):
        sol += abs(a[i] - b[i])

    print(sol)





