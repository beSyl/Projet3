"""Class 'My_pygame' - 'Help MacGyver to escape !' game
Useful for Pygame management (display).
Methods : init, move, run_pygame, check_victory.
"""
from constants import *
import pygame


class My_pygame:
    def __init__(self):
        pygame.init()
        # Open Pygame window(square, so width = height)
        self.window = pygame.display.set_mode((window_size, window_size))
        # Continue the movement if the direction key is held down for 50 ms (1st argument), then repeated every 80 ms (2nd argument).
        pygame.key.set_repeat(50, 80)
        self.load_background()
        self.load_pictures()

    def load_background(self):
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

    def refresh(self, laby, hero):
        self.window.blit(self.background, (0, 0))
        laby.show(self)
        self.window.blit(self.hero, (hero.x, hero.y))  # mac_gyver avatar.
        pygame.display.flip()

    def show_destiny(self, hero):
        if hero.victory == True:
            picture = pygame.image.load(picture_victory).convert()
        else:
            picture = pygame.image.load(picture_defeat).convert()

        self.window.blit(picture, (0, 0))
        pygame.display.flip()
