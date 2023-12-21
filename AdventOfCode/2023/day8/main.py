import sys

def read_file():
    file_name = 'data.in'
    with open(file_name, 'r') as f:
        lines = f.readlines()
        return lines

# part 1
# def search(key, index, instr, d):
#     if key == 'ZZZ':
#         return 0
#     if instr[index] == 'L':
#         print(key, '->', d[key][0])
#         return 1 + search(d[key][0], (index + 1) % len(instr), instr, d)
#     else:
#         print(key, '->', d[key][1])
#         return 1 + search(d[key][1], (index + 1) % len(instr), instr, d)

# part 2
from math import gcd

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def list_lcm(numbers):
    result = 1
    for num in numbers:
        result = lcm(result, num)
    return result

def search(key, index, instr, d):
    if key[2] == 'Z':
        return 0
    if instr[index] == 'L':
        return 1 + search(d[key][0], (index + 1) % len(instr), instr, d)
    else:
        return 1 + search(d[key][1], (index + 1) % len(instr), instr, d)


def main():
    sys.setrecursionlimit(1000000)
    lines = read_file()
    d = {}
    instr = lines[0].strip()

    lines = lines[2:]

    for line in lines:
        key, values = line.strip().split('=')
        key = key.strip()

        left, right = values.split(',')
        left = left.strip().lstrip('(')
        right = right.strip().rstrip(')')

        if key not in d:
            d[key] = (left, right)

    # part 1
    # l = search('AAA', 0, instr, d)
    # print(l)

    # part 2
    a = []
    for i in d:
        key = i
        if key[2] == 'A':
            a.append(i)
    s = []
    for i in a:
        l = search(i, 0, instr, d)
        s.append(l)

    result = list_lcm(s)
    print(result)




if __name__ == '__main__':
    main()