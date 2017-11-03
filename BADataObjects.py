#!/usr/bin/python3
import random

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

class Combatant(object):
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

	def createMoveset(self):
		#Moves are hardcoded to save time
		Normal_Physical = AttackMove("Attack", "PHYSICAL", "NONE")
		Normal_Magical = AttackMove("Arcane Blast", "MAGICAL", "NONE")
		Fire_Physical = AttackMove("Flametongue", "PHYSICAL", "FIRE")
		Water_Physical = AttackMove("Liquid Steel", "PHYSICAL", "WATER")
		Wind_Physical = AttackMove("Aeroblade", "PHYSICAL", "WIND")
		Earth_Physical = AttackMove("Terablade", "PHYSICAL", "EARTH")
		Fire_Magical = AttackMove("Fireblast", "MAGICAL", "FIRE")
		Wind_Magical = AttackMove("Aeroblast", "MAGICAL", "WIND")
		Water_Magical = AttackMove("Waterblast", "MAGICAL", "WATER")
		Earth_Magical = AttackMove("Terablast", "MAGICAL", "EARTH")

		self.MOVESET = {
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

		return
