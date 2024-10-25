import re
import copy

diri = [0, 1, 0, -1]
dirj = [1, 0, -1, 0]

def write_sol(s, input_file, output_file):
    # Write the output to a file when solving the problem
    with open(output_file, "w") as file:
        for i in range(len(s)):
            file.write("\n")
            for row in s[i]:
                for elem in row:
                    if elem == 1:
                        file.write("X")
                    else:
                        file.write(".")
                file.write("\n")


def parse(lines, input_file, output_file):
    n = int(lines[0])
    lines = lines[1:]

    sol = []

    for line in lines:
        values = line.split(" ")
        x = int(values[0])
        y = int(values[1])
        k = int(values[2])

        mat = [[0 for i in range(x)] for j in range(y)]

        i = 0
        while i < y:
            for j in range(0, x, 2):
                if i + 2 <= y:
                    for m in range(2):
                        if i + m < y:
                            mat[i+m][j] = 1

            i += 3

        # if y % 4 == 1 or y % 4 == 2:
        #     if y % 4 == 1:
        #         cut = 1
        #     if y % 4 == 2:
        #         cut = 2

        #     j = 0
        #     while j + 3 <= x:
        #         for m in range(3):
        #             mat[y - cut][j + m] = 1
        #         j += 4
                
        sol.append(mat)

    # for s in sol:
    #     for row in s:
    #         print(row)
    #     print()

   
    write_sol(sol, input_file, output_file)


def read():
    # For the example input
    lvl = "5"
    input_file = "input/level" + lvl + "/level" + lvl + "_example.in"
    output_file = "output/level" + lvl + "/level" + lvl + "_example.out"
    with open(input_file, "r") as file:
        lines = file.read().splitlines()
        parse(lines, input_file, output_file)

    # For the tests
    # level = "5"
    # for i in range(1, 6):
    #     input_file = "input/level"+level+"/level"+level+"_"+str(i)+".in"
    #     output_file = "output/level"+level+"/level"+level+"_"+str(i)+".out"
    #     with open(input_file, "r") as file:
    #         lines = file.read().splitlines()
    #         parse(lines, input_file, output_file)


read()