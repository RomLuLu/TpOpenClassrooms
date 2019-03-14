import pygame, sys
import pygame.locals as const
from constantes import *
from niveau import Niveau


class Perso:

    def __init__(self, niveau):
        self.niveau = niveau
        # On charge les images du singe
        self.dk_bas = pygame.image.load(dk_bas_path).convert_alpha()
        self.dk_haut = pygame.image.load(dk_haut_path).convert_alpha()
        self.dk_droite = pygame.image.load(dk_droite_path).convert_alpha()
        self.dk_gauche = pygame.image.load(dk_gauche_path).convert_alpha()
        # On attribut au singe la position de départ :
        self.position = self.dk_droite
        # Position du singe en x et y:
        self.x = 0
        self.y = 0

    def move(self, direction):
        # direction vers le bas:
        if direction == 'bas':
            if (self.x, self.y + BAS) not in self.niveau.walls or (self.y + BAS) > sprite_max:
                self.x = self.x
                self.y = self.y + BAS
            self.position = self.dk_bas

        # direction vers le haut:
        if direction == 'haut':
            if (self.x, self.y + BAS) not in self.niveau.walls or (self.y + HAUT) < 0:
                self.x = self.x
                self.y = self.y + HAUT
            self.position = self.dk_haut

        # direction vers la droite:
        if direction == 'droite':
            if (self.x + DROITE, self.y) not in self.niveau.walls or (self.x + DROITE) < 0:
                self.x = self.x + DROITE
                self.y = self.y
            self.position = self.dk_droite

        # direction vers la gauche:
        if direction == 'gauche':
            if (self.x + GAUCHE, self.y) not in self.niveau.walls or (self.x + GAUCHE) < 0:
                self.x = self.x + GAUCHE
                self.y = self.y
            self.position = self.dk_gauche
