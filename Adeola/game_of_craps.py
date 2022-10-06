import random


def roll_dice():
    face1 = random.randrange(1, 6)
    face2 = random.randrange(1, 6)
    print(f'Player played {face1} and {face2}')
    return face2 + face1


def test_game_continuance(num1, point):
    if num1 == point:
        return True
    elif num1 == 7:
        return False
    else:
        print('Player rolls again')
        return None


if __name__ == '__main__':
    gameStatus = None
    myPoint = 0
    sum_of_dice = roll_dice()
    if sum_of_dice == 7 or sum_of_dice == 11:
        gameStatus = True
    elif sum_of_dice == 2 or sum_of_dice == 3 or sum_of_dice == 12:
        gameStatus = False
    else:
        gameStatus = None
        myPoint = sum_of_dice
        print(f'Player rolls again.\nPlayer\'s point is {myPoint}')

    while gameStatus is None:
        sum_of_dice = roll_dice()
        gameStatus = test_game_continuance(sum_of_dice, myPoint)

    if gameStatus:
        print('Player wins :)')
    else:
        print('Player loses :(')
