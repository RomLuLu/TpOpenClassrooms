import os
import pygame.locals as c

def path_to_images(image=''):
    """Function for all path to the directory images"""
    path = os.path.join(os.path.dirname(__file__), "images\\{}".format(image))
    return path


def path_to_level(level=''):
    """Function for all path to the directory levels"""
    path = os.path.join(os.path.dirname(__file__), "levels\\{}".format(level))
    return path

# size if the screen:
size = width, height = 450, 450

# sprites:
# taille en pi
taille_sprite = 30
# max sprites:
sprite_max = 450
# nombre de sprites sur une ligne:
nb_sprite_line = 15
# chemin vers les sprites:
accueuil_path = path_to_images('accueil.jpg')
arrival_path = path_to_images('arrivee.png')
star_path = path_to_images('depart.png')
dk_bas_path = path_to_images('dk_bas.png')
dk_droite_path = path_to_images('dk_droite.png')
dk_gauche_path = path_to_images('dk_gauche.png')
dk_haut_path = path_to_images('dk_haut.png')
font_path = path_to_images('fond.jpg')
icone_path = path_to_images('icone.jpg')
wall_path = path_to_images('mur.jpg')

# chemin vers les niveaux:
level1 = path_to_level('level1.txt')
