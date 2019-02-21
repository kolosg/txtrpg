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
        self.attack = 0
        self.magic_attack = 0
        self.defense = 0
        self.armor = 0
        self.luck = 0
        self.backpack = []
        self.location = 'cave entrance'
        self.game_over = False


myPlayer = player()


def first_screen_options():
    option = input("->")
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("help"):
        help_screen()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower not in ['play', 'help', 'quit']:
        print("Don't try to cheat! Enter a valid command!")
        option = input("->")
        if option.lower() == ("play"):
            setup_game()
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


DESCRIPTION = "description"
LOOK = "examine"
SOLVED = False
UP = "up", "north"
DOWN = "down", "south"
LEFT = "left", "west"
RIGHT = "right", "east"
ITEMS = "items"


solved_places = {
                    "a1": False, "spider nest": False, "a3": False, "a4": False,
                    "b1": False, "cave entrance": False, "b3": False, "b4": False,
                    "c1": False, "c2": False, "c3": False, "c4": False,
                    "d1": False, "d2": False, "d3": False, "d4": False, }

zone_map = {"a1": {
                    DESCRIPTION: "description",
                    LOOK: "examine",
                    SOLVED: False,
                    UP: "",
                    DOWN: "b1",
                    LEFT: "",
                    RIGHT: "spider nest"
                    },
            "spider nest": {
                    DESCRIPTION: "description",
                    LOOK: "examine",
                    SOLVED: False,
                    UP: "",
                    DOWN: "cave entrance",
                    LEFT: "a1",
                    RIGHT: "a3"
                    },
            "a3": {
                    DESCRIPTION: "description",
                    LOOK: "examine",
                    SOLVED: False,
                    UP: "",
                    DOWN: "b3",
                    LEFT: "spider nest",
                    RIGHT: "a4"
                    },
            "a4": {
                    DESCRIPTION: "description",
                    LOOK: "examine",
                    SOLVED: False,
                    UP: "",
                    DOWN: "b4",
                    LEFT: "a3",
                    RIGHT: ""
                    },
            "b1": {
                    DESCRIPTION: "description",
                    LOOK: "examine",
                    SOLVED: False,
                    UP: "a1",
                    DOWN: "c1",
                    LEFT: "",
                    RIGHT: "cave entrance"
                    },
            "cave entrance": {
                    DESCRIPTION: "You find yourself in a dark cave.\nThe only source of light is a 'torch' on the wall next to you.\nMaybe should 'examine' it.\n",
                    LOOK: "You see 'rock' in the corner with a carved opening\nIt looks suspicious.\nThere are also four openings to the north, south, east and west.",
                    SOLVED: False,
                    ITEMS: "rocktorch",
                    UP: "spider nest",
                    DOWN: "c2",
                    LEFT: "b1",
                    RIGHT: "b3"
                    },
            "b3": {
                    DESCRIPTION: "description",
                    LOOK: "examine",
                    SOLVED: False,
                    UP: "a3",
                    DOWN: "c3",
                    LEFT: "cave entrance",
                    RIGHT: "b4"
                    },
            "b4": {
                    DESCRIPTION: "description",
                    LOOK: "examine",
                    SOLVED: False,
                    UP: "a4",
                    DOWN: "c4",
                    LEFT: "b3",
                    RIGHT: ""
                    },
            "c1": {
                    DESCRIPTION: "description",
                    LOOK: "examine",
                    SOLVED: False,
                    UP: "b1",
                    DOWN: "d1",
                    LEFT: "",
                    RIGHT: "c2"
                    },
            "c2": {
                    DESCRIPTION: "description",
                    LOOK: "examine",
                    SOLVED: False,
                    UP: "cave entrance",
                    DOWN: "d2",
                    LEFT: "c1",
                    RIGHT: "c3"
                    },
            "c3": {
                    DESCRIPTION: "description",
                    LOOK: "examine",
                    SOLVED: False,
                    UP: "b3",
                    DOWN: "d3",
                    LEFT: "c2",
                    RIGHT: "c4"
                    },
            "c4": {
                    DESCRIPTION: "description",
                    LOOK: "examine",
                    SOLVED: False,
                    UP: "b4",
                    DOWN: "d4",
                    LEFT: "c3",
                    RIGHT: ""
                    },
            "d1": {
                    DESCRIPTION: "description",
                    LOOK: "examine",
                    SOLVED: False,
                    UP: "c1",
                    DOWN: "",
                    LEFT: "",
                    RIGHT: "d2"
                    },
            "d2": {
                    DESCRIPTION: "description",
                    LOOK: "examine",
                    SOLVED: False,
                    UP: "c2",
                    DOWN: "",
                    LEFT: "d1",
                    RIGHT: "d3"
                    },
            "d3": {
                    DESCRIPTION: "description",
                    LOOK: "examine",
                    SOLVED: False,
                    UP: "c3",
                    DOWN: "",
                    LEFT: "d2",
                    RIGHT: "d4"
                    },
            "d4": {
                    DESCRIPTION: "description",
                    LOOK: "examine",
                    SOLVED: False,
                    UP: "c4",
                    DOWN: "",
                    LEFT: "d3",
                    RIGHT: ""
                    }}


