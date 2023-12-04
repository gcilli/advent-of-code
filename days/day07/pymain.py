from utilities.pyutils import *

from collections import defaultdict


def get_hand_value(hand, use_j_as_jolly=False):
    card_value = {str(i): int(i) for i in range(2, 10)}
    card_value['T'] = 10
    card_value['J'] = 1 if use_j_as_jolly else 11
    card_value['Q'] = 12
    card_value['K'] = 13
    card_value['A'] = 14

    hand_value = 0
    cards = defaultdict(int)
    for i, card in enumerate(hand):
        cards[card] += 1
        hand_value += 16**(5 - i) * card_value[card]

    if use_j_as_jolly and 'J' in cards.keys() and cards['J'] != 5:
        cards_without_j = {card: amount for card,
                           amount in cards.items() if card != 'J'}
        card_in_highest_quantity = sorted(
            list(cards_without_j.items()), key=lambda x: x[1], reverse=True)[0][0]
        hand = hand.replace('J', card_in_highest_quantity)
        cards[card_in_highest_quantity] += cards['J']
        cards.pop('J', None)

    # five of a kind
    if len(cards) == 1:
        return hand_value + 16**12

    # either full house or four of a kind
    if len(cards) == 2:
        return hand_value + 16**(11 if max(list(cards.values())) == 4 else 10)

    # either three of a kind or two pairs
    if len(cards) == 3:
        return hand_value + 16**(9 if max(list(cards.values())) == 3 else 8)

    # one pair
    if len(cards) == 4:
        return hand_value + 16**7

    # high card
    if len(cards) == 5:
        return hand_value + 16**6


def solve_part_one():
    content = read_input(day=7)
    content = [(line.split()[0], int(line.split()[1])) for line in content]
    content.sort(key=lambda hand: get_hand_value(hand[0]))
    ans = sum([i*c[1] for i, c in enumerate(content, 1)])
    print(f"part 1: {ans}")


def solve_part_two():
    content = read_input(day=7)
    content = [(line.split()[0], int(line.split()[1])) for line in content]
    content.sort(key=lambda hand: get_hand_value(hand[0], use_j_as_jolly=True))
    ans = sum([i*c[1] for i, c in enumerate(content, 1)])
    print(f"part 2: {ans}")


if __name__ == "__main__":
    solve_part_one()
    solve_part_two()
