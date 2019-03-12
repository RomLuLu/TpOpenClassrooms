"""
Jeu Donkey Kong Labyrinthe
Jeu dans lequel on doit déplacer DK jusqu'aux bananes à travers un labyrinthe.

Script Python
files : main.py, niveau.py, perso.py, constantes.py
Directory:
-> levels : level1, level2
-> images : sprites
"""
import sys, pygame
from pygame import locals as const
from constantes import *
from niveau import Niveau
from perso import Perso


def main():
    pygame.init()
    screen = pygame.display.set_mode(size)
    # Logo:
    icone = pygame.image.load(icone_path).convert_alpha()
    pygame.display.set_icon(icone)
    # Title:
    pygame.display.set_caption("DKLabyrinthe")
    # menu:
    acceuil = pygame.image.load(accueuil_path).convert_alpha()
    screen.blit(acceuil, (0, 0))
    # fond:
    font = pygame.image.load(font_path).convert()
    screen.blit(font, (0, 0))
    # refresh display
    pygame.display.flip()

    while 1:
        pygame.time.Clock().tick(30)
        # loop menu:
        start_acceuil = 1
        while start_acceuil:
            pygame.time.Clock().tick(30)
            screen.blit(acceuil, (0, 0))
            pygame.display.flip()
            for event in pygame.event.get():
                # Close window with cross:
                if event.type == const.QUIT:
                    sys.exit()
                # selection level:
                elif event.type == const.KEYDOWN:
                    if event.key == const.K_F1:
                        n1 = Niveau(level1, screen)
                        n1.import_map()
                        singe = Perso(n1.walls, n1.start, n1.arrival, n1.export_map())
                        start_acceuil = 0
                    elif event.key == const.K_F2:
                        start_acceuil = 0
        
        start_game = 1
        while start_game:
            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                if event.type == const.KEYDOWN and event.key == const.K_ESCAPE:
                    start_game = 0
            singe.move()
            pygame.display.flip()
            

if __name__ == "__main__":
    main()
