"""'Aidez MacGyver à s'échapper !'
OpenClassrooms parcours DA Python - Projet 3
https://openclassrooms.com/projects/aidez-macgyver-a-sechapper
"""

import pygame
from pygame.locals import *

from Labyrinth import *
from Hero import *
from constantes import *

pygame.init()

#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
window = pygame.display.set_mode((window_size, window_size))

#Poursuite du mouvement si la touche de direction est maintenue enfoncée 50 ms (1er argument), puis répété tous les 80 ms (2e argument).
pygame.key.set_repeat(50, 80)

#BOUCLE PRINCIPALE
play = 1

while play == 1:	

	#Génération d'un labyrinth à partir d'un fichier
	labyrinth = Labyrinth()
	labyrinth.create()
	labyrinth.place_objects()
	labyrinth.show(window)

	#Création de MacGyver
	macGyver = Hero("images/macGyver.png", labyrinth)
	game = 1
				
	#BOUCLE DE JEU
	while game:
		#Chargement et affichage de l'écran d'accueil
		background = pygame.image.load(picture_background).convert()
		window.blit(background, (0,0))

		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(20)
	
                #Déplacement clavier.
		macGyver.run_pygame()			
			
		#Affichages aux nouvelles positions
		window.blit(background, (0,0))
		labyrinth.show(window)
		window.blit(macGyver.direction, (macGyver.x, macGyver.y)) #macGyver.direction = l'image dans la bonne direction
		pygame.display.flip()

		#Ramasser un objet
		if labyrinth.structure[macGyver.case_y][macGyver.case_x] == 'E' or labyrinth.structure[macGyver.case_y][macGyver.case_x] == 'N' or labyrinth.structure[macGyver.case_y][macGyver.case_x] == 'T':
			macGyver.panier += 1
			labyrinth.structure[macGyver.case_y][macGyver.case_x] = ' '
			if __name__ == "__main__":
				print("Objet(s) dans le panier : " + str(macGyver.panier))
				print(str(labyrinth.structure))

		#Victoire
		if labyrinth.structure[macGyver.case_y][macGyver.case_x] == 'e':
			macGyver.check_victory()
			if macGyver.victory == True:
				picture = pygame.image.load(picture_victory).convert()            
			elif macGyver.victory == False:
				picture = pygame.image.load(picture_defeat).convert()

			window.blit(picture, (0,0))
			pygame.display.flip()
			play = 0
			game = 0
