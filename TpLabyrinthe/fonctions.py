def move_N(coord):
    """return la valeur de l'ordonnée à soustraire"""
    return -int(coord[1])
    

def move_S(coord):
    """return la valeur de l'ordonnée à additionner"""
    return int(coord[1])

def move_E(coord):
    """return la valeur de l'abscisse à additionner"""
    return int(coord[1])

def move_W(coord):
    """return la valeur de l'abscisse à soustraire"""
    return -int(coord[1])

def save_quit():
    return 'n'

def check_answer(chaine):
    """Fonction qui s'aasure que le joueur a bien tpare un des lettres voulue"""
    l_chaine = list(chaine)
    if len(l_chaine) ==1:
        l_chaine.append(1)
    if l_chaine[0] in ['N', 'S', 'E', 'W', 'Q'] and len(l_chaine)<3:
        return l_chaine
    else:
        return None