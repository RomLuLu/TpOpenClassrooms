class Labyrinthe:

    def __init__(self, path):
        # path too the map.
        self.path = path
        # map converted to a string.
        self.string_map = self.import_map()
        # self.structure contains all items of labyrinthe.
        self.walls = set()
        self.paths = set()
        self.doors = set()
        self.robot = 0
        self.out = 0
        self.x_max, self.y_max = 0, 0

    def import_map(self):
        """import map into my class labyrinthe"""
        with open(self.path, 'r') as f:
            # str_map = f.read()  # <= faire readlines()
            str_map = f.readlines()
        return str_map

    def position_items(self):
        # self.x_max == position max de x idem pour self.y_max.
        self.x_max = len(self.string_map) - 1
        self.y_max = len(self.string_map[0]) - 1
        for x, line in enumerate(self.string_map):
            for y, col in enumerate(line):
                if col == 'X':
                    self.paths.add((x, y))
                    self.robot = (x, y)
                elif col == 'U':
                    self.paths.add((x, y))
                    self.out = (x, y)
                elif col == ' ':
                    self.paths.add((x, y))
                elif col == '.':
                    self.paths.add((x, y))
                    self.doors.add((x, y))
                elif col == 'O':
                    self.walls.add((x, y))

    def export_map(self):
        chaine = ''
        for x in range(self.x_max + 1):  # 0 -> 11
            for y in range(self.y_max):  # 0 -> 11
                if (x, y) == self.robot:
                    if (x, y) == self.out:
                        chaine += 'X' + '\n'
                    else:
                        chaine += 'X'
                elif (x, y) in self.doors:
                    chaine += '.'
                elif (x, y) in self.walls:
                    if (x, y) == (x, self.y_max - 1):
                        chaine = chaine + 'O' + '\n'
                    else:
                        chaine += 'O'
                elif (x, y) == self.out:
                    chaine += 'U' + '\n'
                elif (x, y) in self.paths:
                    chaine += ' '
        return chaine

    def available_position(self, card):
        (x, y) = self.robot
        list_position = []
        if card[0] in ['N', 'S']:
            if card[0] == 'N':
                (x, y) = x - card[1], y
            elif card[0] == 'S':
                (x, y) = x + card[1], y
            if (x, y) in self.walls:
                return False
            #  all position on 'x' between x and self.robot add to list
            d = self.robot[0] - x
            if d > 0:
                for i in range(d+1):
                    list_position.append((self.robot[0] - i, y))
            elif d < 0:
                for i in range(abs(d+1)):
                    list_position.append((self.robot[0] + i, y))
        elif card[0] in ['E', 'W']:
            if card[0] == 'E':
                (x, y) = x, y + card[1]
            elif card[0] == 'W':
                (x, y) = x, y - card[1]
            if (x, y) in self.walls:
                return False
            #  checking all position on 'y' between y and self.robot
            d = self.robot[1] - y
            if d > 0:
                for i in range(d+1):
                    list_position.append((x, self.robot[1] - i))
            elif d < 0:
                for i in range(abs(d+1)):
                    list_position.append((x, self.robot[1] + i))
        #  Just one position in self.walls and position not available
        c = 0
        for item in list_position:
            if item in self.walls:
                c = 1
        if c == 1:
            return False
        else:
            self.robot = (x, y)

    def winner(self):
        if self.robot == self.out:
            return 'Q'
        elif self.robot[0] == self.out[0] and self.robot[1] > self.y_max:
            self.robot = self.out
            return 'Q'


# if __name__ == "__main__":
#     labi = Labyrinthe(r"cartes\facile.txt")
#     labi.position_items()
#     print(labi.export_map())
#     if labi.available_position(('E', 1)) == 0:
#         print("Are you a ghost  ???")
#     else:
#         print(labi.export_map())