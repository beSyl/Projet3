# noinspection SpellCheckingInspection
"""Class 'My_pygame' - 'Help MacGyver to escape !' game
Useful for Pygame management (display).
Methods : init, display_background, load_pictures, display_elements, manage_keyboard, calculate_in_pixels,
refresh, show_destiny.
"""
import pygame
from pygame.locals import *
from constants import *


class MyPygame:
    def __init__(self):
        pygame.init()
        # Boolean useful to the second loop of the game.
        self.game = True  # useful for second loop
        # Open Pygame window(it's a square, so the width is equal to the height).
        self.window = pygame.display.set_mode((window_size, window_size))
        # Continue the movement if the direction key is held down for 50 ms (1st argument),
        # then repeated every 80 ms (2nd argument).
        pygame.key.set_repeat(50, 80)
        self.load_pictures()
        self.display_background()

    def display_background(self):
        # Load and display the background picture
        self.window.blit(self.background, (0, 0))
        # Speed limitation of the loop
        pygame.time.Clock().tick(20)

    def load_pictures(self):
        self.background = pygame.image.load(picture_background).convert()
        self.hero = pygame.image.load(picture_hero).convert_alpha()
        self.guardian = pygame.image.load(picture_guardian).convert_alpha()
        self.wall = pygame.image.load(picture_wall).convert()
        self.ether = pygame.image.load(picture_ether).convert_alpha()
        self.needle = pygame.image.load(picture_needle).convert_alpha()
        self.tube = pygame.image.load(picture_tube).convert_alpha()

    def display_elements(self, laby, hero):
        """Class My_pygame method.
        Display the labyrinth's elements according to the structure list
        according to the characters symbolizing special elements in labyrinth.txt
        ('E' for ether, 'X' for wall, ...)
        """
        num_line = 0
        for line in laby.structure:
            num_square = 0
            for sprite in line:
                x = self.calculate_in_pixels(num_square)
                y = self.calculate_in_pixels(num_line)
                if sprite == 'X':  # X = wall
                    self.window.blit(self.wall, (x, y))
                elif sprite == 'E':  # E = ether
                    self.window.blit(self.ether, (x, y))
                elif sprite == 'N':  # N = needle
                    self.window.blit(self.needle, (x, y))
                elif sprite == 'T':  # T = tube
                    self.window.blit(self.tube, (x, y))
                elif sprite == 'e':  # e = end
                    self.window.blit(self.guardian, (x, y))
                num_square += 1
            num_line += 1
        self.manage_keyboard(hero)

    def manage_keyboard(self, hero):
        """Class My_pygame method.
        Useful method for handling keyboard events.
        """
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # Keyboard keys useful for the movements
                if event.key == K_RIGHT:
                    hero.move('right', self)
                elif event.key == K_LEFT:
                    hero.move('left', self)
                elif event.key == K_UP:
                    hero.move('up', self)
                elif event.key == K_DOWN:
                    hero.move('down', self)

    def calculate_in_pixels(self, x):
        """Class My_pygame method.
        Calculate the display from the position of a square.
        """
        return x * sprite_size

    def refresh(self, laby, hero):
        """Class My_pygame method.
        Display the elements after a movement.
        """
        self.window.blit(self.background, (0, 0))
        self.display_elements(laby, hero)
        self.window.blit(self.hero, (hero.x, hero.y))  # mac_gyver avatar.
        pygame.display.flip()

    def show_destiny(self, hero):
        """Class My_pygame method.
        Display the final picture according to the state of the victory.
        """
        if hero.victory:
            picture = pygame.image.load(picture_victory).convert()
        else:
            picture = pygame.image.load(picture_defeat).convert()
        self.window.blit(picture, (0, 0))
        pygame.display.flip()
        pygame.time.Clock().tick(0.4)
