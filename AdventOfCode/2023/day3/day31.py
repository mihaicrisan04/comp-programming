
a = []

with open('data.in', 'r') as f:
    sum = 0
    lines = f.readlines()
    for line in lines:
        numbers = line.split()   
        a.append(numbers)   

def get_nums(i, j):
    # up

    # down

    # left
    left = []
    jj = j - 1
    while a[i][jj] != '.' and jj >= 0:
        left.append(a[i][jj])
        jj -= 1

    # right
    right = []
    jj = j + 1
    while a[i][jj] != '.' and jj < len(a[i]):
        right.append(a[i][jj])
        jj += 1

for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        if a[i][j] == '*':
            a, b = get_nums(i, j)
            sum += a * b