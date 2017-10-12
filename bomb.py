from board import b
from enemy import enemy_array
import time

# Bomb class


class Bomb():
    '''Constructor
    contains  coordinates and time of creation as well as frames for explosion
    Explosion will take place if the variable becomes 0
    '''

    def __init__(self, x, y, time):
        self.x = x
        self.y = y
        self.time_created = time
        self.time_bomb = 4

    # function for decresing the time left and calling the explosion of time
    # runs out
    def tick_tick(self, x, y, level):
        if self.time_bomb == 0:
            return self.__explode(x, y, level)
        else:
            self.time_bomb = self.time_bomb - 1

    # Function to display @ in the last frame of explosion
    def __neighbour(self):
        direc = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
        for i, j in direc:
            x = self.x + i
            y = self.y + j

            if b.game[x][y] == ' ':
                b.game[x][y] = '@'

    '''ain function for explode
	Takes coordinates of man as well for the case when man is on the bomb itself
	'''

    def __explode(self, man_x, man_y, level):
        # Adjacent frames are made to @

        self.__neighbour()
        b.renderer(level)
        time.sleep(0.05)
        # All possible directions
        direc = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
        return_value = 0

        for i, j in direc:

            x = self.x + i
            y = self.y + j

            # If man is on adjacent block or on the same block returns -1
            if(b.game[x][y] == 'P' or (man_x == x and man_y == y)):
                b.game[x][y] = ' '
                b.game[self.x][self.y] = ' '
                return_value = -1

            # If brick is there add 20 points to the score of the board
            elif (b.game[x][y] == '/'):
                b.score = b.score + 20
                b.game[x][y] = ' '

            # If enemy is there Find the enemy and remove the enemy from the
            # enemy_array and add 100 points to the score
            elif b.game[x][y] == 'E':
                for i in enemy_array:
                    if(i.x == x and i.y == y):
                        b.score = b.score + 100
                        b.game[x][y] = ' '
                        enemy_array.remove(i)

            # Remove @ generted after the explosion
            if b.game[x][y] == '@' or b.game[x][y] == 'B':
                b.game[x][y] = ' '

        # Remove all the elements from the neighbourhood after the explosion
        for i, j in direc:
            if b.game[i][j] != 'X':
                b.game[i][j] = ' '

        return return_value
