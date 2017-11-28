"""'Help MacGyver to escape! '
OpenClassrooms course DA Python - Project 3
https://openclassrooms.com/projects/aidez-macgyver-a-sechapper
"""
from labyrinth import *
from hero import *
from my_pygame import *


def main():
    """Main function that load and display all the objects of the Pygame window.
    'Play' is True when the player wants to.
    Then, it loads the labyrinth structure and the hero in a main game loop,
    so 'game' is True to symbolize the beginning of the game.
    Finally, as long as 'game' is True, the hero's actions (move, pick-up an object, ...) are managed
    in the second loop that ends when the hero comes to the end.
    Depending on the number of items picked up by the hero, either he wins or loses.
    There, 'game' becomes False and 'play' depends of the player's choice.
    """
    my_pygame = MyPygame()

    # MAIN LOOP
    while my_pygame.play:
        # Make a labyrinth from a file
        labyrinth = Labyrinth()
        # Create character
        mac_gyver = Hero(labyrinth)

        # GAME LOOP
        while my_pygame.game:
            # Manage displaying, updating after a movement and keyboard commands with Pygame
            my_pygame.refresh(labyrinth, mac_gyver)
            mac_gyver.pick_up(labyrinth)
            if labyrinth.structure[mac_gyver.square_y][mac_gyver.square_x] == 'e':
                mac_gyver.check_victory()
                my_pygame.show_destiny(mac_gyver)
                my_pygame.game = False

        my_pygame.play = False


if __name__ == "__main__":
    main()
