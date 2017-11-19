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