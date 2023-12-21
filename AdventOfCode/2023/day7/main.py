# Day: 7

def read_file():
    file_name = 'data.in'
    with open(file_name, 'r') as f:
        lines = f.readlines()
        return lines

cards = '0123456789TJQKA'
types = [[], [], [], [], [], [], []]

def cmp(a, b):
    for i in range(5):
        if cards.index(a[i]) > cards.index(b[i]):
            return 1
        if cards.index(a[i]) < cards.index(b[i]):
            return -1
    return 0

def insert_hand(hand, type, score):
    for i in range(len(types[type])):
        if cmp(hand, types[type][i][0]) < 0:
            types[type].insert(i, (hand, score))
            return
    types[type].append((hand, score))

def five_of_a_kind(hand):
    if hand[0] == hand[1] == hand[2] == hand[3] == hand[4]:
        return True
    return False

def four_of_a_kind(hand):
    f = [0] * 15
    for card in hand:
        f[cards.index(card)] += 1
    for i in range(14):
        if f[i] == 4:
            return True
    return False

def full_house(hand):
    f = [0] * 15
    for card in hand:
        f[cards.index(card)] += 1
    for i in range(14):
        if f[i] == 3:
            for j in range(14):
                if f[j] == 2:
                    return True
    return False

def three_of_a_kind(hand):
    f = [0] * 15
    for card in hand:
        f[cards.index(card)] += 1
    for i in range(14):
        if f[i] == 3:
            return True
    return False

def two_pair(hand):
    f = [0] * 15
    for card in hand:
        f[cards.index(card)] += 1
    for i in range(14):
        if f[i] == 2:
            for j in range(i + 1, 14):
                if f[j] == 2:
                    return True
    return False

def one_pair(hand):
    f = [0] * 15
    for card in hand:
        f[cards.index(card)] += 1
    for i in range(14):
        if f[i] == 2:
            return True
    return False

def main() -> None:
    lines = read_file()

    for line in lines:
        hand, score = line.strip().split(' ')
        score = int(score)
        
        if five_of_a_kind(hand):
            insert_hand(hand, 6, score)
            continue
        
        if four_of_a_kind(hand):
            insert_hand(hand, 5, score)
            continue

        if full_house(hand):
            insert_hand(hand, 4, score)
            continue

        if three_of_a_kind(hand):
            insert_hand(hand, 3, score)
            continue

        if two_pair(hand):
            insert_hand(hand, 2, score)
            continue

        if one_pair(hand):
            insert_hand(hand, 1, score)
            continue

        insert_hand(hand, 0, score)

    sol = 0
    rank = 1
    for i in range(7):
        print(types[i])
        for j in range(len(types[i])):
            sol += rank * types[i][j][1]
            rank += 1

    print(sol)


if __name__ == '__main__':
    main()  