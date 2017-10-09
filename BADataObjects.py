#!/usr/bin/python3
from random import choice


BATTLE_CLASS_OPTIONS = [
    'Melee',
    'Balanced',
    'Magic']

class Combatant():

	BATTLECLASS = ""
	HP = 0
	MP = 0
	ATT = 0
	MATT = 0
	DEF = 0
	MDEF = 0
	MOVESET = {}

	def __init__(self):
		self.BATTLECLASS = self.randomizeClass()
		self.GenerateStats()
		self.GenerateMoveset()

	def randomizeClass(self):
		return random.choice(BATTLE_CLASS_OPTIONS)

	def GenerateStats(self):
		FighterType = self.BATTLECLASS

		if FighterType == "Melee":
			pass
		elif FighterType == "Balanced":
			pass
		elif FighterType == "Magic":
			pass
		else:
			#If something failed, then auto set class to balanced and call method again.
			self.BATTLECLASS = "Balanced"
			self.GenerateStats

		return

	def GenerateMoveset:
		#Probably create a database here. Simple MYSQL or postgres ought to do.
		return




