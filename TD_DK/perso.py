import pygame, sys
import pygame.locals as const
from constantes import *
from niveau import Niveau


class Perso:

    def __init__(self, walls, start, arrival, niveau):
        self.walls = walls
        self.start = start
        self.arrival = arrival
        self.niveau = niveau
        # Nouvelle ecran qui garde la trace du précédent.
        self.ecran = self.niveau
        # On charge les images du singe
        self.dk_bas = pygame.image.load(dk_bas_path).convert_alpha()
        self.dk_haut = pygame.image.load(dk_haut_path).convert_alpha()
        self.dk_droite = pygame.image.load(dk_droite_path).convert_alpha()
        self.dk_gauche = pygame.image.load(dk_gauche_path).convert_alpha()
        # On attribut au singe la position de départ :
        self.position = self.start

    def move(self):
        for event in pygame.event.get():
            if event.type == const.QUIT:
                sys.exit()
            elif event.type == const.KEYDOWN:
                if event.key == const.K_DOWN:
                    n_pos = self.position[0], self.position[1] + taille_sprite
                    if n_pos not in self.walls and n_pos[1] < sprite_max:
                        self.position = n_pos
                        self.niveau.blit(self.dk_bas, self.position)
                if event.key == const.K_UP:
                    n_pos = self.position[0], self.position[1] - taille_sprite
                    if n_pos not in self.walls and n_pos[1] >= 0:
                        self.position = n_pos
                        self.niveau.blit(self.dk_haut, self.position)
                if event.key == const.K_RIGHT:
                    n_pos = self.position[0] + taille_sprite, self.position[1]
                    if n_pos not in self.walls and n_pos[0] < sprite_max:
                        self.position = n_pos
                        self.niveau.blit(self.dk_droite, self.position)
                if event.key == const.K_LEFT:
                    n_pos = self.position[0] - taille_sprite, self.position[1]
                    if n_pos not in self.walls and n_pos[0] >= 0:
                        self.position = n_pos
                        self.niveau.blit(self.dk_gauche, self.position)
