"""Classe 'Hero' du jeu 'Aidez MacGyver à s'échapper !'
Utile à la gestion du personnage.
Méthodes : init, move, run_pygame, check_victory.
"""

import random
import pygame
from pygame.locals import * 
from constantes import *

class Hero:
    """Méthode permettant de créer un personnage"""
    def __init__(self, picture, game):
        #Avatar du personnage
        self.picture = pygame.image.load(picture).convert_alpha()
        #Position du personnage en cases et en pixels
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        #Plateau de jeu dans lequel le personnage évolue. 
        self.game = game
        #Panier dans lequel stocker les objets ramassés.
        self.cart = 0
    
    
    def move(self, direction):
        """Méthode de classe Hero.
        Déplacer le personnage : haut, bas, droite et gauche."""
        #Déplacement vers la droite
        if direction == 'right':
            #Pour ne pas dépasser l'écran
            if self.case_x < (squares_per_side - 1):
                #On vérifie que la case de destination n'est pas un mur
                if self.game.structure[self.case_y][self.case_x+1] != 'X':
                    #Déplacement d'une case en abscisse
                    self.case_x += 1
                    #Calcul de la position à afficher dans la fenêtre Pygame, en pixel
                    self.x = self.case_x * sprite_dimension
        
        #Déplacement vers la gauche
        if direction == 'left':
            if self.case_x > 0:
                if self.game.structure[self.case_y][self.case_x-1] != 'X':
                    self.case_x -= 1
                    self.x = self.case_x * sprite_dimension
        
        #Déplacement vers le haut
        if direction == 'up':
            if self.case_y > 0:
                if self.game.structure[self.case_y-1][self.case_x] != 'X':
                    self.case_y -= 1
                    self.y = self.case_y * sprite_dimension
        
        #Déplacement vers le bas
        if direction == 'down':
            if self.case_y < (squares_per_side - 1):
                if self.game.structure[self.case_y+1][self.case_x] != 'X':
                    self.case_y += 1
                    self.y = self.case_y * sprite_dimension

    def run_pygame(self):
        """Méthode de classe Hero.
        Gérer les déplacements au clavier : haut, bas, droite et gauche."""
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                #Si l'utilisateur presse Echap ici, on revient seulement au menu
                if event.key == K_ESCAPE:
                    continuer_jeu = 0
                    
            #Touches de déplacement de MacGyver
                elif event.key == K_RIGHT:
                    self.move('right')
                elif event.key == K_LEFT:
                    self.move('left')
                elif event.key == K_UP:
                    self.move('up')
                elif event.key == K_DOWN:
                    self.move('down')

    def check_victory(self):
        """Méthode de classe Hero.
        Vérifier les conditions de victoire lorsque le personnage arrive en fin de jeu."""
        if self.cart == 3:
            self.victory = True
        else:
            self.victory = False
