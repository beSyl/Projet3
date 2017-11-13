from constantes import *

#CLASSES-----
#STRUCTURE.
class Labyrinth:
    HEIGHT=15 #Hauteur en nombre de cases.
    WIDTH=15 #Largeur en nombre de cases.
    ALL_SQUARES = HEIGHT*WIDTH #Nombre de cases composant du labyrinthe.

    def __init__(self):#Transformer le fichier labyrinthe en liste (i.e. une liste des cases du plateau de jeu).
        with open('labyrinth.txt', 'r') as f:
            file = f.read()
        for element in file: #Tant qu'il y a un élément dans le fichier
            if element!="\n": #Sauf s'il s'agit d'un saut de ligne
                list_labyrinth.append(element)
        i=0
        while i<Labyrinth.ALL_SQUARES:
            if list_labyrinth[i] != "\n":
                if list_labyrinth[i]=="X":
                    walls.append(i)
                elif list_labyrinth[i]==" ":
                    road.append(i)
            i+=1


#OBJECTS TO PICK UP.
#class Object:
#    objects_counter = 0 #compteur d'instances de la classe.
#    def __init__(self, position):
#        self.position = position #numéro de case par défaut
#        Object.objects_counter += 1 #incrément le compteur d'instance de classe Object.




#CHARACTERS.
class Hero:
    def __init__(self):
        self.position = 0 #emplacement dans le labyrinthe exprimé en numéro de case, soit la case 0 au début du jeu.
        self.objectsCounter = 0 #objets ramassés, soit aucun par défaut au début du jeu.
        self.picture = "images/hero.jpg" #ACTUALISER / CORRIGER
        self.line = 0 #position affichée à l'écran, exprimée en ligne
        self.column = 0 #position affichée à l'écran, exprimée en colonne

    def move(self, direction):
        movement=0
        #Déterminer l'ampleur du mouvement selon la direction.
        #Un déplacement horizontal vaut 1 case, un déplacement horizontal vaut le nombre de cases par ligne (i.e. "haut" ou "bas" correspond à changer la position d'une ligne).
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
                print("MacGyver a trouvé tous les objets : il a GAGNÉ !")
            else:
                print("MacGyver n'a trouvé que " + str(self.objectsCounter) + " objet(s) : il a PERDU...")
        else: 
            movement=0

        self.line = self.position//Labyrinth.WIDTH

        self.column = self.position-(self.line*Labyrinth.WIDTH)
        print("MacGyver en case n° " + str(self.position) + ". En ligne " + str(self.line) + ", colonne " + str(self.column))

