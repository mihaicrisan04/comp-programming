def get_max_joltage(line):
    result = []
    pos = 0

    for k in range(12):
        search_end = len(line) - (11 - k)
        digit = max((line[j] for j in range(pos, search_end)), default='0')
        result.append(digit)
        pos = line.index(digit, pos) + 1

    return int(''.join(result))


def main():
    with open("input.txt", "r") as f:
        print(sum(get_max_joltage(line.strip()) for line in f))


if __name__ == "__main__":
    main()
