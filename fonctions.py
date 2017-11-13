import random
from constantes import *

#FUNCTIONS
def make_walls():
    i=0
    while i<3: #Créer autant de chiffres qu'il existe d'objets.
        number=random.randint(1, road[-1]) #Exclure la première et la dernière case, soit le départ et l'arrivée du jeu, pour positionner les objets à ramasser.
        if number in road and number not in objects: #S'assurer que la position correspond à une case 'chemin' et qu'elle ne soit pas déjà associée à un objet créé précédemment dans 'objects'.
            objects.append(number)
            i+=1
