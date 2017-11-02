import BADataObjects

if __name__== '__main__':

	Human = BADataObjects.Combatant("Stefan")
	print("Human Stats:")
	for attr, value in Human.__dict__.items():
		print(attr, value)

	AI = BADataObjects.Combatant("Computer")
	print("Computer Stats:")
	
	for attr, value in AI.__dict__.items():
		print(attr, value)