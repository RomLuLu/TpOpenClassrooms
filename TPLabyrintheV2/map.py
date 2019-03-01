import os


class Map:

    def __init__(self, name):
        self.name = name
        self.path = r"cartes\{}".format(self.name)

    def save_map(self, filename):
        """Method that records in a file the player's progress"""
        if self.name.startswith("save_"):
            self.name = self.name[5:]
        with open(r"cartes\save_{}".format(self.name), 'w') as f:
            f.write(filename)

    def remove_save_game(self):
        os.remove(self.path)