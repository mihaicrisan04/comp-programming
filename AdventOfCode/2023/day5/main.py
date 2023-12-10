


def read_file():
    file_name = 'data.in'
    with open(file_name, 'r') as f:
        lines = f.readlines()
        return lines

def main() -> None:
    lines = read_file()
    print(lines)

if __name__ == '__main__':
    main()  