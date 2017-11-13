from classes import *
from fonctions import *


#GAME-----
labyrinth = Labyrinth() #Initialiser le plateau de jeu.
macGyver = Hero() #Initialiser le héros.
make_walls()

#Déterminer les objets à partir des positions créées de manière aléatoire dans 'objects'.
tube = objects[0]
needle = objects[1]
ether = objects[2]


#VERIFICATION-----
print("Cases 'chemin' : " + str(road))     
print("Cases 'mur' : " + str(walls))
print("Case 'fin' : " + str(road[-1]))
print("Objets ajoutés à la liste 'objects' : " + str(len(objects)))
print("Le tube est placé en case " + str(tube))
print("L'aiguille est placée en case " + str(needle))
print("L'ether est placée en case " + str(ether) + "\n")

macGyver.move("left")
macGyver.move("right")
macGyver.move("right")
macGyver.move("right")
macGyver.move("up")
macGyver.move("down")
macGyver.move("down")
macGyver.move("right")
macGyver.move("down")
macGyver.move("down")
macGyver.move("right")
macGyver.move("right")
macGyver.move("right")
macGyver.move("right")
macGyver.move("right")
macGyver.move("down")
macGyver.move("down")
macGyver.move("right")
macGyver.move("right")
macGyver.move("down")
macGyver.move("down")
macGyver.move("down")
macGyver.move("down")
macGyver.move("left")
macGyver.move("down")
macGyver.move("down")
macGyver.move("right")
macGyver.move("right")
macGyver.move("right")
macGyver.move("down")
macGyver.move("down")
macGyver.move("right")
macGyver.move("right")
macGyver.move("right")
print("\nA la fin du jeu, la liste 'objects' contient " + str(len(objects)) + " objets.")
if tube in objects:
    print("Le tube n'a pas été ramassé.")
else:
    print("Le tube a été ramassé : bravo !")
if needle in objects:
    print("L'aiguille n'a pas été ramassée.")
else:
    print("L'aiguille a été ramassée : bravo !")
if ether in objects:
    print("L'ether n'a pas été ramassée.")
else:
    print("L'ether a été ramassé : bravo !")
