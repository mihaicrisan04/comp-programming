import sys
from copy import deepcopy

dir = {
    "W": (-1, 0),
    "D": (0, 1),
    "S": (1, 0),
    "A": (0, -1)
}

def get_freq(path):
    w, d, s, a = 0, 0, 0, 0
    for c in path:
        if c == "W":
            w += 1
        elif c == "D":
            d += 1
        elif c == "S":
            s += 1
        elif c == "A":
            a += 1
    return (w, d, s, a)

def smalles_rect(path):
    x_origin = 0
    y_origin = 0
    max_left = 0
    max_right = 0
    max_top = 0
    max_down= 0
    n,m = 0, 0
    for i in path:

        if i == "W":
            n +=1
        elif i == "S":
            n -= 1
        elif i == "A":
            m -= 1
        elif i == "D":
            m += 1
        #print(str(n) + " "+ str(m))
        if n > max_top:
            max_top = n
        if n < max_down:
            max_down = n
        if m < max_left:
            max_left = m
        if m > max_right:
            max_right = m
        #print(max_top, max_down, max_left, max_right)
    return -max_left +max_right+1, max_top- max_down+1       

def is_valid_path(m, n, lawn, path):
    for ii in range(n):
        for jj in range(m):
            visited = [[False for j in range(m)] for i in range(n)]
            i, j = ii, jj
            for c in path:
                if not (0 <= i < n and 0 <= j < m):
                    break
                if visited[i][j]:
                    break
                if lawn[i][j] == -1:
                    break
                visited[i][j] = True
                i += dir[c][0]
                j += dir[c][1]
            if not (0 <= i < n and 0 <= j < m):
                continue
            if visited[i][j]:
                continue
            if lawn[i][j] == -1:
                continue
            visited[i][j] = True

            # check if all cells are visited
            valid = True
            for i in range(n):
                for j in range(m):
                    if not visited[i][j] and lawn[i][j] != -1:
                        valid = False
            if valid:
                return True
    return False

def find_path(m, n, lawn, line_with_tree, col_with_tree):
    path = ""
    direction = "D"  # Initial direction is right

    for i in range(n):
        if i == line_with_tree or i == line_with_tree - 1:
            # If the current row is the row with the tree or the row before it
            for j in range(m if direction == "D" else col_with_tree):
                path += direction
            path += "S"  # Move down
            direction = "A" if direction == "D" else "D"  # Change direction
            for j in range(m if direction == "A" else col_with_tree):
                path += direction
            path += "S" if i != n - 1 else ""  # Move down if not at the last row
        else:
            # If the current row is not the row with the tree or the row before it
            for j in range(m - 1):
                path += direction
            path += "S" if i != n - 1 else ""  # Move down if not at the last row
            direction = "A" if direction == "D" else "D"  # Change direction

    return path

def write_output(output_file, valids):
    with open(output_file, "w") as file:
        for valid in valids:
            file.write(valid + "\n")

def parse(lines, input_file, output_file):
    K = int(lines[0].split(" ")[0])
    lines = lines[1:]

    # level 1
    # freqs = []

    # level 2
    # coords = []

    # level 3
    # valids = []

    for k in range(K):
        # w, d, s, a = get_freq(path)
        # freq = (w, d, s, a)

        # level 2
        # n, m = smalles_rect(path)
        # coord = (n, m)
        # coords.append(coord)

        # level 3
        coord = lines[0].split(" ")
        m, n = int(coord[0]), int(coord[1])
        lawn = [[0 for j in range(m)] for i in range(n)]
        lines = lines[1:]
        for i in range(n):
            for j in range(m):
                lawn[i][j] = 0 if lines[i][j] == "." else -1
        lines = lines[n:]
        # path = lines[0].replace('\n', "")
        # lines = lines[1:]
        
        # levele 3
        # if is_valid_path(m, n, lawn, path):
        #     valids.append("VALID")
        # else:
        #     valids.append("INVALID")

        # level 4
        line_with_tree = -1;
        col_with_tree = -1;
        for i in range(n):
            for j in range(m):
                if lawn[i][j] == -1:
                    line_with_tree = i
                    col_with_tree = j
                    break
            if line_with_tree != -1:
                break

        path = find_path(m, n, lawn, line_with_tree, col_with_tree)
        if is_valid_path(m, n, lawn, path):
            print("VALID")
        else:
            print("INVALID")

        # level 1
        # freqs.append(freq)
    # write_output(output_file, valids)


def read():
    # For the example input
    level = "4"
    input_file = "input/level"+level+"/level"+level+"_example.in"
    output_file = "output/level"+level+"/level"+level+"_example.out"
    with open(input_file, "r") as file:
        lines = file.read().splitlines()
        parse(lines, input_file, output_file)

    # For the tests
    # level = "4"
    # for i in range(1, 6):
    #     input_file = "input/level"+level+"/level"+level+"_"+str(i)+".in"
    #     output_file = "output/level"+level+"/level"+level+"_"+str(i)+".out"
    #     with open(input_file, "r") as file:
    #         lines = file.read().splitlines()
    #         parse(lines, input_file, output_file)



read()