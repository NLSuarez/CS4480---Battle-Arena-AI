#!/usr/bin/python3
import random
from math import ceil
#3rd party modules
from easyAI import TwoPlayersGame

TYPE_OPTIONS = [
	'MAGICAL'
	'PHYSICAL']

ELEMENTAL_OPTIONS = [
	'FIRE',
	'EARTH',
	'WATER',
	'WIND']

class AttackMove(object):
	"""Attack Moves for a combatant"""
	NAME = ""
	TYPE = ""
	ELEMENT = ""

	def __init__(self, name, attack_type, attack_element):
		super(AttackMove, self).__init__()
		self.NAME = name
		self.TYPE = attack_type
		self.ELEMENT = attack_element

	def __str__(self):
		return self.NAME

class Combatant(object):
	"""An arena combatant.
	Class contains all attributes common to both players."""
	NAME = "" #determined at creation
	ELEMENTAL_AFFINITY = ""
	ELEMENTAL_WEAKNESS = ""
	MAX_HP = 0 #Static
	HP = 0 #Current
	ATT = 0
	MATT = 0
	DEF = 0
	MDEF = 0
	#MOVESET = {}

	def __init__(self, name):
		super(Combatant, self).__init__()
		self.NAME = name
		self.randomizeElements()
		self.generateStats()

	def randomizeElements(self):
		'''
		Design thoughts on elements:
		Elements should have a high chance of being directly opposed from each other when picking affinities and weaknesses.
		This is because of the fact that we assume an enemy will use their elemental affinity more than other attacks if possible.
		That is because they typically do more damage with their affinity. However, using one's affinity can be a drawback
		in any real battle if your weakness is the obvious and direct opposite of that affinity. To encourage thinking
		on the part of the AI and the User, we want both to try and find their weakness based on previous moves, so we should make
		the weakness somewhat predictable.

		For now, the elemental opposites are as follows:
			WIND > EARTH > WATER > FIRE > WIND
		'''

		#Choose affinity
		elemental_affinity = random.choice(ELEMENTAL_OPTIONS)
#		print("Elemental Affinity: {}".format(elemental_affinity)) #debug

		#Make new list of elements without affinity
		elements_eligible = list(ELEMENTAL_OPTIONS)
		#Note, you must use the list function or you're editing the same list
#		print(elements_eligible) #debug
		elements_eligible.remove(elemental_affinity)
#		print(elements_eligible) #debug

		#Parse based on affinity to determine weakness
		#50% to have the obvious weakness. 50% to have a randomized other.
		#Note, you cannot be weak to your affinity
		if elemental_affinity == "WIND":
			if random.random() < 0.5:
				elemental_weakness = "FIRE"
			else:
				#If not the obvious weakness, remove obvious weakness
				#And roll between the last two
				elements_remaining = list(elements_eligible)
				elements_remaining.remove("FIRE")
				elemental_weakness = random.choice(elements_remaining)
		elif elemental_affinity == "EARTH":
			if random.random() < 0.5:
				elemental_weakness = "WIND"
			else:
				elements_remaining = list(elements_eligible)
				elements_remaining.remove("WIND")
				elemental_weakness = random.choice(elements_remaining)
		elif elemental_affinity == "WATER":
			if random.random() < 0.5:
				elemental_weakness = "EARTH"
			else:
				elements_remaining = list(elements_eligible)
				elements_remaining.remove("EARTH")
				elemental_weakness = random.choice(elements_remaining)
		elif elemental_affinity == "FIRE":
			if random.random() < 0.5:
				elemental_weakness = "WATER"
			else:
				elements_remaining = list(elements_eligible)
				elements_remaining.remove("WATER")
				elemental_weakness = random.choice(elements_remaining)
		else:
			print("Error")
			exit()

#		print("Elemental Weakness: {}".format(elemental_weakness)) #debug
		self.ELEMENTAL_AFFINITY = elemental_affinity
		self.ELEMENTAL_WEAKNESS = elemental_weakness
		return


	def generateStats(self):
		#HP should be consistent between opponents for now
		self.MAX_HP = 500
		self.HP = 500
		#DEF and ATT are physical based and directly opposed
		#MDEF and MATT are magical based and directly opposed
		#For now, we will focus on randomized static values
		#50% chance to specialize in ATT or MATT
		if random.random() < 0.5:
			self.ATT = random.randrange(75, 100, 1)
			self.MATT = random.randrange(25, 50, 1)
		else:
			self.MATT = random.randrange(75, 100, 1)
			self.ATT = random.randrange(25, 50, 1)

		#Same chance for Def and MDef
		#For implementation's sake, remember that damage reduction is capped at 80%
		if random.random() < 0.5:
			self.DEF = random.randrange(75, 100, 1)
			self.MDEF = random.randrange(25, 50, 1)
		else:
			self.MDEF = random.randrange(75, 100, 1)
			self.DEF = random.randrange(25, 50, 1)

