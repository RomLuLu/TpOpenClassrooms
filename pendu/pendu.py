import os
from fonctions import *


# on recupère le fichier scores ou on le crée.
if os.path.isfile('scores'):
    score = recuperer_score()
else :
    creer_score(score)

# on demande le pseudo au joueur.

pseudo = ''
while len(pseudo) <3 :
    pseudo = input("Entrer votre pseudo (lettre et chiffre accepte et plus de 3 characteres) : ")
    if not pseudo.isalnum():
        continue
    
# on ajoute le pseudo au dictionnaire 'score':
score[pseudo] = 0

# On choisi le mot a trouver:
mot_a_trouver = random_word(words)
print(mot_a_trouver)
#j'affiche la sequence de mot  sous forme de '*'
print("Voici le mot à trouver : ")
mot_transforme= mot_cache(mot_a_trouver)
print(mot_transforme)
print()


# on rentre dans le jeu :

while chances >0:

    # on affiche le nombre de score a chaque tour
    print("Il vous reste {0} chance(s)".format(chances))
        
    # je demande a l'utilisateur de saisir une lettre.
    lettre = ''
    while len(lettre) >1 or lettre == '' or not lettre.isalpha():
        lettre = (input("Entrer votre lettre : ")).lower()
    
    #on verifie si ma mettre appartient bien  au mot
    if lettre in mot_a_trouver:
        mot = verification(mot_transforme, mot_a_trouver, lettre)
        mot_transforme = mot
        print(mot_transforme)
        # on verifie que tout le mot est trouvé.
        if mot_transforme == mot_a_trouver :
            total_score = chances
            print("Vous avez gagnez, votre score est de {0} point(s)".format(total_score))
            break
    else :
        print(mot_transforme)
        chances -=1

#on recupère le score et l'enregistre dans le fichier 'scores'
score[pseudo] = total_score
creer_score(score)

#On demande si on veux afficher les scores des autres joueurs.
reponse = ''
while not (reponse == 'o' or reponse == 'n'):
    reponse = (input("voulez vous voir les scores ?? (o/n) : ")).lower()

if reponse == 'o':
    score  = recuperer_score()
    print(score)
else:
    print("Au revoir !!!!")


      