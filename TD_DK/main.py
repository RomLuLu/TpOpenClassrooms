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
    # fond:
    fond = pygame.image.load(font_path).convert()

    boucle_jeu = 1
    while boucle_jeu:
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
                        choix = path_to_level('level1.txt')
                        start_acceuil = 0
                    elif event.key == const.K_F2:
                        choix = path_to_level('level2.txt')
                        start_acceuil = 0

        # Chargement du niveau:
        niveau = Niveau(choix, screen)
        niveau.import_map()
        niveau.export_map()

        # Création de dk:
        dk = Perso(niveau)
        print(dk.x)
        start_game = 1
        while start_game:
            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                if event.type == const.QUIT:
                    sys.exit()
                elif event.type == const.KEYDOWN and event.key == const.K_ESCAPE:
                    start_game = 0
                elif event.type == const.KEYDOWN:
                    if event.key == const.K_DOWN:
                        dk.move('bas')
                    elif event.key == const.K_UP:
                        dk.move('haut')
                    elif event.key == const.K_RIGHT:
                        dk.move('droite')
                    elif event.key == const.K_LEFT:
                        dk.move('gauche')

            # affichage des différents écrans.
            screen.blit(fond, (0, 0))
            niveau.export_map()
            screen.blit(dk.position, (dk.x, dk.y))
            pygame.display.flip()

            # condition pour gagner:
            if (dk.x, dk.y) == dk.niveau.arrival:
                start_game = 0

if __name__ == "__main__":
    main()
