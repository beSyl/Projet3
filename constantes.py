#VARIABLES-----
list_labyrinth=[]#Toutes les cases, numérotées de 0 à ALL_SQUARES-1.
walls=[x for x in list_labyrinth if x=="X"]
road=[x for x in list_labyrinth if x==" "]
objects=[]#Cases "objets" créées de manière aléatoire à partir de la liste 'road' (NB : ces cases sont à la fois dans les listes 'objects' et 'road')


#IMAGES-----
