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

	MOVESET = [
		Normal_Physical,
		Normal_Magical,
		Fire_Physical,
		Water_Physical,
		Wind_Physical,
		Earth_Physical,
		Fire_Magical,
		Wind_Magical,
		Water_Magical,
		Earth_Magical
	]

	return MOVESET

'''To create a guide for the player.'''
def createMoveGuide():
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

	OutFileName = "./Guides/MovesGuide.txt"
	OutFile = open(OutFileName, 'w')
	OutFile.write("Move Guide:\n\n")
	for item in MOVESET:
		OutFile.write(item+"\n")
		OutFile.write("Name:{}\n".format(Available_Moves[item].NAME))
		OutFile.write("Type:{}\n".format(Available_Moves[item].TYPE))
		OutFile.write("Element:{}\n".format(Available_Moves[item].ELEMENT))
		OutFile.write("\n") #Extra space for readability

	OutFile.close()

'''To return the opposite element.'''
def findOpposingElement(element):
	#python version of a switch statement.
	reverse_element = {
		'FIRE':'WATER',
		'WATER':'EARTH',
		'EARTH':'WIND',
		'WIND':'FIRE',
		'NONE':'NONE'
	}
	return reverse_element[element]
