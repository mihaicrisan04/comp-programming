


def read_file():
    file_name = 'data.in'
    with open(file_name, 'r') as f:
        lines = f.readlines()
        return lines

def main() -> None:
    lines = read_file()
    aux, time = lines[0].split(':')
    aux, distance = lines[1].split(':')
    time = [char for char in time if char != '\n' and char != ' ']
    distance = [char for char in distance if char != '\n' and char != ' ']
    time = int(''.join(time))
    distance = int(''.join(distance))

    res = 1
    k = 0
    for j in range(time):
        t = time - j
        d = t * j
        if d > distance:
            k += 1
    
    if k != 0:
        res *= k

    print(res)


if __name__ == '__main__':
    main()  