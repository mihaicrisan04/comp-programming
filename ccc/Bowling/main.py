

def solve(line: str) -> int:
    num_throws = int(line[0])
    line = line[2:]
    num_list = [int(x) for x in line.split(",")]
    for i in range(len(num_list)):
        pass
    print(num_throws, num_list)

with open("input.in", "r") as file:
    lines = file.read().splitlines()
    for line in lines:
        print(line) # line is a string
        print(solve(line)) # solve(line) is an int