
with open('input.txt', 'r') as f:
# with open('test.txt', 'r') as f:
    lines = f.read().splitlines()


flag = False
rules = {}
updates = []

for line in lines:
    if line == '':
        flag = True
        continue
    if not flag:
        rule = line.split('|')
        key, constraint = map(int, rule)
        if key not in rules:
            rules[key] = [constraint]
        else:
            rules[key].append(constraint)
    else:
        update = [int(x) for x in line.split(',')]
        updates.append(update)

for key, value in rules.items():
    value.sort()

def isCorrect(update) -> bool:
    for i in range(len(update)):
        if update[i] in rules:
            for j in range(i):
                if update[j] in rules[update[i]]:
                    return False
    return True

def getCorrect(update) -> list:
    correct = []
    for e in update:
        if len(correct) == 0:
            correct.append(e)
            continue

        for i in range(len(correct), -1, -1):
            correct.insert(i, e)
            if isCorrect(correct):
                break
            correct.pop(i)
    return correct

sol = 0
for update in updates:
    if not isCorrect(update):
        update = getCorrect(update)
        l, r = 0, len(update) - 1
        sol += update[(l + r) // 2]

print(sol)
