
with open('input.txt') as f:
# with open('test.txt') as f:
    lines = f.readlines()

a = [line.strip() for line in lines]
n = len(a)

def xmas(i, j):
    k = 0
    # M.M
    # .A.
    # S.S
    if (a[i-1][j-1] == 'M' and a[i-1][j+1] == 'M' and
        a[i+1][j-1] == 'S' and a[i+1][j+1] == 'S'):
        k += 1   
    # M.S
    # .A.
    # M.S
    if (a[i-1][j-1] == 'M' and a[i+1][j-1] == 'M' and
        a[i-1][j+1] == 'S' and a[i+1][j+1] == 'S'):
        k += 1   
    # S.S
    # .A.
    # M.M
    if (a[i-1][j-1] == 'S' and a[i-1][j+1] == 'S' and
        a[i+1][j-1] == 'M' and a[i+1][j+1] == 'M'):
        k += 1
    # S.M
    # .A.
    # S.M
    if (a[i-1][j-1] == 'S' and a[i+1][j-1] == 'S' and
        a[i-1][j+1] == 'M' and a[i+1][j+1] == 'M'):
        k += 1
    return k

def countXmas():
    count = 0
    for i in range(1, n-1):
        for j in range(1, n-1):
            if a[i][j] == 'A':
                count += xmas(i, j)
    return count

print(countXmas())
