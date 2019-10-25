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
		print('I can't do that')
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
