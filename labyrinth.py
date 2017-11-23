"""Class 'Labyrinth' - 'Help MacGyver to escape ! game'
Useful for making the structure of the labyrinth.
Methods : init, create, place_objects, show."""

import random
import pygame
from pygame.locals import *
from constants import *


class Labyrinth:
    """Create a labyrinth."""

    def __init__(self):
        self.fichier = 'labyrinth.txt'
        self.structure = []

    def create(self):
        """Class Labyrinth method.
        Make a labyrinth from a file '.txt'.
        Make a list, containing a list for each line to display."""
        # Open file
        with open(self.fichier, "r") as file:
            # Go through the lines of the file
            for line in file:
                list_line = []
                # Go through characters in the file, meaning the squares
                for sprite in line:
                    # Ignore line breaks
                    if sprite != '\n':
                        # Add each character to the line list
                        list_line.append(sprite)
                # Add the line to the general list
                self.structure.append(list_line)

    def place_objects(self):
        """Class Labyrinth method.
        Place the objects in the labyrinth, changing the structure list ('self.structure')."""
        # On ouvre le fichier
        i = 0
        while i < 3:
            number1 = random.randint(0, 14)
            number2 = random.randint(0, 14)
            if self.structure[number1][number2] == " ":
                if i == 0:
                    self.structure[number1][number2] = "E"  # ether
                if i == 1:
                    self.structure[number1][number2] = "N"  # needle
                if i == 2:
                    self.structure[number1][number2] = "T"  # tube
                i += 1
        # [DELETE AT THE END OF THE DEVELOPMENT] Display and check the structure
        print(str(self.structure))

    def show(self, window):
        """Classe Labyrinth method.
        Display the game according to the structure list ('self.structure')."""
        # Loading pictures
        guardian = pygame.image.load(picture_guardian).convert_alpha()
        wall = pygame.image.load(picture_wall).convert()
        ether = pygame.image.load(picture_ether).convert_alpha()
        needle = pygame.image.load(picture_needle).convert_alpha()
        tube = pygame.image.load(picture_tube).convert_alpha()

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
                    window.blit(wall, (x, y))
                elif sprite == 'E':  # E = ether
                    window.blit(ether, (x, y))
                elif sprite == 'N':  # N = needle
                    window.blit(needle, (x, y))
                elif sprite == 'T':  # T = tube
                    window.blit(tube, (x, y))
                elif sprite == 'e':  # e = end
                    window.blit(guardian, (x, y))
                num_square += 1
            num_line += 1
