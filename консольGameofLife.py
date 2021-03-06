from random import choice

LIVE = '1'
DEAD = '0'
MAXIMAL = 15


def sosed(x, y):
    for dx, dy in (
            (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
            (-1, 1)):
                yield x+dx, y+dy


def empty_field():
    return [[DEAD for x in range(MAXIMAL)] for y in range(MAXIMAL)]


def show_field(field):
    for y in range(MAXIMAL):
        print(''.join(field[y]))


def live(field, sosed_x, sosed_y):
    return 0 <= sosed_x < MAXIMAL \
           and 0 <= sosed_y < MAXIMAL \
           and field[sosed_y][sosed_x] == LIVE


field = [
    [choice([DEAD, LIVE]) for x in range(MAXIMAL)] for y in range(MAXIMAL)]

while True:
    input('start game(please, write any letter or word): ')
    show_field(field)
    damper = empty_field()
    for y in range(MAXIMAL):
        for x in range(MAXIMAL):
            a = field[y][x]
            neighbours = 0
            for sosed_x, sosed_y in sosed(x, y):
                neighbours += 1 if live(field, sosed_x, sosed_y) else 0
            if a == DEAD:
                damper[y][x] = LIVE if neighbours == 3 else DEAD
            else:
                damper[y][x] = LIVE if neighbours in (2, 3) else DEAD

    if field == damper:
        print('stagantion')
        break
    field = damper
