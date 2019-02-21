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
        self.backpack = {}
        self.location = 'Cave entrance'
        self.game_over = False


myPlayer = player()


def first_screen_options():
    option = input("-> ")
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("help"):
        help_screen()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower not in ['play', 'help', 'quit']:
        print("Don't try to cheat! Enter a valid command!")
        option = input("-> ")
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
    print("")
    print("You can always try these commands: 'examine', 'look', 'move', 'status', 'help'")
    print("You can 'move' to 'up or north', 'down or south', 'left or west', 'right or east'")
    print("Enter 'quit' to give up...")


DESCRIPTION = "description"
LOOK = "examine"
SOLVED = False
DONE = "done"
UP = "up", "north"
DOWN = "down", "south"
LEFT = "left", "west"
RIGHT = "right", "east"
ITEMS = "items"


solved_places = {
                    "Treasure room": False, "Spider nest": False, "Hall of runes": False, "Salacite cavern": False,
                    "Alchemist's lab": False, "Cave entrance": False, "Cavern swamp": False, "Grave": False,
                    "Lost man's hide": False, "Room of altar": False, "Mirrors cavern": False, "Goblin's cavern": False,
                    "Christall cavern": False, "Haunted cavern": False, "Hide-out": False, "Smuggler's hide": False, }

visited_places = {
                    "Treasure room": False, "Spider nest": False, "Hall of runes": False, "Salacite cavern": False,
                    "Alchemist's lab": False, "Cave entrance": True, "Cavern swamp": False, "Grave": False,
                    "Lost man's hide": False, "Room of altar": False, "Mirrors cavern": False, "Goblin's cavern": False,
                    "Christall cavern": False, "Haunted cavern": False, "Hide-out": False, "Smuggler's hide": False, }


zone_map = {"Treasure room": {
                    DESCRIPTION: "description",
                    LOOK: "examine",
                    SOLVED: False,
                    DONE : "done",
                    UP: "",
                    DOWN: "Alchemist's lab",
                    LEFT: "",
                    RIGHT: "Spider nest"
                    },
            "Spider nest": {
                    DESCRIPTION: "description",
                    LOOK: "examine",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "",
                    DOWN: "Cave entrance",
                    LEFT: "Treasure room",
                    RIGHT: "Hall of runes"
                    },
            "Hall of runes": {
                    DESCRIPTION: "description",
                    LOOK: "examine",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "",
                    DOWN: "Cavern swamp",
                    LEFT: "Spider nest",
                    RIGHT: "Salacite cavern"
                    },
            "Salacite cavern": {
                    DESCRIPTION: "description",
                    LOOK: "examine",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "",
                    DOWN: "Grave",
                    LEFT: "Hall of runes",
                    RIGHT: ""
                    },
            "Alchemist's lab": {
                    DESCRIPTION: "description",
                    LOOK: "examine",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "Treasure room",
                    DOWN: "Lost man's hide",
                    LEFT: "",
                    RIGHT: "Cave entrance"
                    },
            "Cave entrance": {
                    DESCRIPTION: "You find yourself in a dark cave.\nThe only source of light is a 'torch' on the wall next to you.\nMaybe should 'examine' it.\n",
                    LOOK: "You see 'rock' in the corner with a carved opening.\nIt looks suspicious.\nThere are also four openings to the north, south, east and west.\n",
                    SOLVED: False,
                    DONE: "You have already collected everything in this cave.\nYou can go ahead to north, south, west, east.\n",
                    ITEMS: "rocktorch",
                    UP: "Spider nest",
                    DOWN: "Room of altar",
                    LEFT: "Alchemist's lab",
                    RIGHT: "Cavern swamp"
                    },
            "Cavern swamp": {
                    DESCRIPTION: "description",
                    LOOK: "examine",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "Hall of runes",
                    DOWN: "Mirrors cavern",
                    LEFT: "Cave entrance",
                    RIGHT: "Grave"
                    },
            "Grave": {
                    DESCRIPTION: "description",
                    LOOK: "examine",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "Salacite cavern",
                    DOWN: "gobling's cavern",
                    LEFT: "Cavern swamp",
                    RIGHT: ""
                    },
            "Lost man's hide": {
                    DESCRIPTION: "description",
                    LOOK: "examine",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "alchemist lab",
                    DOWN: "Christall cavern",
                    LEFT: "",
                    RIGHT: "Room of altar"
                    },
            "Room of altar": {
                    DESCRIPTION: "description",
                    LOOK: "examine",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "Cave entrance",
                    DOWN: "Haunted cavern",
                    LEFT: "Lost man's hide",
                    RIGHT: "Mirrors cavern"
                    },
            "Mirrors cavern": {
                    DESCRIPTION: "description",
                    LOOK: "examine",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "b3",
                    DOWN: "d3",
                    LEFT: "c2",
                    RIGHT: "c4"
                    },
            "Goblin's cavern": {
                    DESCRIPTION: "description",
                    LOOK: "examine",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "Grave",
                    DOWN: "Smuggler's hide",
                    LEFT: "Mirrors cavern",
                    RIGHT: ""
                    },
            "Christall cavern": {
                    DESCRIPTION: "description",
                    LOOK: "examine",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "Lost man's hide",
                    DOWN: "",
                    LEFT: "",
                    RIGHT: "Haunted cavern"
                    },
            "Haunted cavern": {
                    DESCRIPTION: "description",
                    LOOK: "examine",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "Room of altar",
                    DOWN: "",
                    LEFT: "Christall cavern",
                    RIGHT: "Hide-out"
                    },
            "Hide-out": {
                    DESCRIPTION: "description",
                    LOOK: "examine",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "Mirrors cavern",
                    DOWN: "",
                    LEFT: "Haunted cavern",
                    RIGHT: "Smuggler's hide"
                    },
            "Smuggler's hide": {
                    DESCRIPTION: "description",
                    LOOK: "examine",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "Goblin's cavern",
                    DOWN: "",
                    LEFT: "Hide-out",
                    RIGHT: ""
                    }}

