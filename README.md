EN
"Help MacGyver to escape!"
OpenClassrooms DA Python Course - Project 3
-----

The file 'jeu.py' corresponds to the program whose modules are 'contantes.py', 'Labyrinth.py' (class), 'Hero.py' (class).
The file 'labyrinth.txt' represents the structure of the game using lines of characters.
The 'images' directory

The maze is seen as a game board with 15 lines (numbered from 0 to 14) and 15 columns (numbered from 0 to 14).

To materialize it, one writes a file 'labyrinth.txt' of 15 lines composed of 15 characters each.
These characters symbolize either a 'path' box through which MacGyver can move if it is a '' space '' character, or a 'wall' box that prevents MacGyver from moving around if it is a character "X".

We instantiate a labyrinth from the class 'Labyrinth'.
We instantiate the MacGyver character (instance 'macGyver') from the class 'Hero'.
We randomly position 3 objects on the path that MacGyver can traverse.

A position is determined along the x and y axes (abscissa and ordinate).
The character starts at the top left of the labyrinth (x = 0, y = 0).
The end of the labyrinth is at the bottom right of the labyrinth (x = 14, y = 14).

The player wins if he manages to drive MacGyver to the finish square after picking up the 3 items.
If he has not picked up all the objects by reaching the end, he loses.


----------
FR
"Aidez MacGyver à s'échapper !"
OpenClassrooms parcours DA Python - projet 3
-----

Le fichier 'jeu.py' correspond au programme dont les modules sont 'contantes.py', 'Labyrinth.py' (classe), 'Hero.py' (classe).
Le fichier 'labyrinth.txt' représente la structure du jeu à l'aide de lignes de caractères.
Le répertoire 'images'

Le labyrinthe est vu comme un plateau de jeu de 15 lignes (numérotées de 0 à 14) et 15 colonnes (numérotées de 0 à 14).

Pour le matérialiser, on rédige un fichier 'labyrinth.txt' de 15 lignes composées de 15 caractères chacune.
Ces caractères symbolisent soit une case 'chemin' via laquelle MacGyver peut se déplacer s'il s'agit d'un caractère espace «  », soit une case 'mur' empêchant MacGyver de se déplacer s'il s'agit d'un caractère « X ».

On instancie un labyrinthe à partir de la classe 'Labyrinth'.
On instancie le personnage MacGyver (instance 'macGyver') à partir de la classe 'Hero'.
On positionne 3 objets de manière aléatoire sur le chemin que MacGyver peut parcourir.

Une position se détermine selon les axes x et y (abscisse et ordonnée).
Le personnage débute en haut à gauche du labyrinthe (x=0, y=0).
La fin du labyrinthe se situe en bas à droite du labyrinthe (x=14, y=14).

Le joueur gagne s'il parvient à conduite MacGyver jusqu'à la case d'arrivée après avoir ramassé les 3 objets.
S'il n'a pas ramassé tous les objets en atteignant la fin, il perd.