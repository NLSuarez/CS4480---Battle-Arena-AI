#3rd party modules
from easyAI import TwoPlayersGame
from easyAI.Player import Human_Player
#My modules
import BADataObjects

class Battle( TwoPlayersGame ):
	"""
	Rules:
	1. No board.
	2. 2 players.
	3. Attack that decreases opponents health to 0 fastest should be dominant
	strategy
	"""

	def __init__(self, players):
		self.players = players
		self.nplayer = 1 # player 1 starts.
		return

	def possible_moves(self):
		return

	def make_move(self, move):
		return

	def unmake_move(self, move): # optional method (speeds up the AI)
		return

	def lose(self):
		""" Are you at 0 hp? """
		return

	def is_over(self):
		return self.lose()

	def show(self):
		return

	def scoring(self):
		return

def createMoveset():
	#Moves are hardcoded to save time
	Normal_Physical = BADataObjects.AttackMove("Attack", "PHYSICAL", "NONE")
	Normal_Magical = BADataObjects.AttackMove("Arcane Blast", "MAGICAL", "NONE")
	Fire_Physical = BADataObjects.AttackMove("Flametongue", "PHYSICAL", "FIRE")
	Water_Physical = BADataObjects.AttackMove("Liquid Steel", "PHYSICAL", "WATER")
	Wind_Physical = BADataObjects.AttackMove("Aeroblade", "PHYSICAL", "WIND")
	Earth_Physical = BADataObjects.AttackMove("Terablade", "PHYSICAL", "EARTH")
	Fire_Magical = BADataObjects.AttackMove("Fireblast", "MAGICAL", "FIRE")
	Wind_Magical = BADataObjects.AttackMove("Aeroblast", "MAGICAL", "WIND")
	Water_Magical = BADataObjects.AttackMove("Waterblast", "MAGICAL", "WATER")
	Earth_Magical = BADataObjects.AttackMove("Terablast", "MAGICAL", "EARTH")

	MOVESET = {
		"Attack" : Normal_Physical,
		"Arcane Blast" : Normal_Magical,
		"Flametongue" : Fire_Physical,
		"Liquid Steel" : Water_Physical,
		"Aeroblade" : Wind_Physical,
		"Terablade" : Earth_Physical,
		"Fireblast" : Fire_Magical,
		"Aeroblast" : Wind_Magical,
		"Waterblast" : Water_Magical,
		"Terablast" : Earth_Magical
	}

	return MOVESET

if __name__== '__main__':

	#Create the necessary objects for attack moves and store them
	Available_Moves = createMoveset()

	#Print these strings into a .txt document
	print("Available Moves:")
	for item in Available_Moves:
		print(item)
		print("Name:{}".format(Available_Moves[item].NAME))
		print("Type:{}".format(Available_Moves[item].TYPE))
		print("Element:{}".format(Available_Moves[item].ELEMENT))

	#Create human player stats
	Human = BADataObjects.Combatant("Stefan")
	print("Human Stats:")
	for attr, value in Human.__dict__.items():
		print(attr, value)

	#Create AI player stats
	AI = BADataObjects.Combatant("Computer")
	print("Computer Stats:")
	for attr, value in AI.__dict__.items():
		print(attr, value)