zone = []
for key, value in zone_map.items():
    zone.append(key)



def print_location():
    if solved_places[myPlayer.location] == False: 
        print("# " + myPlayer.location.upper() + " #\n")
        for character in zone_map[myPlayer.location][DESCRIPTION]:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
    else:
        print("# " + myPlayer.location.upper() + " #\n")
        for character in zone_map[myPlayer.location][DONE]:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
        prompt()


def prompt():
    print("\n" + "==========================")
    print("What would you like to do?")
    action = input("-> ")
    acceptable_actions = ["move", "go", "travel" "walk", "quit", "run", "examine", "inspect", "interact", "look", "attack", "magic attack" "use", "equip", "open", "status", "help"]
    while action.lower() not in acceptable_actions:
        print("Unknown action, try again.\n")
        action = input("-> ")
    if action.lower() == "quit":
        sys.exit()
    elif action.lower() in ["move", "go", "travel" "walk", "run"]:
        player_move(action.lower())
    elif action.lower() in ["examine", "inspect", "interact"]:
        player_examine(action.lower())
    elif action.lower() in ["look"]:
        player_look(action.lower())
    elif action.lower() in ["status"]:
        status()
        zones()
    elif action.lower() in ["help"]:
        help_screen()


def status():
    print("")
    print("Your name is: " + myPlayer.name)
    print("Your class is: " + myPlayer.job)
    print("Your hp is: " + str(myPlayer.hp))
    print("Your mp is: " + str(myPlayer.mp))
    print("Your attack is: " + str(myPlayer.attack))
    print("Your maggic attack is: " + str(myPlayer.magic_attack))
    print("Your defense is: " + str(myPlayer.defense))
    print("Your armor is: " + str(myPlayer.armor))
    print("Your luck is: " + str(myPlayer.luck))


