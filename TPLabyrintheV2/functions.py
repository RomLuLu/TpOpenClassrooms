

# INSTRUCTIONS.

def instructions():
    commands = ("up(North) -> 'N'.\ndown(South) -> 'S'."
                "\nright(East) -> 'E'.\nleft(West) -> 'W'."
                "\nif cardinal letter is following by number, this number "
                "equal number of cases.")
    print("Welcome to Labyrinthe !")
    print("to move robot, you need to use this commands:")
    print(commands)
    print("Use command 'Q' to  save and quit program.")


def simple_instruction():
    commands = ("up -> 'N'.down -> 'S'."
                "right -> 'E'.left -> 'W'."
                "quit -> 'Q'")
    print("Recall princpal commands :")
    print(commands)

# GESTION OF INPUTS PLAYER.


def display_maps(liste):
    for i, item in enumerate(liste, 1):
        print("<{0}> : {1}".format(i, item[:-3]))


def selection_carte_player(liste):
    index = ''
    while not (type(index) == int):
        index = input("Entrer le N° de la carte : ")
        try:
            index = int(index)
        except:
            print("Erreur de saisi !")
            index = ''
        else:
            try:
                return liste[index-1]
            except IndexError:
                print("Votre choixn'est pas dans la liste")
                index = ''


def position_selection():
    coord = ''
    while not coord.isalnum():
        coord = input("Enter the next robot move : ").upper()
        if coord[0] not in ['N', 'S', 'E', 'W', 'Q']:
            print("Wrong letter try again !")
            coord = ''
        elif len(coord) > 3:
            print("Seized too long !")
            coord = ''
    if coord == 'Q':
        return 'Q'
    elif len(coord) == 1:
        coord += '1'
        return (coord[0], int(coord[1]))
    else:
        return (coord[0], int(coord[1]))