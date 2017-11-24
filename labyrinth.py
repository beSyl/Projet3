"""Class 'Labyrinth' - 'Help MacGyver to escape ! game'
Useful for making the structure of the labyrinth.
Methods : init, create, place_objects, show."""

import random
from my_pygame import *


class Labyrinth:
    """Create a labyrinth."""

    def __init__(self, pygame_instance, file='labyrinth.txt'):
        self.file = file
        self.structure = []
        self.create()
        self.place_objects()
        self.show(pygame_instance)

    def create(self):
        """Class Labyrinth method.
        Make a labyrinth from a file '.txt'.
        Make a list, containing a list for each line to display."""
        # Open file
        with open(self.file, "r") as file:
            # Go through the lines of the file
            for line in file:
                list_line = []
                # Go through characters in the file, meaning the squares
                for sprite in line:
                    # Ignore line breaks
                    if sprite != '\n':
                        # Add each character to the line list
                        list_line.append(sprite)
                self.structure.append(list_line)

    def place_objects(self):
        """Class Labyrinth method.
        Place the objects in the labyrinth, changing the structure list ('self.structure')."""
        # Open file
        i = 0
        while i < 3:
            number1 = random.randint(0, 14)
            number2 = random.randint(0, 14)
            if self.structure[number1][number2] == " ":
                if i == 0:
                    self.structure[number1][number2] = "E"  # ether
                elif i == 1:
                    self.structure[number1][number2] = "N"  # needle
                elif i == 2:
                    self.structure[number1][number2] = "T"  # tube
                i += 1
        # [DELETE AT THE END OF THE DEVELOPMENT] Display and check the structure
        print(str(self.structure))

    def show(self, pygame_instance):
        """Classe Labyrinth method.
        Display the game according to the structure list ('self.structure')."""
        # Determine the position in the Pygame window according to abscissa/ordinate
        # Use the dimension of a sprite (Pygame square)
        num_line = 0
        for line in self.structure:
            # Go through the lines lists
            num_square = 0
            for sprite in line:
                # Determine the position to display (in pixels)
                x = num_square * sprite_dimension
                y = num_line * sprite_dimension
                if sprite == 'X':  # X = wall
                    pygame_instance.window.blit(pygame_instance.wall, (x, y))
                elif sprite == 'E':  # E = ether
                    pygame_instance.window.blit(pygame_instance.ether, (x, y))
                elif sprite == 'N':  # N = needle
                    pygame_instance.window.blit(pygame_instance.needle, (x, y))
                elif sprite == 'T':  # T = tube
                    pygame_instance.window.blit(pygame_instance.tube, (x, y))
                elif sprite == 'e':  # e = end
                    pygame_instance.window.blit(pygame_instance.guardian, (x, y))
                num_square += 1
            num_line += 1