def zones():

    """Treasure room": False, "Spider nest": False, "Hall of runes": False, "Salacite cavern": False,
    "Alchemist's lab": False, "Cave entrance": False, "Cavern swamp": False, "Grave": False,
    "Lost man's hide": False, "Room of altar": False, "Mirrors cavern": False, "Goblin's cavern": False,
    "Christall cavern": False, "Haunted cavern": False, "Hide-out": False, "Smuggler's hide": False"""

    if visited_places["Treasure room"] == True:
        if myPlayer.location == "Threasure room":
            a1 = "You are here"
        else:
            a1 = "Threasure room"
    else:
        a1 = 18 * " "
    if visited_places["Spider nest"] == True:
        if myPlayer.location == "Spider nest":
            a2 = int((20 - len("You are here")) / 2 - 1) * " " + "You are here" + int((20 - len("You are here")) / 2 - 1) * " "
        else:
            a2 = "Spider nest"
    else:
        a2 = 18 * " "
    if visited_places["Hall of runes"] == True:
        if myPlayer.location == "Hall of runes":
            a3 = int((20 - len("You are here")) / 2 - 1) * " " + "You are here" + int((20 - len("You are here")) / 2 - 1) * " "
        else:
            a3 = "Hall of runes"
    else:
        a3 = 18 * " "
    if visited_places["Salacite cavern"] == True:
        if myPlayer.location == "Salacite cavern":
            a4 = int((20 - len("You are here")) / 2 - 1) * " " + "You are here" + int((20 - len("You are here")) / 2 - 1) * " "
        else:
            a4 = "Salacite cavern"
    else:
        a4 = 18 * " "
    if visited_places["Alchemist's lab"] == True:
        if myPlayer.location == "Alchemist's lab":
            b1 = int((20 - len("You are here")) / 2 - 1) * " " + "You are here" + int((20 - len("You are here")) / 2 - 1) * " "
        else:
            b1 = "Alchemist's lab"
    else:
        b1 = 18 * " "
    if visited_places["Cave entrance"] == True:
        if myPlayer.location == "Cave entrance":
            b2 = int((20 - len("You are here")) / 2 - 1) * " " + "You are here" + int((20 - len("You are here")) / 2 - 1) * " "
        else:
            b2 = "Cave entrance"
    else:
        b2 = 18 * " "
    if visited_places["Cavern swamp"] == True:
        if myPlayer.location == "Cavern swamp":
            b3 = int((20 - len("You are here")) / 2 - 1) * " " + "You are here" + int((20 - len("You are here")) / 2 - 1) * " "
        else:
            b3 = "Cavern swamp"
    else:
        b3 = 18 * " "
    if visited_places["Grave"] == True:
        if myPlayer.location == "Grave":
            b4 = int((20 - len("You are here")) / 2 - 1) * " " + "You are here" + int((20 - len("You are here")) / 2 - 1) * " "
        else:
            b4 = "Grave"
    else:
        b4 = 18 * " "
    if visited_places["Lost man's hide"] == True:
        if myPlayer.location == "Lost man's hide":
            c1 = int((20 - len("You are here")) / 2 - 1) * " " + "You are here" + int((20 - len("You are here")) / 2 - 1) * " "
        else:
            c1 = "Lost man's hide"
    else:
        c1 = 18 * " "
    if visited_places["Room of altar"] == True:
        if myPlayer.location == "Room of altar":
            c2 = int((20 - len("You are here")) / 2 - 1) * " " + "You are here" + int((20 - len("You are here")) / 2 - 1) * " "
        else:
            c2 = "Room of altar"
    else:
        c2 = 18 * " "
    if visited_places["Mirrors cavern"] == True:
        if myPlayer.location == "Mirrors cavern":
            c3 = int((20 - len("You are here")) / 2 - 1) * " " + "You are here" + int((20 - len("You are here")) / 2 - 1) * " "
        else:
            c3 = "Mirrors cavern"
    else:
        c3 = 18 * " "
    if visited_places["Goblin's cavern"] == True:
        if myPlayer.location == "Goblin's cavern":
            c4 = int((20 - len("You are here")) / 2 - 1) * " " + "You are here" + int((20 - len("You are here")) / 2 - 1) * " "
        else:
            c4 = "Goblin's cavern"
    else:
        c4 = 18 * " "
    if visited_places["Christall cavern"] == True:
        if myPlayer.location == "Christall cavern":
            d1 = int((20 - len("You are here")) / 2 - 1) * " " + "You are here" + int((20 - len("You are here")) / 2 - 1) * " "
        else:
            d1 = "Christall cavern"
    else:
        d1 = 18 * " "
    if visited_places["Haunted cavern"] == True:
        if myPlayer.location == "Haunted cavern":
            d2 = int((20 - len("You are here")) / 2 - 1) * " " + "You are here" + int((20 - len("You are here")) / 2 - 1) * " "
        else:
            d2 = "Haunted cavern"
    else:
        d2 = 18 * " "
    if visited_places["Hide-out"] == True:
        if myPlayer.location == "Hide-out":
            d3 = int((20 - len("You are here")) / 2 - 1) * " " + "You are here" + int((20 - len("You are here")) / 2 - 1) * " "
        else:
            d3 = "Hide-out"
    else:
        d3 = 18 * " "
    if visited_places["Smuggler's hide"] == True:
        if myPlayer.location == "Smuggler's hide":
            d4 = (20 - len("You are here") / 2) * " " + "You are here" + (20 - len("You are here") / 2) * " "
        else:
            d4 = "Smuggler's hide"
    else:
        d4 = 18 * " "
    
    len_of_map = 4 * 20 + 3

    print(" " + len_of_map * "–")
    print("| " + len_of_map * " ")
    print("| "+a1+" | "+a2+" | "+a3+" | "+a4+" |")
    print("| " + len_of_map * " ")
    print("| " + len_of_map * "–")
    print("| " + len_of_map * " ")
    print("| "+b1+" | "+b2+" | "+b3+" | "+b4+" |")
    print("| " + len_of_map * " ")
    print("| " + len_of_map * "–")
    print("| " + len_of_map * " ")
    print("| "+c1+" | "+c2+" | "+c3+" | "+c4+" |")
    print("| " + len_of_map * " ")
    print("| " + len_of_map * "–")
    print("| " + len_of_map * " ")
    print("| "+d1+" | "+d2+" | "+d3+" | "+d4+" |")
    print("| " + len_of_map * " ")
    print("| " + len_of_map * "–")
    print(" " + len_of_map * " ")


