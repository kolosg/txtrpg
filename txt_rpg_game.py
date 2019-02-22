# Old School TXT RPG Game

import sys
import time
import random
import os
import classes

screen_width = 100

spider = classes.spider()
myPlayer = classes.player()
goblin = classes.goblin()
witch = classes.witch()
boss = classes.boss()


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
    print("You should try these commands: 'examine', 'look', 'move', 'status', 'help'")
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
                    "Treasure Room": False, "Spider's Nest": False, "Hall of Runes": False, "Stalactite Cavern": False,
                    "Alchemist's Lab": False, "Cave Entrance": False, "Cavern Swamp": False, "Graveyard": False,
                    "Lost Man's Hide": False, "Room of Altar": False, "Cavern of Mirrors": False, "Goblin's Hollow": False,
                    "Crystal Cavern": False, "Haunted Cavern": False, "Hide-out": False, "Smuggler's Hide": False, }


visited_places = {
                    "Treasure Room": False, "Spider's Nest": False, "Hall of Runes": False, "Stalactite Cavern": False,
                    "Alchemist's Lab": False, "Cave Entrance": False, "Cavern Swamp": False, "Graveyard": False,
                    "Lost Man's Hide": False, "Room of Altar": False, "Cavern of Mirrors": False, "Goblin's Hollow": False,
                    "Crystal Cavern": False, "Haunted Cavern": False, "Hide-out": False, "Smuggler's Hide": False, }


