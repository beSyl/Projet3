"""'Help MacGyver to escape! '
OpenClassrooms course DA Python - Project 3
https://openclassrooms.com/projects/aidez-macgyver-a-sechapper
"""
from labyrinth import *
from hero import *
from my_pygame import *

my_pygame = My_pygame()

# PRINCIPAL LOOP
play = 1

while play == 1:

    # Make a labyrinth from a file
    labyrinth = Labyrinth(my_pygame)
    # Create character
    mac_gyver = Hero(labyrinth)
    game = 1

    # GAME LOOP
    while game:
        mac_gyver.activate(my_pygame)
        my_pygame.refresh(labyrinth, mac_gyver)

        # Pick up an object
        if labyrinth.structure[mac_gyver.case_y][mac_gyver.case_x] in ['E', 'N', 'T']:
            mac_gyver.cart += 1
            labyrinth.structure[mac_gyver.case_y][mac_gyver.case_x] = ' '
            if __name__ == "__main__":
                print("Objet(s) dans le panier : " + str(mac_gyver.cart))
                print(str(labyrinth.structure))

        # End of game
        if labyrinth.structure[mac_gyver.case_y][mac_gyver.case_x] == 'e':
            mac_gyver.check_victory()
            my_pygame.show_destiny(mac_gyver)
            play = 0
            game = 0
