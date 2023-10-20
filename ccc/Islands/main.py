import re
import copy

diri = [0, 1, 0, -1]
dirj = [1, 0, -1, 0]

def write_sol(n, m, a, s, input_file, output_file):
    # Write the output to a file when solving the problem
    with open(output_file, "w") as file:
        for i in range(m):

            ans = ""
            if s[i]:
                ans = "VALID"
            else:
                ans = "INVALID"

            file.write(ans + "\n")

def solve(n, m, b, s):
    pass

def fill(i, j, n, b):
    for k in range(4):
        ii = i+diri[k]
        jj = j+dirj[k]
        if ii >= 0 and ii < n and jj >= 0 and jj < n and b[ii][jj] == -1:
            b[ii][jj] = b[i][j]
            fill(ii, jj, n, b)
       
def check_intersections(n, b) -> bool:
    intersected = False
    for x in range(n-1):
        for y in range(n-1):
            if x - 1 > 0 and y - 1 > 0:
                if b[x-1][y-1] == b[x][y] - 1 and abs(b[x][y-1] - b[x-1][y]) == 1:
                    intersected = True
            if x - 1 > 0 and y + 1 < n:
                if b[x-1][y+1] == b[x][y] - 1 and abs(b[x][y+1] - b[x-1][y]) == 1:
                    intersected = True
            if x + 1 < n and y + 1 < n:
                if b[x+1][y+1] == b[x][y] - 1 and abs(b[x][y+1] - b[x+1][y]) == 1:        
                    intersected = True
            if x + 1 < n and y - 1 > 0:
                if b[x+1][y-1] == b[x][y] - 1 and abs(b[x][y-1] - b[x+1][y+1]) == 1:
                    intersected = True
    return intersected


def parse(lines, input_file, output_file):
    n = int(lines[0])
    lines = lines[1:]

    a = []
    s = []

    for line in range(n):
        arr = [char for char in lines[line]]
        a.append(arr)

    lines = lines[n:]

    m = int(lines[0])
    lines = lines[1:]

    for line in range(m):
        # Use regular expression to find and extract numbers
        numbers = re.findall(r'\d+', lines[line])

        # Convert the extracted strings to integers and add them to the list
        pos_list = [int(num) for num in numbers]

        s.append(pos_list)

    lines = lines[m:] # Clear the lines list

    # End of reading the input file
    ################################################



    # b as the input matrix using -1 and 0 for L and W respectively
    b = []
    for i in range(n):
        l = []
        for j in range(n):
            x = 0
            l.append(x)
        b.append(l)

    sol = []
    for i in range(m):
        # reset the matrix
        # bb = b.copy()
        for ii in range(n):
            for j in range(n):
                b[ii][j] = 0
        
        # fill the matrix with the road
        intersected = False
        k = 1
        for j in range(0, len(s[i]), 2):
            y = s[i][j]
            x = s[i][j+1]

            if b[x][y] != 0:
                intersected = True
            b[x][y] = k
            k += 1

            # if x - 1 > 0 and y - 1 > 0:
            #     if b[x-1][y-1] == k - 1 and abs(b[x][y-1] - b[x-1][y]) == 1:
            #         intersected = True
            # if x - 1 > 0 and y + 1 < n:
            #     if b[x-1][y+1] == k - 1 and abs(b[x][y+1] - b[x-1][y]) == 1:
            #         intersected = True
            # if x + 1 < n and y + 1 < n:
            #     if b[x+1][y+1] == k - 1 and abs(b[x][y+1] - b[x+1][y]) == 1:
            #         print("here")           
            #         intersected = True
            # if x + 1 < n and y - 1 > 0:
            #     if b[x+1][y-1] == k - 1 and abs(b[x][y-1] - b[x+1][y+1]) == 1:
            #         intersected = True
            
        
 
        # print("Case: ", i+1, s[i], intersected)
        # for i in range(n):
        #     print(b[i])
        # print()

        # check intersection function
        if (intersected == False):
            intersected = check_intersections(n, b)
        sol.append(not intersected)

    
    # Fill the conected islands
    # code = 0
    # for i in range(n):
    #     for j in range(n):
    #         if b[i][j] == -1:
    #             code += 1
    #             b[i][j] = code
    #             fill(i, j, n, b)

    write_sol(n, m, b, sol, input_file, output_file)

def read():
    # For the example input
    # input_file = "input/level3/level3_example.in"
    # output_file = "output/level3/level3_example.out"
    # with open(input_file, "r") as file:
    #     lines = file.read().splitlines()
    #     parse(lines, input_file, output_file)

    # For the tests
    level = "3"
    for i in range(1, 6):
        input_file = "input/level"+level+"/level"+level+"_"+str(i)+".in"
        output_file = "output/level"+level+"/level"+level+"_"+str(i)+".out"
        with open(input_file, "r") as file:
            lines = file.read().splitlines()
            parse(lines, input_file, output_file)


read() # Read the input file -> parse the input file -> store the input file in the variables