zone_map = {"Treasure Room": {
                    DESCRIPTION: "You have arrived in quickly builded wooden room.\nThere's a heap in the corner, covered whith some nasty rags.\n",
                    LOOK: "There's no more interesting things except for the mysterious heap...\n",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "heap",
                    UP: "",
                    DOWN: "Alchemist's Lab",
                    LEFT: "",
                    RIGHT: "Spider's Nest"
                    },
            "Spider's Nest": {
                    DESCRIPTION: "You enter an ominous cavern. You see huge spider webs all around you...\n",
                    LOOK: "Not far from you realize there is disgusting spider lurking in the shadows.\n",
                    SOLVED: False,
                    DONE : "You have already collected everything here.\nYou can go ahead to the south, west, east.\n",
                    ITEMS: "",
                    UP: "",
                    DOWN: "Cave Entrance",
                    LEFT: "Treasure Room",
                    RIGHT: "Hall of Runes"
                    },
            "Hall of Runes": {
                    DESCRIPTION: "You entered a quite spacious room, there are mysterious lights everywhere.\n",
                    LOOK: "As you look around in the room, you realize that the lights are luminous runes on the wall...\n",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "",
                    DOWN: "Cavern Swamp",
                    LEFT: "Spider's Nest",
                    RIGHT: "Stalactite Cavern"
                    },
            "Stalactite Cavern": {
                    DESCRIPTION: "This place is like a typical cavern.\n",
                    LOOK: "You see nothing special...\nBig salactites everywhere...\nBut you suddenly realize that something was written on one of them.\n",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "",
                    DOWN: "Graveyard",
                    LEFT: "Hall of Runes",
                    RIGHT: ""
                    },
            "Alchemist's Lab": {
                    DESCRIPTION: "You arrive to a strange place.. It seems like a chemistry lab...\n",
                    LOOK: "You see a table full of strange bottles and equipments.\n",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "Treasure Room",
                    DOWN: "Lost Man's Hide",
                    LEFT: "",
                    RIGHT: "Cave Entrance"
                    },
            "Cave Entrance": {
                    DESCRIPTION: "You find yourself in a dark cave.\nThe only source of light is a 'torch' on the wall next to you.\nMaybe should 'examine' it.\n",
                    LOOK: "You see 'rock' in the corner with a carved opening.\nIt looks suspicious.\nThere are also four openings to the north, south, east and west.\n",
                    SOLVED: False,
                    DONE: "You have already collected everything in this cave.\nYou can go ahead to north, south, west, east.\n",
                    ITEMS: "rocktorch",
                    UP: "Spider's Nest",
                    DOWN: "Room of Altar",
                    LEFT: "Alchemist's Lab",
                    RIGHT: "Cavern Swamp"
                    },
            "Cavern Swamp": {
                    DESCRIPTION: "As you enter this place, suddenly a disgusting smell hits your nose...\nIt's like a marsh...\n",
                    LOOK: "As you look around, you see that there's a small pound full of crystal clear water in the marsh...\nReally strange...\n",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "Hall of Runes",
                    DOWN: "Cavern of Mirrors",
                    LEFT: "Cave Entrance",
                    RIGHT: "Graveyard"
                    },
            "Graveyard": {
                    DESCRIPTION: "You enter a dark cavern...\nSuddenly something cracks under your foot...\n",
                    LOOK: "You see that bones and corpses are everywhere in this place.\nOne of them looks really strange...\n",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "Stalactite Cavern",
                    DOWN: "Goblin's Hollow",
                    LEFT: "Cavern Swamp",
                    RIGHT: ""
                    },
            "Lost Man's Hide": {
                    DESCRIPTION: "You find yourself is a dark cavern whitch is like a catacomb...",
                    LOOK: "You see a human shape in the back of the cavern...\nAs you step closer you see a matted, thin man who seems totally lost...\n",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "Alchemist's Lab",
                    DOWN: "Crystal Cavern",
                    LEFT: "",
                    RIGHT: "Room of Altar"
                    },
            "Room of Altar": {
                    DESCRIPTION: "This place looks like a premise of a temple from ancient times.\n",
                    LOOK: "You realize that a small altar is in the middle of this place.\n",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "altar",
                    UP: "Cave Entrance",
                    DOWN: "Haunted Cavern",
                    LEFT: "Lost Man's Hide",
                    RIGHT: "Cavern of Mirrors"
                    },
            "Cavern of Mirrors": {
                    DESCRIPTION:  "As you enter this place, you see yourself on the walls...\nYou feel confused...\n",
                    LOOK: "It looks like all the walls are made of mirror...\nYou don't even know where are you going...\n",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: random.choice(["Room of Altar", "Goblin's Hollow", "Hide-out"]),
                    DOWN: random.choice(["Room of Altar", "Goblin's Hollow", "Cavern Swamp"]),
                    LEFT: random.choice(["Cavern Swamp", "Goblin's Hollow", "Hide-out"]),
                    RIGHT: random.choice(["Room of Altar", "Cavern Swamp", "Hide-out"])
                    },
            "Goblin's Hollow": {
                    DESCRIPTION: "You entered a place where small, used stuff are everywhere... and bones too...something smells bad...\n",
                    LOOK: "You see a small person in strange clothes.\nHe seems angry because you entered his territory...\n",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "Graveyard",
                    DOWN: "Smuggler's Hide",
                    LEFT: "Cavern of Mirrors",
                    RIGHT: ""
                    },
            "Crystal Cavern": {
                    DESCRIPTION: "This place is really strange. Colourful crystals everywhere..\nAnd stuffs... which looks like the equipment for some dark ritual...\n",
                    LOOK: "You see a pretty woman who seems really attractive, but you feel that not everything is fine with her...\n",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "Lost Man's Hide",
                    DOWN: "",
                    LEFT: "",
                    RIGHT: "Haunted Cavern"
                    },
            "Haunted Cavern": {
                    DESCRIPTION: "You entered a place which looks like a normal part of a cave...\n",
                    LOOK: "You see a shape of a person... But as you get closer his body looks transparent...\nIt's a ghost!\n ",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "ghost",
                    UP: "Room of Altar",
                    DOWN: "",
                    LEFT: "Crystal Cavern",
                    RIGHT: "Hide-out"
                    },
            "Hide-out": {
                    DESCRIPTION: "You step into place which look like a room formed to hide...\nA human's stuff everywhere...\n",
                    LOOK: "examine",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "Cavern of Mirrors",
                    DOWN: "",
                    LEFT: "Haunted Cavern",
                    RIGHT: "Smuggler's Hide"
                    },
            "Smuggler's Hide": {
                    DESCRIPTION: "This dark place looks like a storage... Every kind of stuff inside.\n",
                    LOOK: "You see a thin man inside packing up the stuff\n",
                    SOLVED: False,
                    DONE : "done",
                    ITEMS: "",
                    UP: "Goblin's Hollow",
                    DOWN: "",
                    LEFT: "Hide-out",
                    RIGHT: ""
                    }}


