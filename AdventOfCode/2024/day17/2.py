import re 

# with open('test.txt', 'r') as f:
# with open('test2.txt', 'r') as f:
with open('input.txt', 'r') as f:
    data = f.read().splitlines()

a = int(re.search(r'\d+', data[0]).group())
b = int(re.search(r'\d+', data[1]).group())
c = int(re.search(r'\d+', data[2]).group())
programs = [int(num) for num in data[4].split()[1].split(',')]

def combo(operand):
    match operand:
        case 0 | 1 | 2 | 3: return operand
        case 4: return a
        case 5: return b
        case 6: return c
        case 7: return -1


found = False
a = 0
while not found:
    b, c = 0, 0
    out = []
    ca = a

    i = 0
    run = True
    while i < len(programs) and run:
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
            case 5: 
                out.append(combo(operand) % 8)
                if len(out) > len(programs): run = False
                if len(out) > 0 and out[len(out) - 1] != programs[len(out) - 1]: run = False
            case 6:
                op1 = a
                op2 = combo(operand) 
                b = op1 // (2**op2)
            case 7:
                op1 = a
                op2 = combo(operand) 
                c = op1 // (2**op2)

        if iter_flag: i += 2

    if programs == out: found = True; print(ca); break
    a = ca + 1


