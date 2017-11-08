#!/usr/bin/env python3

#python modules
import os
#My modules
from BADataObjects import Battle, Combatant
from BAHelpFunctions import createMoveset


if __name__== '__main__':

	#Create the necessary objects for attack moves and store them
	Available_Moves = createMoveset()

	'''
	#This is a one time script command that is used to create a text
	#document with all available moves and their stats.'''

	OutFileName = "./Guides/MovesGuide.txt"
	OutFile = open(OutFileName, 'w')
	OutFile.write("Move Guide:\n\n")
	for item in Available_Moves:
		OutFile.write(item+"\n")
		OutFile.write("Name:{}\n".format(Available_Moves[item].NAME))
		OutFile.write("Type:{}\n".format(Available_Moves[item].TYPE))
		OutFile.write("Element:{}\n".format(Available_Moves[item].ELEMENT))
		OutFile.write("\n") #Extra space for readability
	OutFile.close()
	#End script
	
	os.startfile(os.path.normpath(OutFileName))#Windows only
	#Create human player stats
	Human = Combatant("Stefan")
	OutFileName = "./Stats/PlayerStats.txt"
	OutFile = open(OutFileName, 'w')
	OutFile.write("Human Stats:\n\n")
	for attr, value in Human.__dict__.items():
		OutFile.write(attr + ": " + str(value) + "\n")

	OutFile.close()
	os.startfile(os.path.normpath(OutFileName))#Windows only

	#Create AI player stats
	AI = Combatant("Computer")
	OutFileName = "./Stats/ComputerStats.txt"
	OutFile = open(OutFileName, 'w')
	OutFile.write("Computer Stats:\n\n")
	for attr, value in AI.__dict__.items():
		OutFile.write(attr + ": " + str(value) + "\n")

	OutFile.close()
	os.startfile(os.path.normpath(OutFileName))#Windows only