#		print("HP:{}".format(self.HP)) #debug
#		print("ATT:{}".format(self.ATT)) #debug
#		print("MATT:{}".format(self.MATT)) #debug
#		print("DEF:{}".format(self.DEF)) #debug
#		print("MDEF:{}".format(self.MDEF)) #debug


		return


class HumanCombatant(Combatant):
	"""A human, arena combatant."""

	def __init__(self, name):
		super(HumanCombatant, self).__init__(name)

	def ask_move(self, game):
		possible_moves = game.possible_moves()
		# The str version of every move for comparison with the user input:
		possible_moves_str = list(map(str, game.possible_moves()))
		move = "NO_MOVE_DECIDED_YET"
		while True:
			move = input("\nPlayer %s what do you play ? "%(game.nplayer))
			if move == 'show moves':
				print ("Possible moves:\n"+ "\n".join(
					["#%d: %s"%(i+1,m) for i,m in enumerate(possible_moves)])
					+"\nType a move or type 'move #move_number' to play.")

			elif move == 'quit':
				raise KeyboardInterrupt

			elif move.startswith("move #"):
				# Fetch the corresponding move and return.
				move = possible_moves[int(move[6:])-1]
				return move

			elif str(move) in possible_moves_str:
				# Transform the move into its real type (integer, etc. and return).
				move = possible_moves[possible_moves_str.index(str(move))]
				return move

	def is_human(self):
		return True

class AICombatant(Combatant):
	def __init__(self, AI_algo, name):
		super(AICombatant, self).__init__(name)
		self.AI_algo = AI_algo
		self.move = {}

	def ask_move(self, game):
		return self.AI_algo(game)

	def is_human(self):
		return False

