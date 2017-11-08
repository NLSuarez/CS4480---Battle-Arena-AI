#!/usr/bin/python3
from BADataObjects import AttackMove

'''Docstring: To create attack moves.
Moves are hardcoded to save time.'''
def createMoveset():
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