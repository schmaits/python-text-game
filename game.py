# Python Text RPG

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

##### Player Setup #####
class player:
	def __init__(self):
		self.name = ''
		self.hp = 0
		self.mp = 0
		self.status_effects = []
		self.location = 'start'
myPlayer = player()

##### Title Screen #####
def title_screen_selections():
	option = input('> ')
	if option.lower() == ('play'):
		state_game() # placeholder until written
	elif option.lower() == ('help'):
		help_menu() # placeholder until written
	elif option.lower() == ('quit'):
		sys.exit()
	while option.lower() not in ['play', 'help', 'quit']:
		print('I can\'t do that')
		option = input('> ')
		if option.lower() == ('play'):
			state_game() # placeholder until written
		elif option.lower() == ('help'):
			help_menu() # placeholder until written
		elif option.lower() == ('quit'):
			sys.exit()

def title_screen():
	os.system('clear')
	print('########################')
	print('# Welcome to the game! #')
	print('########################')
	print('        - Play -        ')
	print('        - Help -        ')
	print('        - Quit -        ')
	title_screen_selections()

def help_menu():
	print('########################')
	print('# Welcome to the game! #')
	print('########################')
	print('- Type your commands to action them')
	print('- Use north, south, east, west to move')
	print('- Use look to inspect something')
	title_screen_selections()
	
##### Game Functionality #####
def start_game():

##### Map #####
"""
  1   2   3   4	# Player starts at b2
-----------------
|	|	|	|	|  a
-----------------
|	|	|	|	|  b
-----------------
|	|	|	|	|  c
-----------------
|	|	|	|	|  d
-----------------
"""

ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'al': False, 'a2': False, 'a3': False, 'a4': False,
				'bl': False, 'b2': False, 'b3': False, 'b4': False,
				'cl': False, 'c2': False, 'c3': False, 'c4': False,
				'dl': False, 'd2': False, 'd3': False, 'd4': False,
				}

zonemap = {'al': {
				ZONENAME: ''
				DESCRIPTION
				EXAMINATION
				UP = ''
				DOWN = 'b1'
				LEFT = ''
				RIGHT = 'a2'
				},
			'a2': {
				ZONENAME: ''
				DESCRIPTION = ''
				EXAMINATION = 
				UP = ''
				DOWN = 'b2'
				LEFT = 'a1'
				RIGHT = 'a3'
				}, 
			'a3': {
				ZONENAME: ''
				DESCRIPTION
				EXAMINATION
				UP = ''
				DOWN = 'b3'
				LEFT = 'a2'
				RIGHT = 'a4'
				}, 
			'a4': {
				ZONENAME
				DESCRIPTION
				EXAMINATION
				UP = ''
				DOWN = 'b4'
				LEFT = 'a3'
				RIGHT = ''
			},
			'bl': {
				ZONENAME: 'Graveyard'
				DESCRIPTION = 'Lots of tombstones, is that a hand emerging from one of them?!'
				EXAMINATION = 'Might be best to get out of here quick'
				UP = 'a1'
				DOWN = 'c1'
				LEFT = ''
				RIGHT = 'b2'
			}, 
			'b2': {
				ZONENAME: 'Home',
				DESCRIPTION = 'This is your home',
				EXAMINATION = 'Nothing looks different, but where is everyone?',
				UP = 'a2',
				DOWN = 'c2',
				LEFT = 'b1',
				RIGHT = 'b3'
			}, 
			'b3': {
				ZONENAME
				DESCRIPTION
				EXAMINATION
				UP = 'a3'
				DOWN = 'c3'
				LEFT = 'b2'
				RIGHT = 'b4'
			}, 
			'b4': {
				ZONENAME
				DESCRIPTION
				EXAMINATION
				UP = 'a4'
				DOWN = 'c4'
				LEFT = 'b3'
				RIGHT = ''
			},
			'cl': {
				ZONENAME
				DESCRIPTION
				EXAMINATION
				UP = 'b1'
				DOWN = 'd1'
				LEFT = ''
				RIGHT = 'c2'
			}, 
			'c2': {
				ZONENAME
				DESCRIPTION
				EXAMINATION
				UP = 'b2'
				DOWN = 'd2'
				LEFT = 'c1'
				RIGHT = 'c3'
			}, 
			'c3': {
				ZONENAME
				DESCRIPTION
				EXAMINATION
				UP = 'b3'
				DOWN = 'd3'
				LEFT = 'c2'
				RIGHT = 'c4'
			}, 
			'c4': {
				ZONENAME
				DESCRIPTION
				EXAMINATION
				UP = 'b4'
				DOWN = 'd4'
				LEFT = 'c3'
				RIGHT = ''
			},
			'dl': {
				ZONENAME
				DESCRIPTION
				EXAMINATION
				UP = 'c1'
				DOWN = ''
				LEFT = ''
				RIGHT = 'd2'
			}, 
			'd2': {
				ZONENAME
				DESCRIPTION
				EXAMINATION
				UP = 'c2'
				DOWN = ''
				LEFT = 'd1'
				RIGHT = 'd3'
			}, 
			'd3': {
				ZONENAME
				DESCRIPTION
				EXAMINATION
				UP = 'c3
				DOWN = ''
				LEFT = 'd2'
				RIGHT = 'd4'
			}, 
			'd4': {
				ZONENAME
				DESCRIPTION
				EXAMINATION
				UP = 'c4'
				DOWN = ''
				LEFT = 'd3'
				RIGHT = ''
			},
		}