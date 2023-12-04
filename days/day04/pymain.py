from utilities.pyutils import *


def solve_part_one():
    content = read_input(day=4)

    content = [line.split(':')[1].split('|') for line in content]
    win_cards = [list(map(int, game[0].split())) for game in content]
    my_cards = [list(map(int, game[1].split())) for game in content]

    ans = 0
    for i in range(len(win_cards)):
        game_win_cards = win_cards[i]
        game_my_cards = my_cards[i]
        num_winning_cards = 0
        for card in game_win_cards:
            if card in game_my_cards:
                num_winning_cards += 1
        ans += 2**(num_winning_cards-1) if num_winning_cards > 0 else 0

    print(f"part 1: {ans}")


def solve_part_two():
    content = read_input(day=4)

    content = [line.split(':')[1].split('|') for line in content]
    win_cards = [list(map(int, game[0].split())) for game in content]
    my_cards = [list(map(int, game[1].split())) for game in content]

    copies = {i: 1 for i in range(len(win_cards))}
    ans = 0
    for i in range(len(win_cards)):
        game_win_cards = win_cards[i]
        game_my_cards = my_cards[i]
        num_winning_cards = 0
        for card in game_win_cards:
            if card in game_my_cards:
                num_winning_cards += 1
        for j in range(i+1, i+1+num_winning_cards):
            copies[j] += copies[i]

    ans = sum(list(copies.values()))

    print(f"part 2: {ans}")


if __name__ == "__main__":
    solve_part_one()
    solve_part_two()
