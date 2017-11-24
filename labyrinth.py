"""Class 'Labyrinth' - 'Help MacGyver to escape ! game'
Useful for making the structure of the labyrinth.
Methods : init, create, place_objects, show, finish."""
import random
from my_pygame import *


class Labyrinth:
    """Create a labyrinth."""

    def __init__(self, file='labyrinth.txt'):
        self.file = file
        self.structure = []
        self.create()
        self.place_objects()

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

    def finish(self, hero, pygame_instance):
        if self.structure[hero.case_y][hero.case_x] == 'e':
            hero.check_victory()
            pygame_instance.show_destiny(hero)
