def read_file():
    file_name = 'data.in'
    with open(file_name, 'r') as f:
        lines = f.readlines()
        return lines

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def inMatrix(a, x, y) -> bool:
    return 0 <= x < len(a) and 0 <= y < len(a[0])

def lee(a, b, x, y):
    b[x][y] = 1
    if a[x][y] == 'S':
        for d in range(4):
            if inMatrix(a, x + di[d], y + dj[d]) and a[x + di[d]][y + dj[d]] == '.':
                lee(a, b, x + di[d], y + dj[d])

    if a[x][y] in ['|', '-']:
        if a[x][y] == '|':
            if b[x - 1][y] == 0:
                lee(a, b, x - 1, y)

    if a[x][y] in ['F', 'J', '7', 'F']:
        


def part1():
    lines = read_file()
    a = [[_ for _ in line.strip()] for line in lines]
    sx, sy = 0, 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 'S':
                sx, sy = i, j

    b = [[0 for _ in range(len(a[0]))] for _ in range(len(a))]
    a[sx][sy] = 0
    lee(a, b, sx, sy)

def part2():
    pass

if __name__ == '__main__':
    part1()
    part2()