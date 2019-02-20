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


def print location():
    print("\n" + ("#" * (4 + len(myPlayer.location))))
    print("#" + myPlayer.location.upper() + "#")
    print("#" + zonemap[myPlayer.location][DESCRIPTION]) # EZ SZERINTEM ITT LOCATION (nem POSITION)
    print("\n" + ("#" * (4 + len(myPlayer.location))))


def prompt():
    print("\n" + "===============")
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
    elif action.lower() in ["examine", "inspect", "interact", "look"]:
        player_examin(action.lower())


def player_move(myAction):
    ask = "Where would you like to move to?\n"
    dest = input(ask)
    if dest in ["up", "north"]:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ["down", "south"]:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)
    elif dest in ["left", "west"]:
        destination = zonemap[myPlayer.location][left]
        movement_handler(destination)
    elif dest in ["right", "east"]:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)
    

def movement_handler(destination):
    print("\n" + "You have moved to the " + destination + ".")
    myPlayer.location = destination
    print_location()


def player_examin(action):
    if zonemap[myPlayer.location][SOLVED]:
        print("You have already exhausted this zone.")
    else:
        print("You can trigger a puzzle here.")


def start_game():
    first_screen_options()


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
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_job = input('->')
    valid_jobs = ['warrior', 'mage', 'priest']
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print('You are now a ' + player_job + '!\n')
    while player_job.lower() not in valid_jobs:
        player_job = input('->')
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print('You are now a ' + player_job + '!\n')
    if myPlayer.job is 'warrior':
        self.hp = 140
        self.mp = 20
    if myPlayer.job is 'mage':
        self.hp = 40
        self.mp = 120
    if myPlayer.job is 'priest':
        self.hp = 80
        self.mp = 80

    question3 = 'Welcome, ' + player_name + "the " + player_job ".\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input('->')
    myPlayer.name = player_name

    speech1 = 'Hello'
    speech2 = 'Welcome'
    speech3 = 'Hola'
    speech4 = 'Guten tag'

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
    print('###########')
    print(" let's start ")
    print('############')
    main_game_loop()


first_screen_options()

csa