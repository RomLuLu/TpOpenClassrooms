import pickle
import random
from donnees import *

#  creer le fichier scores avec score vide
def creer_score(score):
    with open('scores', 'wb') as f:
        fichier_pickler  = pickle.Pickler(f)
        fichier_pickler.dump(score)

#Si le fichier scores existe on le recupère et on le charges   
def recuperer_score():
    with open('scores', 'rb') as f:
        fichier_depickler = pickle.Unpickler(f)
        score_recupere = fichier_depickler.load()
    return score_recupere


# checker si le pseudo existe déjà: (en standbye)

def checker_pseudo(pseudo, score):
    for key in score.keys():
        if key == pseudo:
            return "le pseudo {0} est déjà utilisé.".format(pseudo)
        else :
            score[pseudo] = 0
            return score

# Choix du mot a trouver

def random_word(words):
    mot_a_trouver = random.choice(words)
    return mot_a_trouver

# on cache le mot à trouver :

def mot_cache(mot_a_trouver):
    l = len(mot_a_trouver)
    mot_cache = ['*']*l
    mot_cache = ''.join(mot_cache)
    return mot_cache

# verification si la lettre appartient bien au mot a trouver
def verification(mot, mot_a_trouver, lettre): 
    liste_mot= list(mot)
    liste_mot_a_trouver = list(mot_a_trouver)
    for i, letter in enumerate(liste_mot_a_trouver):
        if letter == lettre:
            liste_mot.pop(i)
            liste_mot.insert(i, letter)
    mot = ''.join(liste_mot)
    return mot






