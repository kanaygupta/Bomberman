import os
from termcolor import colored, cprint
import sys


class Board():
    # Constuctor
    def __init__(self, x, y):
        self.game = []
        self.left = 0
        self.right = y - 1
        self.up = 0
        self.down = x - 1
        self.actual_x = x
        self.actual_y = y
        self.score = 0

    # Initialisation after every level
    def initialise_board(self):

        self.game = []
        for i in range(self.actual_x):
            temp = []
            for j in range(self.actual_y):
                if j is 0:
                    temp.append('X')
                elif j is self.actual_y - 1:
                    temp.append('X')
                else:
                    temp.append(' ')
            self.game.append(temp)

        self.game[1][1] = 'P'

        for i in range(self.actual_y):
            self.game[0][i] = 'X'

        for i in range(self.actual_y):
            self.game[self.actual_x - 1][i] = 'X'

        for i in range(self.actual_x):
            self.game[i][0] = 'X'

        for i in range(self.actual_x):
            self.game[i][self.actual_y - 1] = 'X'

    '''Main function which clears the screen and prints the values'''

    def renderer(self, level):

        os.system('clear')
        print("LEVEL:", level)

        for i in range(2 * self.actual_x):
            for j in range(0, 4 * self.actual_y, 4):
                a = int(i / 2)
                d = int(j / 4)

                if(b.game[a][d] == '/'):
                    cprint('****', 'yellow', attrs=['bold'], end='')

                elif(b.game[a][d] == 'P' and i % 2 == 0):
                    cprint("[^^]", 'red', attrs=['bold'], end='')

                elif(b.game[a][d] == 'P' and i % 2 == 1):
                    cprint(" ][ ", 'red', attrs=['bold'], end='')

                elif(b.game[a][d] == 'E' and i % 2 == 0):
                    cprint("}(){", 'magenta', attrs=['bold'], end='')

                elif(b.game[a][d] == 'E' and i % 2 == 1):
                    cprint(" () ", 'magenta', attrs=['bold'], end='')

                elif(b.game[a][d] == 'e' and i % 2 == 0):
                    cprint("}(){", 'blue', attrs=['bold'], end='')

                elif(b.game[a][d] == 'e' and i % 2 == 1):
                    cprint(" () ", 'blue', attrs=['bold'], end='')

                elif(b.game[a][d] == 'B' or b.game[a][d] == '@'):
                    cprint('@@@@', 'green', attrs=['bold'], end='')

                elif(b.game[a][d] >= '0' and b.game[a][d] <= '4'):
                    cprint(
                        b.game[a][d] +
                        b.game[a][d] +
                        b.game[a][d] +
                        b.game[a][d],
                        'green',
                        attrs=['bold'],
                        end='')

                else:
                    cprint(
                        b.game[a][d] +
                        b.game[a][d] +
                        b.game[a][d] +
                        b.game[a][d],
                        end='')

            print("")


b = Board(20, 25)
b.initialise_board()
b.renderer(1)
