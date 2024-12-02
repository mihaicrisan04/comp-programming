

def allIncreasing(a):
    for i in range(len(a) - 1):
        if a[i] >= a[i + 1]:
            return False
    return True

def allDecreasing(a):
    for i in range(len(a) - 1):
        if a[i] <= a[i + 1]:
            return False
    return True

def absAtLeastOneAtMostThree(a):
    for i in range(len(a) - 1):
        if abs(a[i] - a[i + 1]) > 3 or abs(a[i] - a[i + 1]) < 1:
            return False
    return True

# with open('test.txt', 'r') as file:
with open('input.txt', 'r') as file:
    data = file.read().splitlines()
    sol = 0
    for line in data:
        a = [int(x) for x in line.split()]
        if (allIncreasing(a) or allDecreasing(a)) and absAtLeastOneAtMostThree(a):
            sol += 1
        else:
            for i in range(len(a)):
                b = a[:i] + a[i+1:]
                if (allIncreasing(b) or allDecreasing(b)) and absAtLeastOneAtMostThree(b):
                    sol += 1
                    break
    print(sol)

