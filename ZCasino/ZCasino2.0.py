import random
from math import ceil
import time


def choix_mise():
    """Fonction qui retourne la mise sous forme d'entier"""
    mise = ''
    while not mise.isdigit() :
        mise = input("Entrer votre mise (nombre entier attendu) : ")    
    mise = int(mise)
    return mise

def choix_numero_joueur():
    numero_joueur = ''
    while not numero_joueur.isdigit():
        numero_joueur = input("Entrer un entier compris entre 0 et 49 : ")   
    numero_joueur = int(numero_joueur)
    return numero_joueur

def choix_numero_ordinateur():
    numero_ordinateur = random.randrange(0,50)
    return numero_ordinateur

def resultat(numero_joueur, numero_ordinateur):
    if numero_joueur == numero_ordinateur:
        return 1
    elif numero_joueur%2 == numero_ordinateur%2:
        return 2
    else:
        return 3


def resulat_gain(resultat,mise_jeu):
    if resultat == 1:
        gain = mise_jeu + 3 * mise_jeu
    elif resultat == 2:
        gain = mise_jeu + mise_jeu*0.5
    else :
        gain = 0
    return ceil(gain)


def quitter(continuer):
    continuer = ''
    while not (continuer =='n' or continuer =='o'):
        continuer =input("Continuer ?? (o/n) : ").lower()
    return  continuer

# programme:


print("Sélection de la mise de départ : ")
mise_depart = choix_mise()
continuer = 'o'
while continuer == 'o':

    #entrée dans le jeu :
    print("rappel des règles : ")
    print("""
    -> 50 numéros de 0 à 49.\n
    -> si vous trouvez le bon numéro vous récupérez votre mise + 3 fois votre mise.\n
    -> si bonne couleur mais mauvais numéro : mise + 50% de votre mise.\n
    -> sinon vous perdez votre mise.\n
        """)

    #choix mise à jouer:
    mise_jeu = 0
    while mise_jeu > mise_depart or mise_jeu <=0 :
        mise_jeu = choix_mise()
    mise_depart -=mise_jeu
    time.sleep(1)
    #choix du numéro joueur:
    
    numero_joueur = choix_numero_joueur()
    while numero_joueur not in range(49):
        numero_joueur = choix_numero_joueur()
    
    #choix du numéro ordinateur:
    time.sleep(1)
    print("La roulette est lancée !!!!!!")
    time.sleep(1)
    numero_ordinateur = choix_numero_ordinateur()
    print("la bille est  tombée sur le numéro {}.".format(numero_ordinateur))
    time.sleep(1)

    #resultat :
    resultat = resultat(numero_joueur, numero_ordinateur)
    if resultat ==1 :
        print("Félicitation vous avez gagnez .vous gagnez : {0} $".format(resulat_gain(resultat, mise_jeu)))
    elif resultat == 2:
        print("Félicitation vous avez gagnez .vous gagnez : {0} $".format(resulat_gain(resultat, mise_jeu)))
    else :
        print("Désolé")

    mise_depart+=resulat_gain(resultat, mise_jeu)
    
    #continuer ou pas :

    continuer = quitter(continuer)


print("Vous quittez le ZCasino avec : {0} $.".format(mise_depart))