import random





#Structure du labyrinthe.
class Labyrinth:
    HEIGHT=15 #hauteur en cases.
    WIDTH=15 #largeur en cases.
    def __init__(self):
        self.numberOfSquares = Labyrinth.HEIGHT*Labyrinth.WIDTH #nombre de cases du labyrinthe.


    def create(self):#Transformer le fichier labyrinthe en liste (i.e. une liste des cases du plateau de jeu).
        list_labyrinth = []#toutes les cases, numérotées de 0 à numberOfSquares-1.
        walls=[]#uniquement les cases "murs"
        road=[]#uniquement les cases "chemin"

        with open('laby_test1.txt', 'r') as f:
            file = f.read()
        for element in file: #tant qu'il y a un élément dans le fichier
            if element!="\n": #sauf s'il s'agit d'un saut de ligne
                list_labyrinth.append(element)

#Créer une liste d'ID des murs à partir du fichier labyrinthe (i.e. leur emplacement dans la liste des cases)
#Créer une liste d'ID des passages à partir du fichier labyrinthe.
        i=0
        while i<self.numberOfSquares:
            if list_labyrinth[i]=="X":
                walls.append(i)
            elif list_labyrinth[i]==" ":
                road.append(i)
            i+=1
        print(walls)
        print(road)


#Objets à ramasser.
        objects=[]#cases "objets" créées de manière aléatoire à partir de la liste 'road' (NB : ces cases sont à la fois dans les listes 'objects' et 'road')
        objects.append(Object("tube"))
        objects.append(Object("aiguille"))
        objects.append(Object("ether"))
        #Créer la position / numéro de case où se trouvera chaque objet à ramasser, à partir de la liste des passages.
        i=0
        while i<Object.objects_counter: #on crée autant de chiffres qu'il existe d'instances de la classe Object.
            number=random.randint(0, self.numberOfSquares-1)
            if number in road:
                objects[i].position = number
        i+=1
        print(objects[0].name + str(objects[0].position))
        print(objects[1].name + str(objects[1].position))
        print(objects[2].name + str(objects[2].position))

    
class Object:
    objects_counter = 0 #compteur d'instances de la classe.
    def __init__(self, name):
        self.name = name #nom de l'objet
        self.position = 0 #numéro de case par défaut
        Object.objects_counter += 1 #incrément le compteur d'instance de classe Object.



#McGyver = startPosition (case 0) + objectsCounter ()
class Hero:
    def __init__(self):
        self.position = 0 #emplacement dans le labyrinthe exprimé en numéro de case, case 0 au début du jeu.
        self.objectsCounter = 0 #objets ramassée, aucun par défaut au début du jeu.
        self.picture = "images/hero.jpg" #ACTUALISER / CORRIGER

    def move(self, direction):
        movement=0
        
        if direction == "right":
            movement=1
        elif direction == "left":
            movement=-1
        elif direction == "up":
            movement=-width
        elif direction == "down":
            movement=width
        
        #Si le déplacement envisagé conduit à une case "chemin" (ou une case "objet" figurant à la fois dans les listes 'road' et 'objects')
        #Implicitement, le déplacement est >=0 et <numberOfSquares)
        if self.position+movement in road:
            self.position+=movement
        else: #Si le déplacement conduit à une case "mur" ou sort des limites du plateau de jeu (résultat négatif ou supérieur au numéro de la case de fin)
            movement=0
        
        
    
#Ramasser un objet.
#Ajouter 1 au compteur d'objets.
#Supprimer le numéro de case de l'objet de la liste 'objects' (NB : la case est toujours présente dans la liste 'road').
        if self.position in objects:
            self.objectsCounter+=1
            a=self.position
            objects.remove(a)

#Finir le jeu (dernière case).
#Vérifier si tous les objets ont été ramassés.


#---------------#
#PyGame : représenter une case 'chemin' avec l'image correspondante, sauf s'il s'agit d'une case 'objet'.
#if square in road:
#    if square not in objects:
#        picture = 1 #ACTUALISER POUR PYGAME
