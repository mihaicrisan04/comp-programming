def read_file():
    file_name = 'data.in'
    with open(file_name, 'r') as f:
        lines = f.readlines()
        return lines

def part1():
    lines = read_file()
    sol = 0
    for line in lines:
        line = line.strip()
        v = [int(x) for x in line.split(' ')]

        a = []
        a.append(v)
        i = 0
        while True:
            ok = True
            for j in range(len(a[i])):
                if a[i][j] != 0:
                    ok = False
            if ok:
                break
            else:
                a.append([0] * (len(a[i]) - 1))
                i += 1
                for j in range(len(a[i-1]) - 2, -1, -1):
                    a[i][j] = a[i-1][j+1] - a[i-1][j]

        i = len(a) - 1
        while i >= 1:
            g = a[i-1][-1] + g if i != len(a) - 1 else a[i-1][-1]   
            i -= 1
        sol += g

    print(sol)

def part2():
    lines = read_file()
    sol = 0
    for line in lines:
        line = line.strip()
        v = [int(x) for x in line.split(' ')]

        a = []
        a.append(v)
        i = 0
        while True:
            ok = True
            for j in range(len(a[i])):
                if a[i][j] != 0:
                    ok = False
            if ok:
                break
            else:
                a.append([0] * (len(a[i]) - 1))
                i += 1
                for j in range(len(a[i-1]) - 2, -1, -1):
                    a[i][j] = a[i-1][j+1] - a[i-1][j]

        i = len(a) - 1
        while i >= 1:
            g = a[i-1][0] - g if i != len(a) - 1 else a[i-1][0]   
            i -= 1
        sol += g

    print(sol)

if __name__ == '__main__':
    part1()
    part2()