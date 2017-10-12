from person import Person

from input import _Getch, _GetchUnix
from termcolor import colored, cprint
from board import Board, b
from brick import all_bricks
from walls import add_walls
from bomb import Bomb
from enemy import Enemy, enemy_array, ini
import os
import time

'''Bomber man main class inherited person class'''


class Bomberman(Person):

    # Constructor
    def __init__(self, x=1, y=1):
        Person.__init__(self, x, y)
        self.bombs = 0
    # To check condition so that person can not plant more than 1 bomb
        b.game[x][y] = 'P'

    '''Function to check if the coordinates are in bounds of the board or not
    This uses the board copordinates from the b object
    '''

    def check_bound(self, x, y):
        if x >= b.up + 1 and x <= b.down - 1:
            if y >= b.left + 1 and y <= b.right - 1:
                return True
            else:
                return False
        else:
            return False

    '''Function to move the bomberman with change in x and y given as parameters
    Return values -1 if person is there 0 if move was unsuccessful 1 for successful move
    '''

    def move_bomberman(self, dx, dy):
        x = self.x + dx
        y = self.y + dy
        if self.check_bound(
                x,
                y) and b.game[x][y] != '/' and b.game[x][y] != 'X' and b.game[x][y] != 'B':
            if b.game[x][y] == 'E':
                return -1
            b.game[self.x][self.y] = ' '
            b.game[x][y] = 'P'
            self.x = x
            self.y = y
            return 1
        else:
            return 0


    ''' Main move function of the bomberman
        Main fucntion of the code:Features-
        1. Scan characters from the stdin buffer
        2. Also decreses the bomb counter
        3. Handles the explosion of the bomb
    '''
    def move(self, level):

    #Character read from imput function'''
        getch = _Getch()
        key = getch()
        return_value = 0

        '''Movement accordind to keys'''
        if key is 'w':
            return_value = self.move_bomberman(-1, 0)

        elif key is 's':
            return_value = self.move_bomberman(+1, 0)

        elif key is 'a':
            return_value = self.move_bomberman(0, -1)

        elif key is 'd':
            return_value = self.move_bomberman(0, +1)

        elif key is 'q':
            return -2

        '''If pressed q exit the game right there'''

        '''Function to handle the bomb and its timers'''
        if self.bombs == 1:
# Decrease yhe bomb timer
            self.p_bomb.tick_tick(self.x, self.y, level)
            b.game[self.p_bomb.x][self.p_bomb.y] = 'B'
# If time is over call the neighbour function which displays
# explosion around the bomb
            if(self.p_bomb.time_bomb == 0):

# Displays the board and calls the neighbour also
# call the function so that it calls the explosion and checks
# for different objects around the bomb
                temp = self.p_bomb.tick_tick(self.x, self.y, level)

# Set the bombs to 0 and del the bomb object
                self.bombs = 0
                del self.p_bomb

                if temp is -1:
                    return -1

        elif (key is 'b') and self.bombs == 0:
            '''Add new bomb if the key is b and bombs are 0'''
            self.p_bomb = Bomb(self.x, self.y, time.time())
            b.game[self.p_bomb.x][self.p_bomb.y] = 'B'
            self.bombs = 1

        # Returns return_value which stores the status of the moves
        return return_value


def move_poly(obj_type, level, x=0, y=0, type_easy=0):
    if isinstance(obj_type, Bomberman):
        return obj_type.move(level)
    else:
        return obj_type.move(level, x, y, type_easy)


''' Main function which maintains levels,lives and all the objects of different classes'''


def main():
    '''Initialisation:
    level - to store current level
    lives to store number of lives
    type_easy - easy bot
    type_hard-hard bot'''
    level = 1
    lives = 0
    type_easy = 1
    type_hard = 2

    while(level <= 3):
        '''Create bomberman and reinitialise the board as well as bricks and walls'''
        p = Bomberman()
        b.initialise_board()
        all_bricks()
        add_walls()
        ini(level)
        b.renderer(level)
        lives = 0

        while(lives <= 2):

            return_value = 0
            lives = lives + 1

            while(True):

                # if all the enemies are killed break the loop
                if len(enemy_array) == 0:
                    break

                # move the bomberman
                return_value = move_poly(p, level)

                # -1 tells that enemy has caught the person
                if return_value is -1:
                    break
                # -2 tells that user has enetered q
                if return_value is -2:
                    return

                flag = 0

                # Move all the enemies one by one
                # From second level onwards every fourth enemy is a medium bot
                for i in enemy_array:

                    if enemy_array.index(i) % 4 != 1:
                        temp = move_poly(i, level, p.x, p.y, type_easy)
                    else:
                        temp = move_poly(i, level, p.x, p.y, type_hard)

                    if temp is -1:
                        flag = 1

                # To display hard enemies with different colours replaced E
                # with e and took into account in the renderer function
                for i in enemy_array:
                    if enemy_array.index(i) % 4 == 1 and level >= 2:
                        b.game[i.x][i.y] = 'e'

                # Add the time left for explosion to the b.game string which is
                # accountes in the renderer function
                if p.bombs == 1 and p.p_bomb.time_bomb > 1:
                    b.game[p.p_bomb.x][p.p_bomb.y] = str(
                        p.p_bomb.time_bomb - 1)

                # Call to renderer after all the moves have been done
                b.renderer(level)

                '''Replacing e with E as all the functions have E for enemy'''
                for i in enemy_array:
                    if enemy_array.index(i) % 4 != 1:
                        pass
                    else:
                        b.game[i.x][i.y] = 'E'

                # Flag is 1 only when an emey catches the bomberman or bomber
                # man moves towards the enemy
                if flag is 1:
                    break
                # No. of lives left
                print("Lives left are", 3 - lives, ' and score is ', b.score)

            '''Vacate the current position of the bomberman and reinitialise the bomberman at the starting point'''
            b.game[p.x][p.y] = ' '
            p.x = 1
            p.y = 1
            b.game[1][1] = 'P'
            '''Some sleep so that player could see how it got killed'''
            time.sleep(1.5)

            '''If level is complete move to next level'''
            if len(enemy_array) == 0:
                level = level + 1
                break

        if lives == 3:
            break


main()
