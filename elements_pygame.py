#ELEMENTS POUR PYGAME-----
"""
Ebauche.
A intégrer dans le jeu par la suite.
"""

import pygame
from pygame.locals import *

pygame.init()

#Fenêtre Pygame, 600 x 600 pixels.
window = pygame.display.set_mode((600, 600))

#Chargement des images, puis collage sur la fenêtr Pygame.
#Image de fond, en haut à gauche.
background_p = pygame.image.load(background_picture).convert()
window.blit(background_p, (0, 0))

#Image du héros, au début en haut à gauche, méthode 'convert_alpha()' pour gérer la transparence.
hero_p = pygame.image.load(hero_picture).convert_alpha()
hero_position = hero_p.get_rect() #position en haut à gauche par défaut, évolutive selon les événements au clavier.
window.blit(hero_p, hero_position)

#Image du gardien, en bas à droite, méthode 'convert_alpha()' pour gérer la transparence.
guardian_p = pygame.image.load(guardian_picture).convert_alpha()
window.blit(guardian_p, (560, 560))

#Image de l'objet 'ether', aléatoire, méthode 'convert_alpha()' pour gérer la transparence.
ether_p = pygame.image.load(ether_picture).convert_alpha()
window.blit(ether_p, (40, 40))

#Rafraîchissement de l'écran, nécessaire pour afficher les images Pygame.
pygame.display.flip()
