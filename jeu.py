import random
from classes import Labyrinth
from classes import Hero
from classes import Object


labyrinth = Labyrinth() #initialiser le plateau de jeu.
labyrinth.create() #fonction pour créer la structure du labyrinth (murs, objets, etc.)
macGyver = Hero()



objects=[]#cases "objets" créées de manière aléatoire à partir de la liste 'road' (NB : ces cases sont à la fois dans les listes 'objects' et 'road')
objects.append(Object("tube", 0))
objects.append(Object("aiguille", 0))
objects.append(Object("ether", 0))
labyrinth.make_objects()

print(objects[0].name + str(objects[0].position))
print(objects[1].name + str(objects[1].position))
print(objects[2].name + str(objects[2].position))
