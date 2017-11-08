#!/usr/bin/python3
import random
#3rd party modules
from easyAI import TwoPlayersGame
from easyAI.Player import Human_Player, AI_Player

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

class HumanCombatant(Human_Player):
	"""An arena combatant."""
	NAME = "" #determined at creation
	ELEMENTAL_AFFINITY = ""
	ELEMENTAL_WEAKNESS = ""
	HP = 0
	ATT = 0
	MATT = 0
	DEF = 0
	MDEF = 0
	#MOVESET = {}

	def __init__(self, name):
		super(HumanCombatant, self).__init__()
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

class AICombatant(AI_Player):
	"""An arena combatant."""
	NAME = "Computer"
	ELEMENTAL_AFFINITY = ""
	ELEMENTAL_WEAKNESS = ""
	HP = 0
	ATT = 0
	MATT = 0
	DEF = 0
	MDEF = 0
	#MOVESET = {}

	def __init__(self, AI_algo):
		super(AICombatant, self).__init__(AI_algo, name=self.NAME)
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

class Battle( TwoPlayersGame ):
	"""
	Rules:
	1. No board.
	2. 2 players.
	3. Attack that decreases opponents health to 0 fastest should be dominant
	strategy
	"""

	#Determines the known factors of the human
	Human_Knowns = { 
		"Affinity": False,
		"Weakness": False,
		"ATT": False,
		"MATT": False,
		"DEF": False,
		"MDEF": False
	}

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
		ATT_MIN = ATT * 0.2 # Minimum of 20% ATT value as damage
		MATT = self.player.MATT
		MATT_MIN = MATT * 0.2 # Minimum of 20% MATT value as damage
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
			Damage = ROUGH_DAMAGE*ELEMENTAL_MULTIPLIER	
		
		self.opponent.HP = self.opponent.HP - Damage

	def unmake_move(self, move): # optional method (speeds up the AI)
		#initialize variables
		Damage = 0
		
		#Get positive attributes from current player

		ATT = self.player.ATT
		ATT_MIN = ATT * 0.2 # Minimum of 20% ATT value as damage
		MATT = self.player.MATT
		MATT_MIN = MATT * 0.2 # Minimum of 20% MATT value as damage
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
			Damage = ROUGH_DAMAGE*ELEMENTAL_MULTIPLIER

        self.opponent.HP = self.opponent.HP + Damage #Run the same calculations, but reverse damage.

	def lose(self):
		return self.player.HP == 0

	def is_over(self):
		#Game is over if you have 0 hp
		return self.lose()

	def scoring(self):
		#Insert scoring algorithm
		#Scoring is NOT the same as the make_move algorithm.
		#Scoring depends on WHAT the AI knows. The AI starts by knowing
		#nothing, but learns as we go. IF the AI makes a move, the score should be rated
		#based on an algorithm that only takes into account knowns based on the 
		#Human_Knowns dictionary.
		score = 0 #initiate at 0
		#If you have lost, your score is immediately -100
		if self.lose():
			score = -100
			return score
		else:
			pass
		#Otherwise, use the formula
		#initialize variables
		Damage = 0
		
		#Get positive attributes from current player
		#Positive attributes will ALWAYS be known

		ATT = self.player.ATT
		ATT_MIN = ATT * 0.2 # Minimum of 20% ATT value as damage
		MATT = self.player.MATT
		MATT_MIN = MATT * 0.2 # Minimum of 20% MATT value as damage
		AFFINITY = self.player.ELEMENTAL_AFFINITY
		
		#Get reductive attributes from other player
		#Reductive attributes may or may NOT be known
		if self.Human_Knowns["DEF"]:
			DEF = self.opponent.DEF
		else:
			DEF = 0 #If the AI doesn't know the defense, we assume we will do 100% of our att

		#Repeat for others
		if self.Human_Knowns["MDEF"]:
			MDEF = self.opponent.MDEF
		else:
			MDEF = 0
		if self.Human_Knowns["Weakness"]:
			WEAKNESS = self.opponent.ELEMENTAL_WEAKNESS
		else:
			WEAKNESS = False

		#Design note: Affinity and weakness each multiply damage by 1.5.
		#Max multiplier is therefore 2.25.
		'''PROBLEM!!! Move isn't available here! Move "moves" back to the Combatant classes.
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
			Damage = ROUGH_DAMAGE*ELEMENTAL_MULTIPLIER
		'''

		return score
