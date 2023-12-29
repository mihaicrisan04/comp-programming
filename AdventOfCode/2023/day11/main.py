def read_file():
    file_name = 'data.in'
    with open(file_name, 'r') as f:
        lines = f.readlines()
        return lines

def print_matrix(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end='')
        print()

def expand_horizontal(a, i):
    a.insert(i, ['.'] * len(a[0]))
    for j in range(len(a) - 1, i, -1):
        a[j] = a[j - 1][:]

def expand(a):
    # expand horizontally
    i = 0
    while i < len(a):
        if '#' not in a[i]:
            expand_horizontal(a, i)
            i += 2  # Skip the newly added row
        else:
            i += 1


def main():
    lines = read_file()
    a = [list(line.strip()) for line in lines]

    expand(a)

    print_matrix(a)


if __name__ == '__main__':
    main()