def player_look(action):
    if solved_places[myPlayer.location] == True:
        for character in zone_map[myPlayer.location][DONE]:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
    else:
        for character in zone_map[myPlayer.location][LOOK]:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
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
    os.system('clear')
    myPlayer.location = destination
    visited_places[myPlayer.location] = True
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
        if len(item_list[0]) == 3:
            if item_list[0][2][:-1] not in myPlayer.backpack:
                myPlayer.backpack[item_list[0][2][:-1]] = 1
        elif len(item_list[0]) == 4:
            if item_list[0][2] not in myPlayer.backpack:
                myPlayer.backpack[item_list[0][2]] = int(item_list[0][3][:-1])
            else:
                myPlayer.backpack[item_list[0][2]] += int(item_list[0][3][:-1])
        print(myPlayer.backpack)
        for character in item_list[0][1]:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
        if zone_map[myPlayer.location][ITEMS] == "":
            solved_places[myPlayer.location] = True
            print("")
            print("You solved everything in this room. Go ahead!")
        prompt()
    else:
        print("There is no such thing here...")
        prompt()


def main_game_loop():
    while myPlayer.game_over is False:
        prompt()


def setup_game():
    os.system("clear")
    question1 = 'What is your name?\n'
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_name = input('-> ')
    myPlayer.name = player_name

    question2 = 'What role do you want to play?\n'
    question2added = ("You can play as warrior, priest or mage.\n")
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_job = input('-> ')
    valid_jobs = ['warrior', 'mage', 'priest']
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print('You are now a ' + player_job + '!\n')
    while player_job.lower() not in valid_jobs:
        print(player_job.title() + " is not a valid class!")
        player_job = input('-> ')
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print('You are now a ' + player_job + '!\n')
    if myPlayer.job in ['warrior']:
        myPlayer.hp = 140
        myPlayer.mp = 20
        myPlayer.attack = 10
        myPlayer.magic_attack = 1
        myPlayer.defense = 19
        myPlayer.armor = 0
    if myPlayer.job in ["mage"]:
        myPlayer.hp = 40
        myPlayer.mp = 120
        myPlayer.attack = 4
        myPlayer.magic_attack = 18
        myPlayer.defense = 8
        myPlayer.armor = 0
    if myPlayer.job in ['priest']:
        myPlayer.hp = 80
        myPlayer.mp = 80
        myPlayer.attack = 10
        myPlayer.magic_attack = 10
        myPlayer.defense = 10
        myPlayer.armor = 0

    question3 = 'Welcome, ' + player_name + " the " + player_job + ".\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)

    """speech1 = 'You have finally finished your training in the ' + player_job + ' clan\n'
    speech2 = 'The head of the ' + player_job + ' clan gives you, a special mission.\n'
    speech3 = 'He tells you that a member of the Clan has become a betrayer and he stole the Golden Idol of the Clan\n'
    speech4 = 'Your mission will be to find the traitor and bring back the Golden Idol! Your master tells you where to look for the traitor..\n'
    speech5 = 'But be prepaired! Anything can happen!\n'

    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in speech5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)"""

    time.sleep(1)
    os.system('clear')
    print_location()
    main_game_loop()


def roll_dice():
    player_dice = random.randint(1, 100)
    print('You rolled ' + player_dice)
    enemy_dice = random.randint(1, 100)
    print('Your enemy has rolled ' + enemy_dice)


second_screen()
first_screen_options()
