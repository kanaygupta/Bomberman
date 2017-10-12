
""" 4 Bricks are randomly  added to each row in the
2d matrix b.game and marked with /"""
from board import b
from random import randint


class brick:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def all_bricks():

    for i in range(3, b.actual_x - 1):

        if(i % 2 == 1):
            for j in range(4):
                a = randint(1, b.actual_y - 2)
                b.game[i][a] = '/'
        else:
            for j in range(4):
                a = randint(1, b.actual_y - 2)
                if b.game[i][a] != 'X':
                    b.game[i][a] = '/'
