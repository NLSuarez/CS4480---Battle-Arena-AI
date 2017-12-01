#!/usr/bin/env python3

#python modules
import os
#My modules
from BADataObjects import Battle, HumanCombatant, AICombatant
from BAHelpFunctions import createMoveset, createMoveGuide
from PartialObserveArena import Partial_Observe


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
	try:
		os.startfile(os.path.normpath(OutFileName))#Windows only
	except:
		pass
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
	try:
		os.startfile(os.path.normpath(OutFileName))#Windows only
	except:
		pass

	#Create AI player stats
	ai_algo = Partial_Observe(2)
	AI = AICombatant(ai_algo, "Computer")
	'''Debug stats for AI are output to a file.'''
	OutFileName = "./Stats/ComputerStats.txt"
	OutFile = open(OutFileName, 'w')
	OutFile.write("Computer Stats:\n\n")
	for attr, value in AI.__dict__.items():
		#remove extraneous fields and write
		if attr != ("name" or "AI_algo" or "move"):
			OutFile.write(attr + ": " + str(value) + "\n")

	OutFile.close()
	#Comment out this line if playing for real and not debugging.
	try:
		os.startfile(os.path.normpath(OutFileName))#Windows only
	except:
		pass

	'''Create game object and operate.'''
	ArenaMatch = Battle( Available_Moves, [Human, AI])
	while not ArenaMatch.is_over():
		print("\n")
		ArenaMatch.show()
		print("\n")
		if ArenaMatch.nplayer==1:  # we are assuming player 1 is a Human_Player
			poss = ArenaMatch.possible_moves()
			for index, move in enumerate(poss):
				print("{} : {}".format(index, move.NAME))
			print("\n")
			index = int(input("Choose attack number: "))
			move = poss[index]
			print("\n")
			print("You used '{}'.".format(move.NAME))
			print("\n")
		else:  # we are assuming player 2 is an AI_Player
			move = ArenaMatch.get_move()
			print("\n")
			print("The Computer used '{}'.".format(move.NAME))
			print("\n")

		damage = ArenaMatch.play_move(move) #Method returns damage for us.
		print("It did {} points in {} and {} damage.".format(damage, move.ELEMENT, move.TYPE))

		if move.ELEMENT == ArenaMatch.player.ELEMENTAL_WEAKNESS and move.ELEMENT == ArenaMatch.opponent.ELEMENTAL_AFFINITY:
			print("It was super effective and enhanced!")
		elif move.ELEMENT == ArenaMatch.player.ELEMENTAL_WEAKNESS:
			print("It was super effective!")
		elif move.ELEMENT == ArenaMatch.opponent.ELEMENTAL_AFFINITY:
			print("It was enhanced!")
	print("\n")
	if AI.HP == 0:
		print("Congratulations, human. You beat me.")
	elif Human.HP == 0:
		print("Game Over. You lost.")
