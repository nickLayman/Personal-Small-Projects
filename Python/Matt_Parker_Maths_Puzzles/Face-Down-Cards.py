# 1 is face up
# 0 is face down

import random

length = 4
cards = []
for card_num in range(length):
    cards.append(random.randint(0, 1))


def check_solved():
    for card in cards:
        if card == 1:
            return False
    return True


def flip(position):
    if cards[position] == 1:
        cards[position] = 0
    else:
        cards[position] = 1


def solve_cards(deck):
    if len(deck) > 1:
        return solve_cards(deck[1:])
    if len(deck) == 1:
        if deck[0] == 1:
            deck[0] = 0
        else:
            deck[0] = 1
        

all_decks = [[]]


def make_all_decks():
    global all_decks
    while len(all_decks[0]) < length:
        new_all_decks = []
        for deck in all_decks:
            new_all_decks.append(deck + [0])
            new_all_decks.append(deck + [1])
        all_decks = new_all_decks


make_all_decks()
for deck in all_decks:
    cards = deck
    print(deck)
