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


#def start_game():


second_screen()
help_screen()