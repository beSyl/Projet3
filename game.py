"""'Help MacGyver to escape! '
OpenClassrooms course DA Python - Project 3
https://openclassrooms.com/projects/aidez-macgyver-a-sechapper
"""
from labyrinth import *
from hero import *
from my_pygame import *


def main():
    my_pygame = My_pygame()

    # PRINCIPAL LOOP
    play = True

    while play:

        # Make a labyrinth from a file
        labyrinth = Labyrinth(my_pygame)
        # Create character
        mac_gyver = Hero(labyrinth)
        game = True

        # GAME LOOP
        while game:
            mac_gyver.activate(my_pygame)
            my_pygame.refresh(labyrinth, mac_gyver)
            mac_gyver.pick_up(labyrinth)

            # End of game
            if labyrinth.structure[mac_gyver.case_y][mac_gyver.case_x] == 'e':
                mac_gyver.check_victory()
                my_pygame.show_destiny(mac_gyver)
                play = False
                game = False

if __name__ == "__main__":
    main()
