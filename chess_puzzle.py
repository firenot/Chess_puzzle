def delta(value_1, value_2):
    return abs(value_1 - value_2)


def move_horizontal_or_vertical(letter_start, letter_finish, number_start, number_finish):
    if letter_start == letter_finish or number_start == number_finish:
        return True


def move_diagonal(letter_start, letter_finish, number_start, number_finish):
    if delta(letter_start, letter_finish) == delta(number_start, number_finish):
        return True


def pawn(letter_start, letter_finish, number_start, number_finish):
    if letter_start == letter_finish and delta(number_start, number_finish) == 1:
        return True


def elephant(letter_start, letter_finish, number_start, number_finish):
    if move_diagonal(letter_start, letter_finish, number_start, number_finish):
        return True


def rook(letter_start, letter_finish, number_start, number_finish):
    if move_horizontal_or_vertical(letter_start, letter_finish, number_start, number_finish):
        return True


def horse(letter_start, letter_finish, number_start, number_finish):
    if delta(letter_start, letter_finish) == 2 and delta(number_start, number_finish) == 1:
        return True
    elif delta(letter_start, letter_finish) == 1 and delta(number_start, number_finish) == 2:
        return True


def king(letter_start, letter_finish, number_start, number_finish):
    if delta(letter_start, letter_finish) <= 1 and delta(number_start, number_finish) <= 1:
        return True


def queen(letter_start, letter_finish, number_start, number_finish):
    if (move_diagonal(letter_start, letter_finish, number_start, number_finish) or move_horizontal_or_vertical(
            letter_start, letter_finish, number_start, number_finish)):
        return True


def definition_figure(figure):
    if figure.lower() == 'пешка':
        return pawn(letter_start, letter_finish, number_start, number_finish)
    elif figure.lower() == 'слон':
        return elephant(letter_start, letter_finish, number_start, number_finish)
    elif figure.lower() == 'ладья':
        return rook(letter_start, letter_finish, number_start, number_finish)
    elif figure.lower() == 'конь':
        return horse(letter_start, letter_finish, number_start, number_finish)
    elif figure.lower() == 'король':
        return king(letter_start, letter_finish, number_start, number_finish)
    elif figure.lower() == 'королева':
        return queen(letter_start, letter_finish, number_start, number_finish)


letters = 'ABCDEFGH'
trajectory, figure = input(), input()
trajectory_start, trajectory_finish = trajectory.split('-')
letter_start, number_start = int(letters.find(trajectory_start[0])) + 1, int(trajectory_start[1])
letter_finish, number_finish = int(letters.find(trajectory_finish[0])) + 1, int(trajectory_finish[1])

if definition_figure(figure):
    print('Да')
else:
    print('Нет')
