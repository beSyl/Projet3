"""'Help MacGyver to escape! '
OpenClassrooms course DA Python - Project 3
https://openclassrooms.com/projects/aidez-macgyver-a-sechapper
"""

import pygame
from pygame.locals import *

from labyrinth import *
from hero import *
from constants import *

pygame.init()

# Open Pygame window(square, so width = height)
window = pygame.display.set_mode((window_size, window_size))

# Continue the movement if the direction key is held down for 50 ms (1st argument), then repeated every 80 ms (2nd argument).
pygame.key.set_repeat(50, 80)

# PRINCIPAL LOOP
play = 1

while play == 1:

    # Make a labyrinth from a file
    labyrinth = Labyrinth()
    labyrinth.create()
    labyrinth.place_objects()
    labyrinth.show(window)

    # Create character
    macGyver = Hero("images/macGyver.png", labyrinth)
    game = 1

    # GAME LOOP
    while game:
        # Load and display the background picture
        background = pygame.image.load(picture_background).convert()
        window.blit(background, (0, 0))

        # Speed limitation of the loop
        pygame.time.Clock().tick(20)

        # Keyboard movement
        macGyver.run_pygame()

        # Display the new position
        window.blit(background, (0, 0))
        labyrinth.show(window)
        window.blit(macGyver.picture, (macGyver.x, macGyver.y))  # MacGyver avatar.
        pygame.display.flip()

        # Pick up an object
        if labyrinth.structure[macGyver.case_y][macGyver.case_x] == 'E' or labyrinth.structure[macGyver.case_y][
            macGyver.case_x] == 'N' or labyrinth.structure[macGyver.case_y][macGyver.case_x] == 'T':
            macGyver.cart += 1
            labyrinth.structure[macGyver.case_y][macGyver.case_x] = ' '
            if __name__ == "__main__":
                print("Objet(s) dans le panier : " + str(macGyver.cart))
                print(str(labyrinth.structure))

        # End of game
        if labyrinth.structure[macGyver.case_y][macGyver.case_x] == 'e':
            macGyver.check_victory()
            if macGyver.victory == True:
                picture = pygame.image.load(picture_victory).convert()
            else:
                picture = pygame.image.load(picture_defeat).convert()

            window.blit(picture, (0, 0))
            pygame.display.flip()
            play = 0
            game = 0