def print_location():
    if solved_places[myPlayer.location] == False: 
        print("# " + myPlayer.location.upper() + " #\n")
        for character in zone_map[myPlayer.location][DESCRIPTION]:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
    else:
        print("# " + myPlayer.location.upper() + " #\n")
        for character in zone_map[myPlayer.location][DONE]:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        prompt()


def prompt():
    visited_places[myPlayer.location] = True
    print("\n" + "==========================")
    print("What would you like to do?")
    action = input("-> ")
    acceptable_actions = ["move", "go", "travel" "walk", "quit", "run", "flee", "examine", "inspect", "interact", "look", "attack", "magic attack", "talk", "status", "help"]
    while action.lower() not in acceptable_actions:
        print("Unknown action, try again.\n")
        action = input("-> ")
    if action.lower() == "quit":
        sys.exit()
    elif action.lower() in ["move", "go", "travel" "walk"]:
        if "torch" not in myPlayer.backpack:
            print("\nYou cannot move because you see nothing. Find a torch!")
        else:
            player_move(action.lower())
    elif action.lower() in ["examine", "inspect", "interact"]:
        player_examine(action.lower())
    elif action.lower() in ["look"]:
        player_look(action.lower())
    elif action.lower() in ["attack"]:
        player_attack(action.lower())
    elif action.lower() in ["status"]:
        status()
        if "map" in myPlayer.backpack:
            zones()
        else:
            print("Your map: Your map is LOCKED now. You have to find a map to unlock it and see where are you")
    elif action.lower() in ["talk"]:
        talk(action.lower())
    elif action.lower() in ["run", "flee"]:
        player_flee(action.lower())
    elif action.lower() in ["help"]:
        help_screen()


def flee(action):
    pass


def talk(action):
    pass


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
    print("Yor backpack contains: " + str(myPlayer.backpack))

