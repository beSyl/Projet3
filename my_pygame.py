"""Class 'My_pygame' - 'Help MacGyver to escape !' game
Useful for Pygame management (display).
Methods : init, display_background, load_pictures, display_elements, calculate_in_pixels, refresh, show_destiny.
"""
import pygame
from pygame.locals import *
from constants import *


class My_pygame:
    def __init__(self):
        pygame.init()
        # Open Pygame window(square, so width = height)
        self.window = pygame.display.set_mode((window_size, window_size))
        # Continue the movement if the direction key is held down for 50 ms (1st argument), then repeated every 80 ms (2nd argument).
        pygame.key.set_repeat(50, 80)
        self.display_background()
        self.load_pictures()

    def display_background(self):
        # Load and display the background picture
        self.background = pygame.image.load(picture_background).convert()
        self.window.blit(self.background, (0, 0))
        # Speed limitation of the loop
        pygame.time.Clock().tick(20)

    def load_pictures(self):  # Load pictures
        self.hero = pygame.image.load(picture_hero).convert_alpha()
        self.guardian = pygame.image.load(picture_guardian).convert_alpha()
        self.wall = pygame.image.load(picture_wall).convert()
        self.ether = pygame.image.load(picture_ether).convert_alpha()
        self.needle = pygame.image.load(picture_needle).convert_alpha()
        self.tube = pygame.image.load(picture_tube).convert_alpha()

    def display_elements(self, laby):
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

    def calculate_in_pixels(self, x):
        return x * sprite_dimension

    def refresh(self, laby, hero):
        self.window.blit(self.background, (0, 0))
        self.display_elements(laby)
        self.window.blit(self.hero, (hero.x, hero.y))  # mac_gyver avatar.
        pygame.display.flip()

    def show_destiny(self, hero):
        if hero.victory == True:
            picture = pygame.image.load(picture_victory).convert()
        else:
            picture = pygame.image.load(picture_defeat).convert()
        self.window.blit(picture, (0, 0))
        pygame.display.flip()
