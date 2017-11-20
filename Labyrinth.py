"""Classe 'Labyrinth' du jeu 'Aidez MacGyver à s'échapper !'
Utile à la structure du labyrinthe.
Méthodes : init, create, place_objects, show."""

import random
import pygame
from pygame.locals import * 
from constantes import *

class Labyrinth:
    """Classe permettant de créer un labyrinthe de jeu."""
    def __init__(self):
        self.fichier = 'labyrinth.txt'
        self.structure = 0
    
    
    def create(self):
        """Méthode de classe Labyrinth.
        Générer le labyrinthe à partir du fichier txt.
        On crée une liste, contenant une liste par ligne à afficher.""" 
        #On ouvre le fichier
        with open(self.fichier, "r") as file:
            list_structure = []
            #On parcourt les lignes du fichier
            for line in file:
                line_niveau = []
                #On parcourt les sprites (lettres) contenus dans le fichier
                for sprite in line:
                    #On ignore les "\n" de fin de ligne
                    if sprite != '\n':
                        #On ajoute le sprite à la liste de la ligne
                        line_niveau.append(sprite)
                #On ajoute la ligne à la liste du niveau
                list_structure.append(line_niveau)
            #On sauvegarde cette structure
            self.structure = list_structure


    def place_objects(self):
        """Méthode de classe Labyrinth.
        Placer les objets dans le labyrinthe, en modifiant la liste de structure du labyrinthe ('self.structure').""" 
        #On ouvre le fichier
        i = 0
        while i < 3:
                number1 = random.randint(0,14)
                number2 = random.randint(0,14)
                if self.structure[number1][number2] == " ":
                        if i == 0:
                                self.structure[number1][number2] = "E" #ether
                        if i == 1:
                                self.structure[number1][number2] = "N" #needle
                        if i == 2:
                                self.structure[number1][number2] = "T" #tube
                        i+=1

        print(str(self.structure))

                
    def show(self, window):
        """Méthode de classe Labyrinth.
        Afficher le plateau de jeu en fonction de la liste de structure du labyrinthe ('self.structure')."""
        #Chargement des images
        guardian = pygame.image.load(picture_guardian).convert_alpha()
        wall = pygame.image.load(picture_wall).convert()
        ether = pygame.image.load(picture_ether).convert_alpha()
        needle = pygame.image.load(picture_needle).convert_alpha()
        tube = pygame.image.load(picture_tube).convert_alpha()

        #Déterminer la position dans la fenêtre Pygame selon la position abscisse/ordonnée.
        #Utiliser la dimension d'un sprite (case dans Pygame).
        num_line = 0
        for line in self.structure:
            #On parcourt les listes de lignes
            num_square = 0
            for sprite in line:
                #On calcule la position réelle en pixels
                x = num_square * sprite_dimension
                y = num_line * sprite_dimension
                if sprite == 'X':          #m = Mur
                    window.blit(wall, (x,y))
                elif sprite == 'E':        #E = Ether
                    window.blit(ether, (x,y))
                elif sprite == 'N':        #N = Needle
                    window.blit(needle, (x,y))
                elif sprite == 'T':        #T = Tube
                    window.blit(tube, (x,y))
                elif sprite == 'e':        #a = End
                    window.blit(guardian, (x,y))
                elif sprite == 'L':        #L = Lose
                    window.blit(lose, (x,y))
                num_square += 1
            num_line += 1