def zones():

    if visited_places["Treasure Room"] == True:
        if myPlayer.location == "Treasure Room":
            a1 = int((20 - len("You are here")) / 2 - 1) * " " + "You are here" + int((20 - len("You are here")) / 2 - 1) * " "
        else:
            a1 = int((16 - len("Treasure Room")) / 2 + 1) * " " + "Treasure Room" + int((16 - len("Treasure Room")) / 2 + 2) * " "
    else:
        a1 = 18 * " "
    if visited_places["Spider's Nest"] == True:
        if myPlayer.location == "Spider's Nest":
            a2 = int((20 - len("You are here")) / 2 - 1) * " " + "You are here" + int((20 - len("You are here")) / 2 - 1) * " "
        else:
            a2 = int((20 - len("Spider's Nest")) / 2) * " "  + "Spider's Nest" + int((20 - len("Spider's Nest")) / 2 - 1) * " "
    else:
        a2 = 18 * " "
    if visited_places["Hall of Runes"] == True:
        if myPlayer.location == "Hall of Runes":
            a3 = int((20 - len("You are here")) / 2 - 1) * " " + "You are here" + int((20 - len("You are here")) / 2 - 1) * " "
        else:
            a3 = int((20 - len("Hall of Runes")) / 2) * " " + "Hall of Runes" + int((20 - len("Hall of Runes")) / 2 - 1) * " "
    else:
        a3 = 18 * " "
    if visited_places["Stalactite Cavern"] == True:
        if myPlayer.location == "Stalactite Cavern":
            a4 = int((20 - len("You are here")) / 2 - 1) * " " + "You are here" + int((20 - len("You are here")) / 2 - 1) * " "
        else:
            a4 = int((20 - len("Stalactite Cavern")) / 2) * " " + "Stalactite Cavern" + int((20 - len("Stalactite Cavern")) / 2 - 1) * " "
    else:
        a4 = 18 * " "
    if visited_places["Alchemist's Lab"] == True:
        if myPlayer.location == "Alchemist's Lab":
            b1 = int((20 - len("You are here")) / 2 - 1) * " " + "You are here" + int((20 - len("You are here")) / 2 - 1) * " "
        else:
            b1 = int((20 - len("Alchemist's Lab")) / 2) * " " + "Alchemist's Lab" + int((20 - len("Alchemist's Lab")) / 2 - 1) * " "
    else:
        b1 = 18 * " "
    if visited_places["Cave Entrance"] == True:
        if myPlayer.location == "Cave Entrance":
            b2 = int((20 - len("You are here")) / 2 - 1) * " " + "You are here" + int((20 - len("You are here")) / 2 - 1) * " "
        else:
            b2 = int((20 - len("Cave Entrance")) / 2) * " " + "Cave Entrance" + int((20 - len("Cave Entrance")) / 2 - 1) * " "
    else:
        b2 = 18 * " "
    if visited_places["Cavern Swamp"] == True:
        if myPlayer.location == "Cavern Swamp":
            b3 = int((20 - len("You are here")) / 2 - 1) * " " + "You are here" + int((20 - len("You are here")) / 2 - 1) * " "
        else:
            b3 = int((20 - len("Cavern Swamp")) / 2 - 1) * " " + "Cavern Swamp" + int((20 - len("Cavern Swamp")) / 2 - 1) * " "
    else:
        b3 = 18 * " "
    if visited_places["Graveyard"] == True:
        if myPlayer.location == "Graveyard":
            b4 = int((20 - len("You are here")) / 2 - 1) * " " + "You are here" + int((20 - len("You are here")) / 2 - 1) * " "
        else:
            b4 = int((20 - len("Graveyard")) / 2) * " " + "Graveyard" + int((20 - len("Graveyard")) / 2 - 1) * " "
    else:
        b4 = 18 * " "
    if visited_places["Lost Man's Hide"] == True:
        if myPlayer.location == "Lost Man's Hide":
            c1 = int((20 - len("You are here")) / 2 - 1) * " " + "You are here" + int((20 - len("You are here")) / 2 - 1) * " "
        else:
            c1 = int((20 - len("Lost Man's Hide")) / 2) * " " + "Lost Man's Hide" + int((20 - len("Lost Man's Hide")) / 2 - 1) * " "
    else:
        c1 = 18 * " "
    if visited_places["Room of Altar"] == True:
        if myPlayer.location == "Room of Altar":
            c2 = int((20 - len("You are here")) / 2 - 1) * " " + "You are here" + int((20 - len("You are here")) / 2 - 1) * " "
        else:
            c2 = int((20 - len("Room of Altar")) / 2) * " " + "Room of Altar" + int((20 - len("Room of Altar")) / 2 - 1) * " "
    else:
        c2 = 18 * " "
    if visited_places["Cavern of Mirrors"] == True:
        if myPlayer.location == "Cavern of Mirrors":
            c3 = int((20 - len("You are here")) / 2 - 1) * " " + "You are here" + int((20 - len("You are here")) / 2 - 1) * " "
        else:
            c3 = int((20 - len("Cavern of Mirrors")) / 2 - 1) * " " + "Cavern of Mirrors" + int((20 - len("Cavern of Mirrors")) / 2) * " "
    else:
        c3 = 18 * " "
    if visited_places["Goblin's Hollow"] == True:
        if myPlayer.location == "Goblin's Hollow":
            c4 = int((20 - len("You are here")) / 2 - 1) * " " + "You are here" + int((20 - len("You are here")) / 2 - 1) * " "
        else:
            c4 = int((20 - len("Goblin's Hollow")) / 2 - 1) * " " + "Goblin's Hollow" + int((20 - len("Goblin's Hollow")) / 2) * " "
    else:
        c4 = 18 * " "
    if visited_places["Crystal Cavern"] == True: 
        if myPlayer.location == "Crystal Cavern":
            d1 = int((20 - len("You are here")) / 2 - 1) * " " + "You are here" + int((20 - len("You are here")) / 2 - 1) * " "
        else:
            d1 = int((20 - len("Crystal Cavern")) / 2 - 1) * " " + "Crystal Cavern" + int((20 - len("Crystal Cavern")) / 2 - 1) * " "
    else:
        d1 = 18 * " "
    if visited_places["Haunted Cavern"] == True:
        if myPlayer.location == "Haunted Cavern":
            d2 = int((20 - len("You are here")) / 2 - 1) * " " + "You are here" + int((20 - len("You are here")) / 2 - 1) * " "
        else:
            d2 = int((20 - len("Haunted Cavern")) / 2 - 1) * " " + "Haunted Cavern" + int((20 - len("Haunted Cavern")) / 2 - 1) * " "
    else:
        d2 = 18 * " "
    if visited_places["Hide-out"] == True:
        if myPlayer.location == "Hide-out":
            d3 = int((20 - len("You are here")) / 2 - 1) * " " + "You are here" + int((20 - len("You are here")) / 2 - 1) * " "
        else:
            d3 = int((20 - len("Hide-out")) / 2 - 1) * " " + "Hide-out" + int((20 - len("Hide-out")) / 2 - 1) * " "
    else:
        d3 = 18 * " "
    if visited_places["Smuggler's Hide"] == True:
        if myPlayer.location == "Smuggler's Hide":
            d4 = int((20 - len("You are here")) / 2 - 1) * " " + "You are here" + int((20 - len("You are here")) / 2 - 1) * " "
        else:
            d4 = int((20 - len("Smuggler's Hide")) / 2 -1) * " " + "Smuggler's Hide" + int((20 - len("Smuggler's Hide")) / 2) * " "
    else:
        d4 = 18 * " "
    print("Your map is UNLOCKED: ")
    len_of_map = 4 * 20 + 2
    print("")
    print(" " + len_of_map * "–"+"–")
    print("| " + len_of_map * " " + "|")
    print("| "+a1+" | "+a2+" | "+a3+" | "+a4+" |")
    print("| " + len_of_map * " " + "|")
    print("| " + len_of_map * "–" + "|")
    print("| " + len_of_map * " " + "|")
    print("| "+b1+" | "+b2+" | "+b3+" | "+b4+" |")
    print("| " + len_of_map * " " + "|")
    print("| " + len_of_map * "–" + "|")
    print("| " + len_of_map * " " + "|")
    print("| "+c1+" | "+c2+" | "+c3+" | "+c4+" |")
    print("| " + len_of_map * " " + "|")
    print("| " + len_of_map * "–" + "|")
    print("| " + len_of_map * " " + "|")
    print("| "+d1+" | "+d2+" | "+d3+" | "+d4+" |")
    print("| " + len_of_map * " " + "|")
    print(" " + len_of_map * "–"+"–")
    print("")


