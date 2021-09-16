def monop(finish_order, games_order):
    finish = 10 ** finish_order
    games = 10 ** games_order

    import random
    from random import shuffle
    from random import randint

    squares = []
    J = 0

    while len(squares) < 40:
        squares.append(0)

    games_finished = 0

    while games_finished < games:

        master_chest = [0, 40, 40, 40, 40, 10, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40]
        chest = [i for i in master_chest]
        shuffle(chest)

        master_chance = [0, 24, 11, 'U', 'R', 40, 40, 'B', 10, 40, 40, 5, 39, 40, 40, 40]
        chance = [i for i in master_chance]
        shuffle(chance)

        doubles = 0

        position = 0

        gos = 0

        while gos < finish:

            first_roll = random.randint(1, 6)
            second_roll = random.randint(1, 6)
            diceroll = first_roll + second_roll

            if first_roll == second_roll:
                doubles += 1
            else:
                doubles = 0
            if doubles >= 3:
                position = 10
                J += 1
            else:

                position = (position + diceroll) % 40

                if position in [7, 22, 33]:  # Chance
                    chance_card = chance.pop(0)
                    if len(chance) == 0:
                        chance = [i for i in master_chance]
                        shuffle(chance)
                    if chance_card != 40:

                        if isinstance(chance_card, int):
                            position = chance_card
                        elif chance_card == 'U':
                            while position not in [12, 28]:
                                position = (position + 1) % 40
                        elif chance_card == 'R':
                            while position not in [5, 15, 25, 35]:
                                position = (position + 1) % 40
                        elif chance_card == 'B':
                            position = position - 3

                elif position in [2, 17]:  # Community Chest
                    chest_card = chest.pop(0)
                    if len(chest) == 0:
                        chest = [i for i in master_chest]
                        shuffle(chest)
                    if chest_card != 40:
                        position = chest_card

                if position == 30:  # Go to jail
                    position = 10
                    J += 1

            squares.insert(position, (squares.pop(position) + 1))

            gos += 1

        games_finished += 1

    print(squares)
    squares_prob = []
    for i in squares:
        squares_prob.append(str(str(squares.index(i)) + "=" + str(i / (finish * games / 100))))
    print(squares_prob)
    print("In Jail=", J / (finish * games / 100))


monop(2, 2)
