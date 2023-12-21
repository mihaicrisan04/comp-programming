# # Day: 7

# def read_file():
#     file_name = 'data.in'
#     with open(file_name, 'r') as f:
#         lines = f.readlines()
#         return lines

# cards = '0123456789TJQKA'
# types = [[], [], [], [], [], [], []]

# def cmp(a, b):
#     for i in range(5):
#         if cards.index(a[i]) > cards.index(b[i]):
#             return 1
#         if cards.index(a[i]) < cards.index(b[i]):
#             return -1
#     return 0

# def insert_hand(hand, type, score):
#     for i in range(len(types[type])):
#         if cmp(hand, types[type][i][0]) < 0:
#             types[type].insert(i, (hand, score))
#             return
#     types[type].append((hand, score))

# def five_of_a_kind(hand):
#     if hand[0] == hand[1] == hand[2] == hand[3] == hand[4]:
#         return True
#     return False

# def four_of_a_kind(hand):
#     f = [0] * 15
#     for card in hand:
#         f[cards.index(card)] += 1
#     for i in range(14):
#         if f[i] == 4:
#             return True
#     return False

# def full_house(hand):
#     f = [0] * 15
#     for card in hand:
#         f[cards.index(card)] += 1
#     for i in range(14):
#         if f[i] == 3:
#             for j in range(14):
#                 if f[j] == 2:
#                     return True
#     return False

# def three_of_a_kind(hand):
#     f = [0] * 15
#     for card in hand:
#         f[cards.index(card)] += 1
#     for i in range(14):
#         if f[i] == 3:
#             return True
#     return False

# def two_pair(hand):
#     f = [0] * 15
#     for card in hand:
#         f[cards.index(card)] += 1
#     for i in range(14):
#         if f[i] == 2:
#             for j in range(i + 1, 14):
#                 if f[j] == 2:
#                     return True
#     return False

# def one_pair(hand):
#     f = [0] * 15
#     for card in hand:
#         f[cards.index(card)] += 1
#     for i in range(14):
#         if f[i] == 2:
#             return True
#     return False

# def main() -> None:
#     lines = read_file()

#     for line in lines:
#         hand, score = line.strip().split(' ')
#         score = int(score)
        
#         if five_of_a_kind(hand):
#             insert_hand(hand, 6, score)
#             continue
        
#         if four_of_a_kind(hand):
#             insert_hand(hand, 5, score)
#             continue

#         if full_house(hand):
#             insert_hand(hand, 4, score)
#             continue

#         if three_of_a_kind(hand):
#             insert_hand(hand, 3, score)
#             continue

#         if two_pair(hand):
#             insert_hand(hand, 2, score)
#             continue

#         if one_pair(hand):
#             insert_hand(hand, 1, score)
#             continue

#         insert_hand(hand, 0, score)

#     sol = 0
#     rank = 1
#     for i in range(7):
#         print(types[i])
#         for j in range(len(types[i])):
#             sol += rank * types[i][j][1]
#             rank += 1

#     print(sol)


# if __name__ == '__main__':
#     main()  

import re
from functools import cmp_to_key
from collections import Counter

with open('/Users/mihaicrisan/Developer/competitive porgramming/AdventOfCode/2023/day7/data.in', 'r') as f:
    puzzle_input = f.read()


def part1(puzzle_input):

    def get_type(hand):
        counts = sorted(Counter(hand).values(), reverse=True)
        if counts[0] == 5:
            return 6
        if counts[0] == 4:
            return 5
        if counts[0] == 3 and counts[1] == 2:
            return 4
        if counts[0] == 3:
            return 3
        if counts[0] == 2 and counts[1] == 2:
            return 2
        if counts[0] == 2:
            return 1
        return 0  
      
    def compare(a, b):
        type_a = get_type(a[0])
        type_b = get_type(b[0])
        if type_a > type_b:
            return 1
        if type_a < type_b:
            return -1
        for card_a, card_b in zip(a[0], b[0]):
            if card_a == card_b:
                continue
            a_wins = (cards.index(card_a) > cards.index(card_b))
            return 1 if a_wins else -1

    cards = '23456789TJQKA'
    regex = r'(\w{5}) (\d+)'
    hands = re.findall(regex, puzzle_input)
    hands.sort(key=cmp_to_key(compare))
    total = 0
    for rank, (_, bid) in enumerate(hands, start=1):
        total += rank * int(bid)
    return total
    

def part2(puzzle_input):

    def get_type(hand):
        jokers = hand.count('J')
        hand = [c for c in hand if c != 'J']
        counts = sorted(Counter(hand).values(), reverse=True)
        if not counts:
            counts = [0]
        if counts[0] + jokers == 5:
            return 6
        if counts[0] + jokers == 4:
            return 5
        if counts[0] + jokers == 3 and counts[1] == 2:
            return 4
        if counts[0] + jokers == 3:
            return 3
        if counts[0] == 2 and (jokers or counts[1] == 2):
            return 2
        if counts[0] == 2 or jokers:
            return 1
        return 0
    
    def compare(a, b):
        type_a = get_type(a[0])
        type_b = get_type(b[0])
        if type_a > type_b:
            return 1
        if type_a < type_b:
            return -1
        for card_a, card_b in zip(a[0], b[0]):
            if card_a == card_b:
                continue
            a_wins = (cards.index(card_a) > cards.index(card_b))
            return 1 if a_wins else -1

    cards = 'J23456789TQKA'
    regex = r'(\w{5}) (\d+)'
    hands = re.findall(regex, puzzle_input)
    hands.sort(key=cmp_to_key(compare))
    total = 0
    for rank, (_, bid) in enumerate(hands, start=1):
        total += rank * int(bid)
    return total


print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))