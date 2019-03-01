
import os
from functions import *
from labyrinthe import Labyrinthe
from map import Map

# CARD MANAGEMENT LOADING THE PROGRAM.

path = r"C:\Users\Romain\labyrinthe\TP\cartes"
list_maps = os.listdir(path)
# dispay maps list:
display_maps(list_maps)
# map selection :
playing_card = selection_carte_player(list_maps)
print(playing_card)

# link to the map
path_playing_card = os.path.join("cartes", playing_card)

# instantiation of map and maze objects.

card_in_court = Map(playing_card)
labi = Labyrinthe(path_playing_card)
labi.position_items()

# Instructions:
instructions()

# Input user to move robot(to give cardinal point and number of cases.)

position = ''
while position != 'Q':
    # diplay map
    print(labi.export_map())
    card_in_court.save_map(labi.export_map())
    # instructions reminber
    simple_instruction()
    #  Test if robot in out
    if labi.winner() == 'Q':
        print("Congratulation !!!!")
        position = labi.winner()
        card_in_court.remove_save_game()
    else:
        # Selection move:
        position = position_selection()
        if position == 'Q':
            print("Good bye")
            #  save map
        elif labi.available_position(position) == 0:
            print("Your not ghost !!!")
        else:
            print(labi.export_map())