def player_look(action):
    if solved_places[myPlayer.location] == True:
        for character in zone_map[myPlayer.location][DONE]:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
    else:
        for character in zone_map[myPlayer.location][LOOK]:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
    prompt()


def player_move(action):
    ask = "Where would you like to move to?\n"
    dest = input(ask)
    if dest in ["up", "north"]:
        if zone_map[myPlayer.location][UP] != "":
            destination = zone_map[myPlayer.location][UP]
            movement_handler(destination)
        else:
            print("You don't want to hit the wall")
    elif dest in ["down", "south"]:
        if zone_map[myPlayer.location][DOWN] != "":
            destination = zone_map[myPlayer.location][DOWN]
            movement_handler(destination)
        else:
            print("You don't want to hit the wall")
    elif dest in ["left", "west"]:
        if zone_map[myPlayer.location][LEFT] != "":
            destination = zone_map[myPlayer.location][LEFT]
            movement_handler(destination)
        else:
            print("You don't want to hit the wall")
    elif dest in ["right", "east"]:
        if zone_map[myPlayer.location][RIGHT] != "":
            destination = zone_map[myPlayer.location][RIGHT]
            movement_handler(destination)
        else:
            print("You don't want to hit the wall")


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
                line = line.split(',')
                if answer == line[0]:
                    item_list.append(line)
        zone_map[myPlayer.location][ITEMS] = zone_map[myPlayer.location][ITEMS].replace(answer, "")
        if len(item_list[0]) == 3:
            if item_list[0][2][:-1] not in myPlayer.backpack:
                myPlayer.backpack[item_list[0][2][:-1]] = 1
        elif len(item_list[0]) == 4:
            if item_list[0][2] not in myPlayer.backpack:
                try:
                    myPlayer.backpack[item_list[0][2]] = int(item_list[0][3][:-1])
                except:
                    myPlayer.backpack[item_list[0][2]] = item_list[0][3][:-1]
            else:
                try:
                    myPlayer.backpack[item_list[0][2]] += int(item_list[0][3][:-1])
                except:
                    myPlayer.backpack[item_list[0][2]] += item_list[0][3][:-1]
        for character in item_list[0][1]:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        if zone_map[myPlayer.location][ITEMS] == "":
            solved_places[myPlayer.location] = True
            print("")
            print("\nYou solved everything in this room. Go ahead!")
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
        time.sleep(0.05)
    player_name = input('-> ')
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
        time.sleep(0.05)
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
        myPlayer.hp = 340
        myPlayer.mp = 20
        myPlayer.attack = 25
        myPlayer.original_attack = 10
        myPlayer.magic_attack = 1
        myPlayer.defense = 19
        myPlayer.original_defense = 19
        myPlayer.armor = 0
    if myPlayer.job in ["mage"]:
        myPlayer.hp = 240
        myPlayer.mp = 120
        myPlayer.attack = 4
        myPlayer.magic_attack = 33
        myPlayer.defense = 8
        myPlayer.armor = 0
    if myPlayer.job in ['priest']:
        myPlayer.hp = 280
        myPlayer.mp = 80
        myPlayer.attack = 20
        myPlayer.magic_attack = 10
        myPlayer.defense = 10
        myPlayer.armor = 0

    question3 = 'Welcome, ' + player_name + " the " + player_job + ".\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    speech1 = 'You have finally finished your training in the ' + player_job + ' clan\n'
    speech2 = 'The head of the ' + player_job + ' clan gives you, a special mission.\n'
    speech3 = 'He tells you that a member of the Clan has become a betrayer and he stole the Golden Idol of the Clan\n'
    speech4 = 'Your mission will be to find the traitor and bring back the Golden Idol! Your master tells you where to look for the traitor..\n'
    speech5 = 'But be prepaired! Anything can happen!\n'

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
    for character in speech5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    time.sleep(1)
    os.system('clear')
    print_location()
    main_game_loop()


