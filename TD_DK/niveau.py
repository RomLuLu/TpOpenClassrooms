import pygame, sys
import pygame.locals as const
from constantes import *


class Niveau:

    def __init__(self, path_level, ecran: pygame.Surface):
        self.ecran = ecran
        self.path_level = path_level
        # Liste qui conserve toutes les positions de sprites.
        self.structure_level_sprites = []
        self.walls = []
        self.paths = []
        self.start = tuple()
        self.arrival = tuple()

    def import_map(self):
        x, y = 0, 0
        with open(self.path_level, 'r') as f:
            structure_level = f.readlines()
            for line in structure_level:
                for c in line.strip():
                    self.structure_level_sprites.append((x, y))
                    if c == 'd':
                        self.paths.append((x, y))
                        self.start = (x, y)
                    elif c == 'a':
                        self.paths.append((x, y))
                        self.arrival = (x, y)
                    elif c == '0':
                        self.paths.append((x, y))
                    else:
                        self.walls.append((x, y))
                    x += taille_sprite
                x, y = 0, y + taille_sprite

    def export_map(self):
        for sprite_position in self.structure_level_sprites:
            if sprite_position in self.walls:
                wall = pygame.image.load(wall_path).convert_alpha()
                self.ecran.blit(wall, sprite_position)
            elif sprite_position == self.start:
                start = pygame.image.load(star_path).convert_alpha()
                self.ecran.blit(start, sprite_position)
            elif sprite_position == self.arrival:
                arrival = pygame.image.load(arrival_path).convert_alpha()
                self.ecran.blit(arrival, sprite_position)
