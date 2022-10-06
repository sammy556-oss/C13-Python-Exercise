if __name__ == '__main__':
    points = int(input('Enter the number of points of the team ahead: '))
    points -= 3
    team_ahead_has_ball = bool(input('Enter True or False if the team ahead has the ball: '))
    if team_ahead_has_ball is True:
        points += 0.5
    else:
        points -= 0.5

    print('None')
