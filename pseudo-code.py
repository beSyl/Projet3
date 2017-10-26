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
while i<225:
    labyrinth.append((x,y)) #ajout d'un nouveau tuple de coordonnées dans la liste.
    if y<14:
        y+=1
    else:
        if x<14:
            x+=1
            y=0
    i+=1

#print(labyrinth)#Afficher le contenu de la liste labyrinth.


#----------
#CLASSES
#class Labytinth:
#   HEIGHT_MAX = 15 #hauteur maxi en nombre de cases
#   WIDTH_MAX = 15 #largeur maxi en nombre de cases
#   def __init__(self):
#       pass

#class Character: #
#   pass


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
