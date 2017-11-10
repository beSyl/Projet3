import random

#VARIABLES-----
walls=[]#uniquement les cases "murs"
road=[]#uniquement les cases "chemin"
list_labyrinth=[]#toutes les cases, numérotées de 0 à numberOfSquares-1.
objects=[]#cases "objets" créées de manière aléatoire à partir de la liste 'road' (NB : ces cases sont à la fois dans les listes 'objects' et 'road')

#CLASSES-----
#STRUCTURE DU LABYRINTHE.
class Labyrinth:
    HEIGHT=15 #hauteur en cases.
    WIDTH=15 #largeur en cases.
    numberOfSquares = HEIGHT*WIDTH #nombre de cases du labyrinthe.

    def __init__(self):#Transformer le fichier labyrinthe en liste (i.e. une liste des cases du plateau de jeu).
        with open('labyrinth.txt', 'r') as f:
            file = f.read()
        for element in file: #tant qu'il y a un élément dans le fichier
            if element!="\n": #sauf s'il s'agit d'un saut de ligne
                list_labyrinth.append(element)
        i=0
        while i<Labyrinth.numberOfSquares:
            if list_labyrinth[i] != "\n":
                if list_labyrinth[i]=="X":
                    walls.append(i)
                elif list_labyrinth[i]==" ":
                    road.append(i)
            i+=1


#OBJETS A RAMASSER.
#class Object:
#    objects_counter = 0 #compteur d'instances de la classe.
#    def __init__(self, position):
#        self.position = position #numéro de case par défaut
#        Object.objects_counter += 1 #incrément le compteur d'instance de classe Object.




#PERSONNAGE DU JEU.
class Hero:
    def __init__(self):
        self.position = 0 #emplacement dans le labyrinthe exprimé en numéro de case, case 0 au début du jeu.
        self.objectsCounter = 0 #objets ramassée, aucun par défaut au début du jeu.
        self.picture = "images/hero.jpg" #ACTUALISER / CORRIGER

    def move(self, direction):
        movement=0
        
        if direction == "right":
            movement = 1
        elif direction == "left":
            movement = -1
        elif direction == "up":
            movement = -Labyrinth.WIDTH
        elif direction == "down":
            movement = Labyrinth.WIDTH

        if self.position in objects:
            print("Un objet trouvé en case " + str(self.position) + " !")
            self.objectsCounter+=1
            a=self.position
            objects.remove(a)
                
        if self.position+movement in road:
            self.position+=movement

        if self.position == road[-1]:
            if self.objectsCounter == 3:
                print("MacGyver a trouvé tous les objets : il a gagné.")
            else:
                print("MacGyver n'a trouvé que " + str(self.objectsCounter) + " objet(s) : il a perdu.")
        else: 
            movement=0
        
        print(self.position)


#JEU-----
labyrinth = Labyrinth() #initialiser le plateau de jeu.
macGyver = Hero()

i=0
while i<3: #on crée autant de chiffres qu'il existe d'objets.
    number=random.randint(1, road[-1]) #on exclut la première et la dernière case, soit le départ et l'arrivée du jeu, pour positionner les objets à ramasser.
    if number in road and number not in objects:
        objects.append(number)
        i+=1

tube = objects[0]
needle = objects[1]
ether = objects[2]


#VERIFICATION-----
print("Cases 'chemin' : " + str(road))     
print("Cases 'mur' : " + str(walls))
print("Case 'fin' : " + str(road[-1]))
print("Objets " + str(len(objects)))
print("Le tube est placé en case " + str(tube))
print("L'aiguille est placée en case " + str(needle))
print("L'ether est placée en case " + str(ether))

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
print("A la fin du jeu, la liste 'objects' contient " + str(len(objects)) + " objets.")
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
