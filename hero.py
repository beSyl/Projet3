"""Class 'Hero' - 'Help MacGyver to escape !' game
Useful for character management.
Methods : init, move, run_pygame, check_victory.
"""

import random
import pygame
from pygame.locals import *
from constants import *


class Hero:
    """Class hero method - Create a character"""

    def __init__(self, picture, game):
        # Avatar du personnage
        self.picture = pygame.image.load(picture).convert_alpha()
        # Position du personnage en cases et en pixels
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        # Plateau de jeu dans lequel le personnage évolue.
        self.game = game
        # Panier dans lequel stocker les objets ramassés.
        self.cart = 0

    def move(self, direction):
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
                    # Calcul de la position à afficher dans la fenêtre Pygame, en pixel
                    self.x = self.case_x * sprite_dimension

        # Go to the left
        if direction == 'left':
            if self.case_x > 0:
                if self.game.structure[self.case_y][self.case_x - 1] != 'X':
                    self.case_x -= 1
                    self.x = self.case_x * sprite_dimension

        # Go to the top
        if direction == 'up':
            if self.case_y > 0:
                if self.game.structure[self.case_y - 1][self.case_x] != 'X':
                    self.case_y -= 1
                    self.y = self.case_y * sprite_dimension

        # Go down
        if direction == 'down':
            if self.case_y < (squares_per_side - 1):
                if self.game.structure[self.case_y + 1][self.case_x] != 'X':
                    self.case_y += 1
                    self.y = self.case_y * sprite_dimension

    def run_pygame(self):
        """Class hero method.
        Manage the movements on the keyboard : up, down, right and left."""
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # Keyboard keys useful for the movements
                if event.key == K_RIGHT:
                    self.move('right')
                elif event.key == K_LEFT:
                    self.move('left')
                elif event.key == K_UP:
                    self.move('up')
                elif event.key == K_DOWN:
                    self.move('down')

    def check_victory(self):
        """Class hero method.
        Check if all the conditions are met to win when the character ends the game."""
        if self.cart == 3:
            self.victory = True
        else:
            self.victory = False
