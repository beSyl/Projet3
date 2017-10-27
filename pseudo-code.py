#----------
#STRUCTURE LABYRINTHE

#1re POSSIBILITÉ : le labyrinthe est un fichier txt 
#fichier txt composé de 15 lignes de 15 lettres
#lettre "s" pour "start" (départ de MacGyver)
#lettre "e" pour "end" (gardien)
#lettre "X" pour un mur
#caractère " " pour un passage
#chiffres 1, 2 et 3 pour les 3 objets

#2e POSSIBILITÉ : à chaque case du plateau de jeu correspond des coordonnées (format "hauteur, largeur" : (1, 1), (12, 4), ... - 225 cases au total pour un carré de 15 cases de largeur)
#labyrinthe = [] => liste de 225 tuples, de (0,0) à (14,14)
#à chaque début de jeu, choix de N murs, 3 objets, 1 gardien et 1 macgyver (1 objet ne peut pas être un mur, etc.) : le reste correspond au chemin
#déplacement = largeur+1 (ou hauteur, ou -1 selon touche clavier)

#Structure du labyrinthe et de ses cases.
x=0 #hauteur.
y=0 #largeur.
labyrinth=[] #liste des coordonnées des 225 cases du plateau de jeu.

i=0
while i<225: #NB : faire correspondre au nombre d'éléments dans la
    labyrinth.append([x, y]) #ajout d'un nouveau tuple de coordonnées dans la liste.
    if y<14:
        y+=1
    else:
        if x<14:
            x+=1
            y=0
    i+=1

print(labyrinth)#Afficher le contenu de la liste labyrinth.

#importer le fichier labyrinth.txt en tant que file
#Mettre le fichier txt "à plat" dans une liste, i.e. liste de 225 éléments plutôt qu'une référence hauteur/largeur
list_labyrinth = []
#ID = ligne*15+largeur #pour une case en ligne 2 colonne 7, [2, 7] : 2*15+7 = ID[37] #la ligne 0 est ainsi neutralisée pour ne conserver que la largeur comme ID.
#intégrer les
for line in file: #tant qu'il y a un élément dans le fichier:
    for element in line: #l'élément est déterminé par hauteur/largeur
        if element!="/n": #sauf s'il s'agit d'un saut de ligne
            list_labyrinth.append([line, element]) #ajouter l'élément dans list_labyrinth


#Créer une liste qui contiendra les ID 

    
    
for element in Walls(): #lister toutes 

#----------
#CLASSES
#class Labytinth:
#   HEIGHT_MAX = 15 #NB: hauteur maxi à capter depuis le fichier labyrinth.txt afin qu'il évolue si besoin
#   WIDTH_MAX = 15 #largeur maxi en nombre de cases
#   def __init__(self):
#       self.macGyver = [0, 0, "image.jpg"] #NB : lier l'image associée 
#       self.guardian = [self.HEIGHT_MAX, self.WIDTH_MAX, "image.jpg"] #NB : lier l'image associée #IMPORTANT: est-ce utile s'il y a un "e" dans labyrinth.txt ?

def make_walls(): #fonction servant à créer les murs
    walls = []
    i=0
    while i<HEIGHT_MAX.Labyrinth*WIDTH_MAX.Labyrinth:
        if list_labyrinth[i]=="X": #si l'élément est un X, il est intégré à la liste de murs
            labyrinth[i]= walls.append(i)
    #les X symbolisent les murs, la liste walls conserve leur ID qui correspond également à celui de la list labyrinth
    #VERIFIER si la suite de la condition est nécessaire : la fin du jeu est déterminée par la position du gardien...
        elif list_labyrinth[i]=="e":
            for x, y in list-labyrinth:
                guardian = [x, y]




#class Character: #
#   pass


guardian=Character()
guardian(HEIGHT_MAX.labyrinth, WIDTH_MAX.labyrinth) #la position du gardien est évolutive et s'ajuste si labyrinth.txt change de dimensions.

#class Movement:
#    def __init__(self):
#        self.degree = 1 #nombre de sprites parcours à chaque événement au clavier

#class Wall:
#    def __init__(self,height,width,picture):
#        self.height = height #coordonnée en hauteur
#        self.width = width #coordonnée en largeur
#        self.picture = picture #appeler l'image stocké dans un fichier
#    def list(self):
        self.list = []
        
#       




#----------
#CONSTANTES
#dimensions labyrinthe (ou attributs de class Labyrinth ?)
#images


#----------
#JEU
#BOUCLE PRINCIPALE:
#   BOUCLE DE MENU:
#       "jouer", "règles du jeu" ou "quitter"   
#       fin de la boucle de menu
#   BOUCLE DE JEU:
#       fin de la boucle de jeu
