#!/usr/bin/env python3

#python modules
import os
#3rd party
from easyAI import Negamax
#My modules
from BADataObjects import Battle, HumanCombatant, AICombatant
from BAHelpFunctions import createMoveset, createMoveGuide


if __name__== '__main__':

	#Create the necessary objects for attack moves and store them
	Available_Moves = createMoveset()

	'''
	#This is a one time script command that is used to create a text
	#document with all available moves and their stats.

	createMoveGuide()
	#End script
	'''

	'''Create necessary documents and open them.'''
	OutFileName = "./Guides/MovesGuide.txt"
	os.startfile(os.path.normpath(OutFileName))#Windows only
	#Create human player stats
	Human = HumanCombatant("Stefan")
	OutFileName = "./Stats/PlayerStats.txt"
	OutFile = open(OutFileName, 'w')
	OutFile.write("Human Stats:\n\n")
	for attr, value in Human.__dict__.items():
		#remove extraneous fields and write
		if attr != "name":
			OutFile.write(attr + ": " + str(value) + "\n")

	OutFile.close()
	os.startfile(os.path.normpath(OutFileName))#Windows only

	#Create AI player stats
	ai_algo = Negamax(2) #Think for this round and the next.
	AI = AICombatant(ai_algo, "Computer")
	OutFileName = "./Stats/ComputerStats.txt"
	OutFile = open(OutFileName, 'w')
	OutFile.write("Computer Stats:\n\n")
	for attr, value in AI.__dict__.items():
		#remove extraneous fields and write
		if attr != ("name" or "AI_algo" or "move"):
			OutFile.write(attr + ": " + str(value) + "\n")

	OutFile.close()
	os.startfile(os.path.normpath(OutFileName))#Windows only

	'''Create game object and operate.'''
	ArenaMatch = Battle( Available_Moves, [Human, AI])
	while not ArenaMatch.is_over():
	    ArenaMatch.show()
	    if ArenaMatch.nplayer==1:  # we are assuming player 1 is a Human_Player
	        poss = ArenaMatch.possible_moves()
	        for index, move in enumerate(poss):
	            print("{} : {}".format(index, move.NAME))
	        index = int(input("Choose attack number: "))
	        move = poss[index]
	    else:  # we are assuming player 2 is an AI_Player
	        move = ArenaMatch.get_move()
	        print("AI plays {}".format(move))
	    ArenaMatch.play_move(move)
