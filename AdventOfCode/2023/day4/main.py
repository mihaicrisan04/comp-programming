


def read_file():
    file_name = 'data.in'
    with open(file_name, 'r') as f:
        lines = f.readlines()
        return lines

# part 1
# def main():
#     lines = read_file()
#     sum = 0
#     for line in lines:
#         game, score = line.split(':')
#         win, you = score.split('|')

#         win = [int(x) for x in win.split()]
#         you = [int(x) for x in you.split()]

#         k = -1
#         for num in you:
#             if num in win:
#                 k += 1

#         if k != -1:
#             sum += 2 ** k

#     print(sum)

# part 2
def main():
    lines = read_file()
    sum = 0
    f = [0] * 1000
    g = [0] * 1000
    for line in lines:
        game, score = line.split(':')
        c, game = game.split()
        game = int(game)
        win, you = score.split('|')

        win = [int(x) for x in win.split()]
        you = [int(x) for x in you.split()]

        f[game] += 1 # add the original card

        k = 0
        for num in you:
            if num in win:
                k += 1
        
        for i in range(game + 1, game + k + 1):
            f[i] += f[game]

    for i in range(1, game + 1):
        sum += f[i]

    print(sum)


if __name__ == '__main__':
    main()  