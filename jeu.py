from classes import *
from fonctions import *


#GAME-----
play = 1 #Le joueur souhaite jouer si play == 1, sinon il souhaite s'arrêter.
while play == 1:
    #Vider les listes 'road', 'walls' et 'objects'.
    del(road[:])
    del(walls[:])
    del(objects[:])
    Labyrinth.GAME = 1 #début de partie
    while Labyrinth.GAME == 1: #La partie commence si Labyrinth.GAME == 1, sinon elle se termine.
        labyrinth = Labyrinth() #Initialiser le plateau de jeu.
        macGyver = Hero() #Initialiser le héros.
        place_objects() #Créer de manière aléatoire la position des objets.

        #Déterminer les objets à partir des positions créées de manière aléatoire dans 'objects'.
        tube = objects[0]
        needle = objects[1]
        ether = objects[2]


        #VERIFICATION-----
        #Scénario d'événements au clavier.
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
        print("\nAprès avoir retiré les objets trouvés, la liste 'objects' ne contient plus que " + str(len(objects)) + " objets à la fin du jeu.")
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

    choice = input("q pour quitter, autre touche pour jouer une nouvelle partie : ")
    if choice == "q":
        play = 0
    elif choice == "o":
        play = 1