def print_location():
    if zone_map[myPlayer.location][SOLVED] == False: 
        print("# " + myPlayer.location.upper() + " #\n")
        for character in zone_map[myPlayer.location][DESCRIPTION]:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
    else:
        print("You have already exhausted this zone.")
        prompt()



def prompt():
    print("\n" + "==========================")
    print("What would you like to do?")
    action = input("->")
    acceptable_actions = ["move", "go", "travel" "walk", "quit", "examine", "inspect", "interact", "look"]
    while action.lower() not in acceptable_actions:
        print("Unknown action, try again.\n")
        action = input("->")
    if action.lower() == "quit":
        sys.exit()
    elif action.lower() in ["move", "go", "travel" "walk"]:
        player_move(action.lower())
    elif action.lower() in ["examine", "inspect", "interact"]:
        player_examine(action.lower())
    elif action.lower() in ["look"]:
        player_look(action.lower())


def player_look(action):
    if zone_map[myPlayer.location][SOLVED] == True:
        print("You have already exhausted this zone.")
    elif zone_map[myPlayer.location][SOLVED] == False:
        for character in zone_map[myPlayer.location][LOOK]:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
    prompt()


def player_move(action):
    ask = "Where would you like to move to?\n"
    dest = input(ask)
    if dest in ["up", "north"]:
        destination = zone_map[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ["down", "south"]:
        destination = zone_map[myPlayer.location][DOWN]
        movement_handler(destination)
    elif dest in ["left", "west"]:
        destination = zone_map[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ["right", "east"]:
        destination = zone_map[myPlayer.location][RIGHT]
        movement_handler(destination)


def movement_handler(destination):
    print("\n" + "You have moved to the " + destination + ".")
    myPlayer.location = destination
    print_location()


def player_examine(action):
    examine_question = "What would you like to examine?\n"
    answer = input(examine_question)
    item_list = []
    if answer.lower() in zone_map[myPlayer.location][ITEMS]:
        with open("items.txt", "r") as item:
            for line in item:
                if answer in line:
                    item_list.append(line.split(','))
        zone_map[myPlayer.location][ITEMS] = zone_map[myPlayer.location][ITEMS].replace(answer, "")
        for character in item_list[0][1]:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        prompt()
    else:
        print("There is no such thing here...")
        prompt()
    if zone_map[myPlayer.location][ITEMS] == "":
        zone_map[myPlayer.location][SOLVED] = True
        print("You solved everything in this room. Go ahead!")


def main_game_loop():
    while myPlayer.game_over is False:
        prompt()


def setup_game():
    os.system("clear")
    question1 = 'What is your name?\n'
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input('->')
    myPlayer.name = player_name

    question2 = 'What role do you want to play?\n'
    question2added = ("You can play as warrior, priest or mage.\n")
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_job = input('->')
    valid_jobs = ['warrior', 'mage', 'priest']
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print('You are now a ' + player_job + '!\n')
    while player_job.lower() not in valid_jobs:
        print(player_job.title() + " is not a valid class!")
        player_job = input('->')
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print('You are now a ' + player_job + '!\n')
    if myPlayer.job is 'warrior':
        self.hp = 140
        self.mp = 20
        self.attack = 10
        self.magic_attack = 1
        self.defense = 19
        self.armor = 0
    if myPlayer.job is 'mage':
        self.hp = 40
        self.mp = 120
        self.attack = 4
        self.magic_attack = 18
        self.defense = 8
        self.armor = 0
    if myPlayer.job is 'priest':
        self.hp = 80
        self.mp = 80
        self.attack = 10
        self.magic_attack = 10
        self.defense = 10
        self.armor = 0

    question3 = 'Welcome, ' + player_name + " the " + player_job + ".\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    speech1 = 'Hello\n'
    speech2 = 'Welcome\n'
    speech3 = 'Hola\n'
    speech4 = 'Guten tag\n'

    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    os.system('clear')
    print('###############')
    print("# Let's Start #")
    print('###############')
    time.sleep(1)
    os.system('clear')
    print_location()
    main_game_loop()


second_screen()
first_screen_options()
