"""Class 'Hero' - 'Help MacGyver to escape !' game
Useful for character management.
Methods : init, move, run_pygame, check_victory.
"""
import pygame
from pygame.locals import *
from constants import *


class Hero:
    """Class hero method - Create a character"""

    def __init__(self, game):
        # Avatar du personnage
        # self.picture = pygame.image.load(picture).convert_alpha()
        # Position du personnage en cases et en pixels
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        # Plateau de jeu dans lequel le personnage évolue.
        self.game = game
        # Panier dans lequel stocker les objets ramassés.
        self.cart = 0

    def move(self, direction, pygame_instance):
        """Class hero method.
        Move the character : up, down, left and rigth."""
        # Go to the right.
        if direction == 'right':
            # Pour ne pas dépasser l'écran
            if self.case_x < (squares_per_side - 1):
                # On vérifie que la case de destination n'est pas un mur
                if self.game.structure[self.case_y][self.case_x + 1] != 'X':
                    # Déplacement d'une case en abscisse
                    self.case_x += 1

        # Go to the left
        elif direction == 'left':
            if self.case_x > 0:
                if self.game.structure[self.case_y][self.case_x - 1] != 'X':
                    self.case_x -= 1

        # Go to the top
        elif direction == 'up':
            if self.case_y > 0:
                if self.game.structure[self.case_y - 1][self.case_x] != 'X':
                    self.case_y -= 1

        # Go down
        elif direction == 'down':
            if self.case_y < (squares_per_side - 1):
                if self.game.structure[self.case_y + 1][self.case_x] != 'X':
                    self.case_y += 1

        self.x = pygame_instance.calculate_in_pixels(self.case_x)
        self.y = pygame_instance.calculate_in_pixels(self.case_y)

    def activate(self, pygame_instance):
        """Class hero method.
        Manage the movements on the keyboard : up, down, right and left."""
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # Keyboard keys useful for the movements
                if event.key == K_RIGHT:
                    self.move('right', pygame_instance)
                elif event.key == K_LEFT:
                    self.move('left', pygame_instance)
                elif event.key == K_UP:
                    self.move('up', pygame_instance)
                elif event.key == K_DOWN:
                    self.move('down', pygame_instance)

    def pick_up(self, laby):
        if laby.structure[self.case_y][self.case_x] in ['E', 'N', 'T']:
            self.cart += 1
            laby.structure[self.case_y][self.case_x] = ' '
            print("Objet(s) dans le panier : " + str(self.cart))
            print(str(laby.structure))

    def check_victory(self):
        """Class hero method.
        Check if all the conditions are met to win when the character ends the game.
        If the hero picks up trhee items, victory is 'True'. Otherwise, he loses and victory is 'False'."""
        if self.cart == 3:
            self.victory = True
        else:
            self.victory = False
