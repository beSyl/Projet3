"""Class 'Hero' - 'Help MacGyver to escape !' game
Useful for character management.
Methods : init, move, check_coord, check_square, pick_up, check_victory.
"""
from constants import *


class Hero:
    """Class hero method - Create a character.
    """

    def __init__(self, game):
        # Hero's position, expressed in squares then in pixels.
        self.square_x = 0
        self.square_y = 0
        self.x = 0
        self.y = 0
        # Labyrinth in which the character evolves.
        self.game = game
        # Cart in which to store the collected items.
        self.cart = 0

    def move(self, direction, pygame_instance):
        """Class Hero method.
        Move the character : up, down, left and rigth.
        """
        if direction == 'right' and self.check_square(self.square_x + 1, self.square_y):
            self.square_x += 1
        elif direction == 'left' and self.check_square(self.square_x - 1, self.square_y):
            self.square_x -= 1
        elif direction == 'up' and self.check_square(self.square_x, self.square_y - 1):
            self.square_y -= 1
        elif direction == 'down' and self.check_square(self.square_x, self.square_y + 1):
            self.square_y += 1

        self.x = pygame_instance.calculate_in_pixels(self.square_x)
        self.y = pygame_instance.calculate_in_pixels(self.square_y)

    def check_coord(self, x, y):
        """Class Hero method.
        Check if the movement stays in the limits of the labyrinth.
        """
        return 0 <= x < (squares_per_side) and 0 <= y < (squares_per_side)

    def check_square(self, x, y):
        """Class Hero method.
        Check if the movement stays in the limits of the labyrinth with 'check_coord()', then if it goes to a wall.
        """
        return self.check_coord(x, y) and self.game.structure[y][x] != 'X'

    def pick_up(self, laby):
        """Class Hero method.
        Add 1 to the heros's cart and delete the picture of an object if the hero picks it up.
        """
        if laby.structure[self.square_y][self.square_x] in ['E', 'N', 'T']:
            self.cart += 1
            laby.structure[self.square_y][self.square_x] = ' '
            # [TEST] Display how many objects are in the hero's cart and the refreshed structure.
            print("Objet(s) dans le panier : " + str(self.cart))
            print(str(laby.structure))

    def check_victory(self):
        """Class Hero method.
        Check if all the conditions are met to win when the character ends the game.
        If the hero picks up trhee items, victory is 'True'. Otherwise, he loses and victory is 'False'.
        """
        if self.cart == 3:
            self.victory = True
        else:
            self.victory = False