class Battle( TwoPlayersGame ):
	"""
	Rules:
	1. No board.
	2. 2 players.
	3. Attack that decreases opponents health to 0 fastest should be dominant
	strategy
	"""

	#AI data collection on opponent.
	#Determines the known factors of the human by the AI
	Human_Knowns = {
		"Affinity": False,
		"Weakness": False,
		"ATT": False,
		"MATT": False,
		"DEF": False,
		"MDEF": False
	}

	Elements_Tested = [
	]

	Elements_Used_By_Human = [
	]
	#Speed up the AI
	#We will store the ideal move after it's found.
	#This will be determined after, at most, 4 moves.
	Ideal_Move = False

	def __init__(self, moveset, players):
		self.moveset = moveset
		self.players = players
		self.nplayer = 1 # player 1 starts.
		return

	def possible_moves(self):
		#Possible moves related to moveset
		return self.moveset

	def make_move(self, move):
		#initialize variables
		Damage = 0

		#Get positive attributes from current player

		ATT = self.player.ATT
		ATT_MIN = int(ceil(ATT * 0.2)) # Minimum of 20% ATT value as damage
		MATT = self.player.MATT
		MATT_MIN = int(ceil(MATT * 0.2)) # Minimum of 20% MATT value as damage
		AFFINITY = self.player.ELEMENTAL_AFFINITY

		#Get reductive attributes from other player
		DEF = self.opponent.DEF
		MDEF = self.opponent.MDEF
		WEAKNESS = self.opponent.ELEMENTAL_WEAKNESS

		#Design note: Affinity and weakness each multiply damage by 1.5.
		#Max multiplier is therefore 2.25.
		ELEMENTAL_MULTIPLIER = 1
		if move.ELEMENT == AFFINITY and move.ELEMENT == WEAKNESS:
			ELEMENTAL_MULTIPLIER = 2.25
		elif move.ELEMENT == AFFINITY:
			ELEMENTAL_MULTIPLIER = 1.5
		elif move.ELEMENT == WEAKNESS:
			ELEMENTAL_MULTIPLIER = 1.5

		#Determine absolute damage with given attributes
		if move.TYPE == 'PHYSICAL':
			#Curb to minimum
			ROUGH_DAMAGE = ATT - DEF
			if ROUGH_DAMAGE < ATT_MIN:
				ROUGH_DAMAGE = ATT_MIN
			else:
				pass
			Damage = ROUGH_DAMAGE*ELEMENTAL_MULTIPLIER
		elif move.TYPE == 'MAGICAL':
			#Curb to minimum
			ROUGH_DAMAGE = MATT - MDEF
			if ROUGH_DAMAGE < MATT_MIN:
				ROUGH_DAMAGE = MATT_MIN
			else:
				pass
			Damage = int(ceil(ROUGH_DAMAGE*ELEMENTAL_MULTIPLIER))

		#Update HP
		self.opponent.HP = self.opponent.HP - Damage
		#If less than 0, set HP to 0.
		if self.opponent.HP < 0:
			self.opponent.HP = 0
		#Now update unknowns
		self.update_unknowns(move)
		#Return damage done.
		return Damage

	def lose(self):
		return self.player.HP == 0

	def is_over(self):
		#Game is over if you have 0 hp
		return self.lose()

	def show(self):
		if self.opponent.is_human:
			print("The Computer's current HP is {}.".format(self.player.HP))
			print("Your current HP is {}.".format(self.opponent.HP))
		else:
			print("Your current HP is {}.".format(self.player.HP))
			print("The Computer's current HP is {}.".format(self.opponent.HP))

	def update_unknowns(self, move):
		'''Step 1: Recognize if the AI is making the move.'''
		if not self.player.is_human():
			'''Track 1 - Step 2: Analyze damage type.'''
			if move.TYPE == "PHYSICAL" and not self.Human_Knowns["DEF"]:
				self.Human_Knowns["DEF"] = True #Performance hack.
				'''
				We assume the AI could easily reverse and solve for the DEF
				value of an opponent given that we already have an equation for
				it, but we choose to bypass that since the computer already has
				the value in memory. Same for all other values. These are
				performance hacks.
				'''
			elif move.TYPE == "MAGICAL" and not self.Human_Knowns["MDEF"]:
				self.Human_Knowns["MDEF"] = True
			else:
				pass #If you know both DEF and MDEF, go to step 2.

			'''Track 1 - Step 3: Update elements.'''
			#Case 1: We have found the weakness, so we pass over everything.
			if self.Human_Knowns["Weakness"]:
				pass
			#Case 2: We don't know the elemental weakness of our opponent, but our
			#latest move exposed it.
			elif move.ELEMENT == self.opponent.ELEMENTAL_WEAKNESS:
				self.Human_Knowns["Weakness"] = True
			#Case 3: We don't know the weakness, and the element is not in our
			#list of elements tested.
			#NOTE: DO NOT INCLUDE NONE!
			elif move.ELEMENT != "NONE" and move.ELEMENT not in self.Elements_Tested:
				self.Elements_Tested.append(move.ELEMENT)
				if len(self.Elements_Tested) == (len(ELEMENTAL_OPTIONS) - 1):
					self.Human_Knowns["Weakness"] = True
				else:
					pass
			#Case 4: Element in list and not a weakness.
			else:
				pass
		else:
			'''Track 2 - Step 2: If the current player is human, analyze their
			attacks to find attack stats.'''
			if move.TYPE == "PHYSICAL" and not self.Human_Knowns["ATT"]:
				self.Human_Knowns["ATT"] = True #Performance hack.
			elif move.TYPE == "MAGICAL" and not self.Human_Knowns["MATT"]:
				self.Human_Knowns["MATT"] = True
			else:
				pass #If you know both ATT and MATT, go to step 2.

			'''Track 2 - Step 3: Find Affinity.'''
			#Case 1: We know the affinity already.
			if self.Human_Knowns["Affinity"]:
				pass
			#Case 2: We don't know the elemental affinity of our opponent, but their
			#latest move exposed it.
			elif move.ELEMENT == self.player.ELEMENTAL_AFFINITY:
				self.Human_Knowns["Affinity"] = True
			#Case 3: We don't know the affinity, and the element is not in the AI's
			#list of elements used by the human.
			#NOTE: DO NOT INCLUDE NONE!
			elif move.ELEMENT != "NONE" and move.ELEMENT not in self.Elements_Used_By_Human:
				self.Elements_Used_By_Human.append(move.ELEMENT)
				#Subcase: If all but one of the elements have been used and we still
				#don't know the affinity, then we assume, by process of elimination,
				#that the affinity is the remaining element.
				if len(self.Elements_Used_By_Human) == (len(ELEMENTAL_OPTIONS) - 1):
					self.Human_Knowns["Affinity"] = True
				else:
					pass
			#Case 4: Element in list and not an affinity.
			else:
				pass
