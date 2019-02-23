"""Classe Labyrinthe"""

class Labyrinthe:
    """Classe qui va gérer tous les mouvements du joueur en les traduisants
    en position valide ou non"""
    derniere_position = ' '
    def __init__(self, chaine):
        self.structure = {}
        self.robot = tuple()
        self.sortie = tuple()
        self.door = {}
        
        #récupération de la map en coordonnées
        x, y = 0, 0
        for c in chaine:
            if c == '\n':
                x, y = 0, y+1
            else:
                self.structure[(x,y)] = c
                x+=1

        #récupération des coordonnées du robot et de la sortie
        for key, value in self.structure.items():
            if value == 'X':
                self.robot = key
            elif value == 'U':
                self.sortie = key

        #Récupération des coordonnée de portes:
        for key, value in self.structure.items():
            if value == '.':
                self.door[key] = value
        
    def ordonne(self, val_y):        
        # on calcule les nouvelles coordonnées:
        n_coord = (self.robot[0], self.robot[1]+val_y)        
        # on verifie si c'est une position valide:
        if self.structure[n_coord] == 'O':
            print("Vous ne pouvez ps traversez le mûr !!!")
        elif self.structure[n_coord] == '.':
            self.structure[self.robot] = ' '
            self.structure[n_coord] = 'X'



