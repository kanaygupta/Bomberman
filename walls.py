"""Walls are added in the b.game 2 d matrix"""

from board import b


def add_walls():
    for i in range(b.actual_x - 1):
        if(i % 4 == 2):
            for j in range(b.actual_y - 1):
                if (j % 3 == 2):
                    b.game[i][j] = 'X'
