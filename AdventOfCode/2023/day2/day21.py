import os


path = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(path, 'data.in')

with open(file_name, 'r') as f:
    data = f.read().splitlines()

    sum = 0
    maxr, maxg, maxb = 12, 13, 14

    for index, line in enumerate(data):
        index = index + 1
        line = line[line.index(':')+1:]
        line = line.split(';')
        is_posible = True
        for game in line:
            rounds = game.split(',')
            for r in rounds:
                r = r.strip()
                r = r.split(' ')
                count, color = int(r[0]), r[1]

                if color == 'red':
                    if count > maxr:
                        is_posible = False
                elif color == 'green':
                    if count > maxg:
                        is_posible = False
                elif color == 'blue':
                    if count > maxb:
                        is_posible = False

        if is_posible == True:
            sum += index 

    print(sum)

        