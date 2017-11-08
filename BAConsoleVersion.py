#3rd party modules
from easyAI import TwoPlayersGame
from easyAI.Player import Human_Player
#My modules
from BADataObjects import Battle, Combatant
from BAHelpFunctions import createMoveset


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
