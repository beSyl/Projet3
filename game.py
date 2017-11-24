"""'Help MacGyver to escape! '
OpenClassrooms course DA Python - Project 3
https://openclassrooms.com/projects/aidez-macgyver-a-sechapper
"""
from labyrinth import *
from hero import *
from my_pygame import *


def main():
    """Main function that load and display all the objects of the Pygame window.
    Then, it loads the labyrinth structure and the hero in a main game loop,
    and finally the hero's actions (move, pick-up an object, ...) are managed in the second loop
    that ends when the hero comes to the end.
    Depending on the number of items picked up by the hero, either he wins or loses.
    """
    my_pygame = My_pygame()
    play = True
    # MAIN LOOP
    while play:
        # Make a labyrinth from a file
        labyrinth = Labyrinth()
        my_pygame.display_elements(labyrinth)
        # Create character
        mac_gyver = Hero(labyrinth)
        game = True

        # GAME LOOP
        while game:
            mac_gyver.activate(my_pygame)
            my_pygame.refresh(labyrinth, mac_gyver)
            mac_gyver.pick_up(labyrinth)
            if labyrinth.structure[mac_gyver.case_y][mac_gyver.case_x] == 'e':
                labyrinth.finish(mac_gyver, my_pygame)
                play = False
                game = False


if __name__ == "__main__":
    main()
