import random

#VARIABLES-----
list_labyrinth = []#toutes les cases, numérotées de 0 à numberOfSquares-1.
walls = []#uniquement les cases "murs"
road = []#uniquement les cases "chemin"
objects = []#cases "objets" créées de manière aléatoire à partir de la liste 'road' (NB : ces cases sont à la fois dans les listes 'objects' et 'road')
end = []
items = []


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


#OBJETS A RAMASSER.
class Object:
    objects_counter = 0 #compteur d'instances de la classe.
    def __init__(self, name, position):
        self.name = name #nom de l'objet
        self.position = position #numéro de case par défaut
        Object.objects_counter += 1 #incrément le compteur d'instance de classe Object.


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
        
        #Si le déplacement envisagé conduit à une case "chemin" (ou une case "objet" figurant à la fois dans les listes 'road' et 'objects').
        #Implicitement, le déplacement est >=0 et <numberOfSquares).
        if self.position+movement in objects:
            a=self.position+movement
            items.append(a)
            objects.remove(a)
            self.position+=movement
        elif self.position+movement in road:
            #Si le déplacement conduit à une case "objet", le personnage le ramasse.
            #L'objet est supprimé de la list 'objects' MAIS sa case est toujours présente dans la liste 'road' dont elle est issue.
            self.position+=movement
        elif self.position+movement in end:
            if len(items) == 3:
                print("MacGyver a trouvé tous les objets : il a gagné.")
            else:
                print("MacGyver a trouvé " + str(len(items)) + " objets : il a perdu.")
            self.position+=movement

          #Si le déplacement conduit à une case "mur" ou sort des limites du plateau de jeu (résultat négatif ou supérieur au numéro de la case de fin), aucun mouvement.
        else: 
            movement=0
        
        print("MacGyver a bougé : il est à la case " + str(self.position))


#JEU-----
labyrinth = Labyrinth() #initialiser le plateau de jeu.
macGyver = Hero()

#while macGyver.position < Labyrinth.numberOfSquares:

    #Créer une liste d'ID des murs à partir du fichier labyrinthe (i.e. leur emplacement dans la liste des cases)
    #Créer une liste d'ID des passages à partir du fichier labyrinthe.
i=0
while i<Labyrinth.numberOfSquares:
    if list_labyrinth[i]=="X":
        walls.append(i)
    elif list_labyrinth[i]==" ":
        road.append(i)
    elif list_labyrinth[i] == "e":
        end.append(i)
    i+=1

    #Créer les objets, en position '0' par défaut.
objects.append(Object("tube", 0))
objects.append(Object("aiguille", 0))
objects.append(Object("ether", 0))

    #Créer la position de chaque objet à ramasser, à partir de la liste 'road'.
i=0
while i<Object.objects_counter: #on crée autant de chiffres qu'il existe d'instances de la classe Object.
    number=random.randint(1, Labyrinth.numberOfSquares-1) #on exclut la première et la dernière case, soit le départ et l'arrivée du jeu, pour positionner les objets à ramasser.
    if number in road:
        objects[i].position = number
        i+=1



#VERIFICATION-----
print("Cases 'chemin' : " + str(road))     
print("Cases 'mur' : " + str(walls))
print("Case 'fin' : " + str(end))
print("La liste 'objects' contient " + str(len(objects)) + " objets.")
print("Objet " + str(objects[0].name) + " en case " + str(objects[0].position))
print("Objet " + str(objects[1].name) + " en case " + str(objects[1].position))
print("Objet " + str(objects[2].name) + " en case " + str(objects[2].position))

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
print("La liste 'objects' contient " + str(len(objects)) + " objets.")
