import os


path = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(path, 'data.in')

with open(file_name, 'r') as f:
    data = f.read().splitlines()

    sum = 0

    for index, line in enumerate(data):
        index = index + 1
        line = line[line.index(':')+1:]
        game = line.split(';')
        maxr, maxg, maxb = -1,-1,-1

        for rounds in game:
            rounds = rounds.split(',')
            for r in rounds:
                r = r.strip()
                r = r.split(' ')
                count, color = int(r[0]), r[1]

                if color == 'red':
                    if count > maxr:
                        maxr = count
                if color == 'green':
                    if count > maxg:
                        maxg = count
                if color == 'blue':
                    if count > maxb:
                        maxb = count


        sum += maxr * maxg * maxb

    print(sum)

        