# Old School TXT RPG Game

import sys
import time
import textwrap
import random
import os 
import cmd

screen_width = 100

class player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = ''
myPlayer = player()

#class room:
#    def __init__(self, filename):
#        open file ...
#        read components ...
#
#        self.name = room_name_from_file
#        self.text = room_text_from_file
#        self.directions = [name_up, name_right, name_down, name_left]
#        self.actions = {talk: {msg: "The dragon attacks!", enemy_name: "Susu", enemy_hp: 10, fight: True, reward: "HP+3", end_game: False}}
#
#    def do_command(command):
#        if c=='\'
#
#    def display(self):
#        print(self.text)
#        input()
#        redirect

# first screen
def first_screen_options():
    option = input("->")
    if option.lower() == ("play"):
        second_screen()
    elif option.lower() == ("help"):
        help_screen()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower not in ['play', 'help', 'quit']:
        print("Don't try to cheat! Enter a valid command!")
        option = input("->")
        if option.lower() == ("play"):
            second_screen()
        elif option.lower() == ("help"):
            help_screen()
        elif option.lower() == ("quit"):
            sys.exit()


def second_screen():
    os.system('clear')
    print(' Welcome! ')
    print(' - Play - ')
    print(' - Help - ')
    print(' - Quit - ')
    first_screen_options()


def help_screen():
    print(' use the arrows to move ')
    print(' type your commands to do them')
    print(' use "look" command to inspect')
    print(' follow these and have fun!')
    first_screen_options()


def start_game():

    DESCRIPTION = "description"
    EXAMINATION = "examine"
    SOLVED = False
    UP = "up", "north"
    DOWN = "down", "south"
    LEFT = "left", "west"
    RIGHT = "right", "east"

    solved_places = {"a1": False, "a2": False, "a3": False, "a4": False, 
                    "b1": False, "b2": False, "b3": False, "b4": False, 
                    "c1": False, "c2": False, "c3": False, "c4": False, 
                    "d1": False, "d2": False, "d3": False, "d4": False, }

    zone_map = {"a1": {DESCRIPTION: "description",
                       EXAMINATION: "examine",
                       SOLVED: False,
                       UP: "",
                       DOWN: "b1",
                       LEFT: "",
                       RIGHT: "a2"},
                "a2": {DESCRIPTION: "description",
                       EXAMINATION: "examine",
                       SOLVED: False,
                       UP: "",
                       DOWN: "b2",
                       LEFT: "a1",
                       RIGHT: "a3"},
                "a3": {DESCRIPTION: "description",
                       EXAMINATION: "examine",
                       SOLVED: False,
                       UP: "",
                       DOWN: "b3",
                       LEFT: "a2",
                       RIGHT: "a4"},
                "a4": {DESCRIPTION: "description",
                       EXAMINATION: "examine",
                       SOLVED: False,
                       UP: "",
                       DOWN: "b4",
                       LEFT: "a3",
                       RIGHT: ""},
                "b1": {DESCRIPTION: "description",
                       EXAMINATION: "examine",
                       SOLVED: False,
                       UP: "a1",
                       DOWN: "c1",
                       LEFT: "",
                       RIGHT: "b2"},
                "b2": {DESCRIPTION: "description",
                       EXAMINATION: "examine",
                       SOLVED: False,
                       UP: "a2",
                       DOWN: "c2",
                       LEFT: "b1",
                       RIGHT: "b3"},
                "b3": {DESCRIPTION: "description",
                       EXAMINATION: "examine",
                       SOLVED: False,
                       UP: "a3",
                       DOWN: "c3",
                       LEFT: "b2",
                       RIGHT: "b4"},
                "b4": {DESCRIPTION: "description",
                       EXAMINATION: "examine",
                       SOLVED: False,
                       UP: "a4",
                       DOWN: "c4",
                       LEFT: "b3",
                       RIGHT: ""},
                "c1": {DESCRIPTION: "description",
                       EXAMINATION: "examine",
                       SOLVED: False,
                       UP: "b1",
                       DOWN: "d1",
                       LEFT: "",
                       RIGHT: "c2"},
                "c2": {DESCRIPTION: "description",
                       EXAMINATION: "examine",
                       SOLVED: False,
                       UP: "b2",
                       DOWN: "d2",
                       LEFT: "c1",
                       RIGHT: "c3"},
                "c3": {DESCRIPTION: "description",
                       EXAMINATION: "examine",
                       SOLVED: False,
                       UP: "b3",
                       DOWN: "d3",
                       LEFT: "c2",
                       RIGHT: "c4"},
                "c4": {DESCRIPTION: "description",
                       EXAMINATION: "examine",
                       SOLVED: False,
                       UP: "b4",
                       DOWN: "d4",
                       LEFT: "c3",
                       RIGHT: ""},
                "d1": {DESCRIPTION: "description",
                       EXAMINATION: "examine",
                       SOLVED: False,
                       UP: "c1",
                       DOWN: "",
                       LEFT: "",
                       RIGHT: "d2"},
                "d2": {DESCRIPTION: "description",
                       EXAMINATION: "examine",
                       SOLVED: False,
                       UP: "c2",
                       DOWN: "",
                       LEFT: "d1",
                       RIGHT: "d3"},
                "d3": {DESCRIPTION: "description",
                       EXAMINATION: "examine",
                       SOLVED: False,
                       UP: "c3",
                       DOWN: "",
                       LEFT: "d2",
                       RIGHT: "d4"},
                "d4": {DESCRIPTION: "description",
                       EXAMINATION: "examine",
                       SOLVED: False,
                       UP: "c4",
                       DOWN: "",
                       LEFT: "d3",
                       RIGHT: ""}}


second_screen()
help_screen()