import re 

# with open('test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    data = f.read().splitlines()

a = int(re.search(r'\d+', data[0]).group())
b = int(re.search(r'\d+', data[1]).group())
c = int(re.search(r'\d+', data[2]).group())
programs = [int(num) for num in data[4].split()[1].split(',')]
out = []

def combo(operand):
    match operand:
        case 0 | 1 | 2 | 3: return operand
        case 4: return a
        case 5: return b
        case 6: return c
        case 7: return -1

i = 0
while i < len(programs):
    iter_flag = True

    opcode = programs[i]
    operand = programs[i+1]

    match opcode:
        case 0: 
            op1 = a
            op2 = combo(operand) 
            a = op1 // (2**op2)
        case 1: b = b ^ operand
        case 2: b = combo(operand) % 8
        case 3:
            if a != 0: i = operand; iter_flag = False
        case 4: b = b ^ c
        case 5: out.append(combo(operand) % 8)
        case 6:
            op1 = a
            op2 = combo(operand) 
            b = op1 // (2**op2)
        case 7:
            op1 = a
            op2 = combo(operand) 
            c = op1 // (2**op2)

    if iter_flag: i += 2


print(",".join(map(str, out)))

