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
        self.location = 'cave entrance'
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
                    "treasure room": False, "spider nest": False, "a3": False, "a4": False,
                    "b1": False, "cave entrance": False, "b3": False, "b4": False,
                    "c1": False, "c2": False, "c3": False, "c4": False,
                    "d1": False, "d2": False, "d3": False, "d4": False, }

zone_map = {"treasure room": {
                    DESCRIPTION: "You arrived in quickie builded wooden room.\n There's a heap in the corner of the room, covered whith some nasty rags.\n",
                    LOOK: "There's no more interesting thing except of the misterious heap...\n",
                    SOLVED: False,
                    DONE : "done",
                    UP: "",
                    DOWN: "alchemist's lab",
                    LEFT: "",
                    RIGHT: "spider nest"
                    },
            "spider nest": {
                    DESCRIPTION: "As you",
                    LOOK: "examine",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "",
                    DOWN: "cave entrance",
                    LEFT: "treasure room",
                    RIGHT: "hall of runes"
                    },
            "hall of runes": {
                    DESCRIPTION: "You entered a quite spacious room, where are misterious lights everywhere.\n",
                    LOOK: "As you look around in the room, you realize that the lights are luminous runes on the wall...\n",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "",
                    DOWN: "cavern swamp",
                    LEFT: "spider nest",
                    RIGHT: "salacite cavern"
                    },
            "salacite cavern": {
                    DESCRIPTION: "This place is like a tipical cavern.\n",
                    LOOK: "You see nothing special...\n Big salacites everywhere...\n But you suddenly realize that something was written on one.\n",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "",
                    DOWN: "grave",
                    LEFT: "hall of runes",
                    RIGHT: ""
                    },
            "alchemist's lab": {
                    DESCRIPTION: "You arrive to a strange place.. It seems like a chemisty lab...\n",
                    LOOK: "You see a table full with strage bottles and equipments on it.\n",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "treasure room",
                    DOWN: "lost man's hide",
                    LEFT: "",
                    RIGHT: "cave entrance"
                    },
            "cave entrance": {
                    DESCRIPTION: "You find yourself in a dark cave.\nThe only source of light is a 'torch' on the wall next to you.\nMaybe should 'examine' it.\n",
                    LOOK: "You see 'rock' in the corner with a carved opening.\nIt looks suspicious.\nThere are also four openings to the north, south, east and west.\n",
                    SOLVED: False,
                    DONE: "You have already collected everything in this cave.\nYou can go ahead to north, south, west, east.\n",
                    ITEMS: "rocktorch",
                    UP: "spider nest",
                    DOWN: "room of altar",
                    LEFT: "alchemist's lab",
                    RIGHT: "cavern swamp"
                    },
            "cavern swamp": {
                    DESCRIPTION: "As you enter this place, suddenly a disgusting smell hit your nose...\n It's like a marsh...\n",
                    LOOK: "As you look around, you see that there's a small pound full of chrystal clear water in the marsh...\n Really strange...\n",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "hall of runes",
                    DOWN: "mirrors cavern",
                    LEFT: "cave entrance",
                    RIGHT: "grave"
                    },
            "grave": {
                    DESCRIPTION: "You enter a dark cavern...\n Suddenly something crashing under your foot...\n",
                    LOOK: "You see that bones and corpses everywhere in this place.\n One of them looks really strange...\n",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "salacite cavern",
                    DOWN: "gobling's cavern",
                    LEFT: "cavern swamp",
                    RIGHT: ""
                    },
            "lost man's hide": {
                    DESCRIPTION: "You find yourself is a drak cavern whitch like a catacomb...",
                    LOOK: "You see a human shape in the back of the cavern...\n As you step closer you see a matted, thin man who seems totally lost...\n",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "alchemist lab",
                    DOWN: "christall cavern",
                    LEFT: "",
                    RIGHT: "room of altar"
                    },
            "room of altar": {
                    DESCRIPTION: "This place looks like permise of a temple from an ancient time.\n",
                    LOOK: "You realize that a small altar is in the middle of this place.\n",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "cave entrance",
                    DOWN: "haunted cavern",
                    LEFT: "lost man's hide",
                    RIGHT: "mirrors cavern"
                    },
            "mirrors cavern": {
                    DESCRIPTION: "As you enter this place, you see yourself on the walls...\n You feel confused...\n",
                    LOOK: "It looks like all the walls are made from mirror...\n You don't even know where are you going...\n",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "b3",
                    DOWN: "d3",
                    LEFT: "c2",
                    RIGHT: "c4"
                    },
            "goblin's cavern": {
                    DESCRIPTION: "You entered a place where small used stuff everywhere... and bones too...smoething smells bad...\n",
                    LOOK: "You see a small person in strange cloths.\n He seems angry because you entered his territory...\n",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "grave",
                    DOWN: "smuggler's hide",
                    LEFT: "mirrors cavern",
                    RIGHT: ""
                    },
            "christall cavern": {
                    DESCRIPTION: "This place is really strange. Colourful chrystalls everywhere..\n And stuffs... which looks like the equipment for some dark ritual...\n",
                    LOOK: "You see a pretty woman who seems really attractive, but you feel that not everything is fine with her...\n",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "lost man's hide",
                    DOWN: "",
                    LEFT: "",
                    RIGHT: "haunted cavern"
                    },
            "haunted cavern": {
                    DESCRIPTION: "You entered a place which looks like a normal part of a cave...\n",
                    LOOK: "You see a shape of a person... But as you get closer his body looks transparent...\n It's a ghost!\n ",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "room of altar",
                    DOWN: "",
                    LEFT: "christall cavern",
                    RIGHT: "hide-out"
                    },
            "hide-out": {
                    DESCRIPTION: "You step into place which look like a room formed to hide...\n A human's stuff everywhere...\n",
                    LOOK: "examine",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "mirrors cavern",
                    DOWN: "",
                    LEFT: "haunted cavern",
                    RIGHT: "smuggler's hide"
                    },
            "smuggler's hide": {
                    DESCRIPTION: "This dark place looks like a storage... Every kind of stuff inside.\n",
                    LOOK: "You see a thin man inside packing up the stuffs\n",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "goblin's cavern",
                    DOWN: "",
                    LEFT: "hide-out",
                    RIGHT: ""
                    }}



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
    zone = [""]
    print(" –––––––––––––––––––")
    print("| a1 | a2 | a3 | a4 |")
    print("|–––––––––––––––––––|")
    print("| b1 | b2 | b3 | b4 |")
    print("|–––––––––––––––––––|")
    print("| c1 | c2 | c3 | c4 |")
    print("|–––––––––––––––––––|")
    print("| d1 | d2 | d3 | d4 |")
    print(" –––––––––––––––––––")


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

    speech1 = 'You have finally finished your training in the ' + player_job + ' clan\n'
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
        time.sleep(0.01)

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
