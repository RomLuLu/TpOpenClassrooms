"""Classe carte"""

class Carte:
    """Classe qui permet de sauvegarder la carte en cour
        attribut de classe 'compteur' pour savoir si une carte est en
        cours. 0 si non 1 si oui."""
    compteur = 0 #
    def __init__(self,nom ='', path=''):
        self.nom = nom  # le nom du fichier qui sera chargé.
        self.path = path  # le chemin vars la carte

    def __str__(self):
        return "Voici le labyrinthe : {0}".format(self.nom)

    def recup_strutcure(self):
        """Fonction récupérant les chaines de caractères du fichier"""
        with open(self.path, 'r') as f:
            structure_laby = f.read()
        return structure_laby

    def save_auto(self,dictionnaire ):
        """Fonction recréer la chaine de caractère à partir d'un dictionnaie et la save"""
      