def player_attack(action):
    if myPlayer.location == "Spider's Nest":
        if myPlayer.hp > 0 and spider.hp > 0:
            print("")
            print("Attack phase: \n")
            player_dice = random.randint(1, 100)
            print('You rolled ' + str(player_dice))
            opponent_dice = random.randint(1, 100)
            print('Your enemy has rolled ' + str(opponent_dice) + "\n")
            myPlayer.attack += player_dice
            spider.defense += opponent_dice
            difference = myPlayer.attack - spider.defense
            if difference > 0:
                spider.hp -= difference
                enemy_lost = str(spider.name) + " lost " + str(difference) + ' health. ' + str(spider.name) + "'s hp is: " + str(spider.hp) + '\n'
                for character in enemy_lost:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                player_health = str(myPlayer.name) + "'s hp is: " + str(myPlayer.hp) + "\n"
                for character in player_health:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
            else:
                enemy_defend = str(spider.name) + " defended!\n"
                for character in enemy_defend:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
            myPlayer.attack = myPlayer.original_attack
            spider.defense = spider.original_defense
            if spider.hp > 0:
                print("\nDefense phase: \n")
                player_dice = random.randint(1, 100)
                print('You rolled ' + str(player_dice))
                opponent_dice = random.randint(1, 100)
                print('Your enemy has rolled ' + str(opponent_dice) + "\n")
                myPlayer.defense += player_dice
                spider.attack += opponent_dice
                difference = spider.attack - myPlayer.defense
                if difference > 0:
                    myPlayer.hp -= difference
                    player_lost = str(myPlayer.name) + " lost " + str(difference) + ' health. ' + str(myPlayer.name) + "'s hp is: " + str(myPlayer.hp) + '\n'
                    for character in player_lost:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    enemy_hp = str(spider.name) + "'s hp is: " + str(spider.hp) + "\n"
                    for character in enemy_hp:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                else:
                    player_defeated = str(myPlayer.name) + " defended!\n"
                    for character in player_defeated:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                myPlayer.defense = myPlayer.original_defense
                spider.attack = spider.original_attack
            if spider.hp < 0:
                defeated = "\n" + spider.name + " is defeated!\n"
                for character in defeated:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                message = "\nNext to the " + spider.name + "'s body you see a strange 'fragment'\n."
                for character in message:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                zone_map[myPlayer.location][ITEMS] += "fragment"
                with open("items.txt", "r") as items:
                    s = []
                    for line in items:
                        s.append([line])
                    s.append(["fragment,That's a strange thing to find. It might become handy later. You put it in your backpack.,fragments,4ZX\n"])
                with open("items.txt", "w") as items:
                    for lists in s:
                        row = ','.join(lists)
                        items.write(row)
            elif myPlayer.hp < 0:
                print("You are defeated")
        else:
            print("There is nothing to attack")
        prompt()
    if myPlayer.location == "Goblin's Hollow":
        if myPlayer.hp > 0 and goblin.hp > 0:
            print("")
            player_dice = random.randint(1, 100)
            print('You rolled ' + str(player_dice))
            opponent_dice = random.randint(1, 100)
            print('Your enemy has rolled ' + str(opponent_dice) + "\n")
            myPlayer.attack += player_dice
            goblin.defense += opponent_dice
            difference = myPlayer.attack - goblin.defense
            if difference > 0:
                goblin.hp -= difference
                print(str(goblin.name) + " lost " + str(difference) + ' health. ' + str(goblin.name) + "'s hp is: " + str(goblin.hp))
                print(str(myPlayer.name) + "'s hp is: " + str(myPlayer.hp) + "\n")
            else:
                print(str(goblin.name) + " defended!")
            myPlayer.attack = myPlayer.original_attack
            goblin.defense = goblin.original_defense
            player_dice = random.randint(1, 100)
            print('You rolled ' + str(player_dice))
            opponent_dice = random.randint(1, 100)
            print('Your enemy has rolled ' + str(opponent_dice) + "\n")
            myPlayer.defense += player_dice
            goblin.attack += opponent_dice
            difference = goblin.attack - myPlayer.defense
            if difference > 0:
                myPlayer.hp -= difference
                print(str(myPlayer.name) + " lost " + str(difference) + ' health. ' + str(myPlayer.name) + "'s hp is: " + str(myPlayer.hp))
                print(str(goblin.name) + "'s hp is: " + str(goblin.hp) + "\n")
            else:
                print(str(myPlayer.name) + " defended!\n")
            myPlayer.defense = myPlayer.original_defense
            goblin.attack = goblin.original_attack
            if goblin.hp < 0:
                print(str(goblin.name) + " is defeated!")
            elif myPlayer.hp < 0:
                print("You are defeated")
        else:
            print("There is nothing to attack")
        prompt()

def main():
    second_screen()


if __name__ == "__main__":
    main()