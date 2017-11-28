"""'Help MacGyver to escape! '
OpenClassrooms course DA Python - Project 3
https://openclassrooms.com/projects/aidez-macgyver-a-sechapper
"""
from labyrinth import *
from hero import *
from my_pygame import *


def main():
    """Main function that load and display all the objects of the Pygame window.
    It makes instances for the Pygame elements, the labyrinth, the hero.
    So 'my_pygame.game' is True to symbolize the beginning of the game.
    Finally, as long as 'my_pygame.game' is True, the hero's actions (move, pick-up an object, ...) are managed
    in the game loop that ends when the hero comes to the last square.
    Depending on the number of items picked up by the hero, either he wins or loses.
    There, 'my_pygame.game' becomes False to end the game.
    """
    # Instance of Pygame elements
    my_pygame = MyPygame()
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


if __name__ == "__main__":
    main()
