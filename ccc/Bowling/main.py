

def solve(line: str) -> None:
    num_throws = int(line[0])
    line = line[2:]
    num_list = [int(x) for x in line.split(",")]

    sol = ""
    sum = 0
    strike = False
    spare = False
    length = len(num_list)

    i = 1
    j = 0

    while i <= num_throws:
        if strike:
            sum += num_list[j] + num_list[j + 1] + num_list[j + 2]
            strike = False
            j += 1
        elif spare:
            sum += num_list[j] + num_list[j + 1]
            spare = False
            j += 2
        else:
            sum += num_list[j] + num_list[j + 1]
            if num_list[j] + num_list[j + 1] == 10:
                spare = True
            if num_list[j] == 10:
                strike = True
            j += 2
        sol += str(sum) + ","
        i += 1

    print(sol[:(len(sol) - 1)])
    

with open("input.in", "r") as file:
    lines = file.read().splitlines()
    for line in lines:
        # print(line) # line is a string
        solve(line)