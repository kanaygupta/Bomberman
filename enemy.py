from person import Person
from random import *
from board import b

'''Enemy class inherits from person class'''


class Enemy(Person):

    '''Constructor'''

    def __init__(self, x, y):
        Person.__init__(self, x, y)

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

    '''Function to move the enemy with change in x and y given as parameters
    Return values
    -1 if person is there
    0 if move was unsuccessful
    1 for successful move
    '''

    def move_enemy(self, dx, dy):

        x = self.x + dx
        y = self.y + dy

        # The new coordinates are x and y and checking for wall ,brick,bomb and
        # other enemy is done before making a move

        if self.check_bound(
                x,
                y) and b.game[x][y] != '/' and b.game[x][y] != 'X' and b.game[x][y] != 'B' and b.game[x][y] != 'E':

            # IF person is there return -1 to the calling function
            if b.game[x][y] == 'P':
                return -1

            # Enemy is moved to thenew coordinates
            b.game[self.x][self.y] = ' '
            b.game[x][y] = 'E'
            self.x = x
            self.y = y
            return 1
        else:
            return 0

    '''Manhattan distance betwwen two points for the advanced enemies'''

    def dist(self, x, y, person_x, person_y):
        return abs(x - person_x) + abs(y - person_y)

    '''Main move function.
    Features-
    Moves based on levels
    Level 1 or easy bot - movement is random
    Level 2 and medium or hard bot - movement in direction of the person
    '''

    def move(self, level, person_x, person_y, type_first):

        # Level 1 or first type of enemy
        if level is 1 or type_first is 1:

            move_done = 0  # for each move
            loop_count = 0  # for loop count
            # while move does not take place

            while (move_done == 0 and loop_count <= 4):
                # Random number between 1 to 40 with each division of 10
                # corresponding to a move in a direction
                z1 = uniform(1, 40)

                if z1 >= 1 and z1 <= 10:
                    temp = self.move_enemy(0, -1)

                if z1 > 10 and z1 <= 20:
                    temp = self.move_enemy(0, +1)

                if z1 > 20 and z1 <= 30:
                    temp = self.move_enemy(-1, 0)

                if z1 > 30 and z1 <= 40:
                    temp = self.move_enemy(1, 0)

                # Temp is 1 if move is made and -1 of person is found
                if temp is -1 or temp is 1:
                    move_done = 1
                    break
                else:
                    loop_count += 1
        # If level is greater than 2 or medium and hard type of bot
        elif level >= 2:
            # similar to previous loop
            move_done = 0
            loop_count = 0

            while (move_done == 0 and loop_count <= 4):

                '''This array contains the pair of distance and index
                0 for left
                1 for right
                2 for up
                3 for down'''

                map_dist = []
                map_dist.append(
                    (self.dist(
                        self.x,
                        self.y - 1,
                        person_x,
                        person_y),
                        0))
                map_dist.append(
                    (self.dist(
                        self.x,
                        self.y + 1,
                        person_x,
                        person_y),
                        1))
                map_dist.append(
                    (self.dist(
                        self.x - 1,
                        self.y,
                        person_x,
                        person_y),
                        2))
                map_dist.append(
                    (self.dist(
                        self.x + 1,
                        self.y,
                        person_x,
                        person_y),
                        3))

                # array is sorted to find the least distance
                map_dist.sort()

                for i, j in map_dist:
                    if j is 0:
                        temp = self.move_enemy(0, -1)

                    if j is 1:
                        temp = self.move_enemy(0, +1)

                    if j is 2:
                        temp = self.move_enemy(-1, 0)

                    if j is 3:
                        temp = self.move_enemy(+1, 0)

                    if temp is -1 or temp is 1:
                        move_done = 1
                        break
                    else:
                        loop_count += 1

        # if temp is -1 then the function is returns -1
        return temp


# Global enemy array. This is accessed from other files as well
enemy_array = []

# Initilaisation function
# arguments level as no. of enemies are equal to 2*level


def ini(level):
    # cnt variable contains number of enemies
    cnt_enemy = 1
    max = level * 2
    while(cnt_enemy <= max):

        # Random x and y coordinates
        x = randint(1, b.actual_x - 2)
        y = randint(1, b.actual_y - 2)

        # Checking for brick , wall and person

        if b.game[x][y] != '/' and b.game[x][y] != 'X' and b.game[x][y] != 'P':
            b.game[x][y] = 'E'
            single_enemy = Enemy(x, y)
            enemy_array.append(single_enemy)
            cnt_enemy = cnt_enemy + 1
