#-*- coding : Latin-1 -*-

import os 
from carte import Carte
from labyrinthe import Labyrinthe
from fonctions import *

#Récuperer fichiers du dossier carte:
liste_de_cartes = []
for carte in os.listdir("cartes"): #['facile.txt', 'prison.txt']
    if carte.endswith('txt'):
        liste_de_cartes.append(carte[:-3].lower())
print(liste_de_cartes)        

#Afficher les cartes présentes pour l'utilisateur:
def afficher_choix_cartes():
    for i, carte in enumerate(liste_de_cartes):
        print("<{0}> : {1}".format(i+1, carte))
afficher_choix_cartes()

#Récupere une partie en cour:

#Demander à l'utilisateur de chosir la carte:
num_carte = int(input("Entrez un numéro de labyrinthe pour\
 commencer à jouer :"))
Carte.compteur = 1 # J'indique qu'une carte est en cours / en fin de game c=0

#Instanciation de classe Carte
nom_carte = liste_de_cartes[num_carte-1] + 'txt'
path_carte = os.path.join("cartes", nom_carte)
carte = Carte(liste_de_cartes[num_carte-1] ,path_carte)

#Instanciation de la classe Labyrinthe
##Transfère de de la carte en coordonnée.
structure = carte.recup_strutcure() # on creer une str avec le fichier
labi = Labyrinthe(structure)


#PLACE AU JOUEUR:
print(structure)
robot = {
    "N":move_N, 
    "S":move_S, 
    "E":move_E, 
    "W":move_W,
    "Q":save_quit
    }

continuer = 'o'
while continuer != 'n' :

    move_player = input("Taper une direction (N,S,E,W,Q) : ").upper()
    coord = check_answer(move_player) # une liste
    if coord == None:
        print("Erreur de saisi") 
        continue # a virer car sinon on est dans le else
    else:
        if coord[0] == 'N' or coord[0] == 'S':
            y = robot[coord[0]](coord)
            structure  = labi.ordonne(y)
            
        elif coord[0] == 'E' or coord[0] == 'W':
            x = robot[coord[0]](coord)
            print(x)
        elif coord[0] == 'Q':
            continuer = robot[coord[0]]()