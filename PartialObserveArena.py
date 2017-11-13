import random
from BAHelpFunctions import findOpposingElement
'''
Made in the spirit of the negamax algorithm, this algorithm will do two things.
1. Implement a negamax in a partially observable environment.
2. Actually bring in the scoring algorithm that couldn't transfer for easyAI.
'''

def score_move(game, move):
	#Insert scoring algorithm
	#Scoring is NOT the same as the make_move algorithm.
	#Scoring depends on WHAT the AI knows. The AI starts by knowing
	#nothing, but learns as we go. IF the AI makes a move, the score should be rated
	#based on an algorithm that only takes into account knowns based on the
	#Human_Knowns dictionary.

	#initialize local variables
	guess_damage = 0
	score = 0
    learning_modifier = 0 #Increases the score of a move if it helps the AI
    #learn something.

	#fetch human knowns
	know_affinity = Human_Knowns["Affinity"]
	know_weakness = Human_Knowns["Weakness"]
	know_def = Human_Knowns["DEF"]
	know_mdef = Human_Knowns["MDEF"]
	know_att = Human_Knowns["ATT"]
	know_matt = Human_Knowns["MATT"]

	#Get positive attributes from current player

	ATT = game.player.ATT
	ATT_MIN = int(ceil(ATT * 0.2)) # Minimum of 20% ATT value as damage
	MATT = game.player.MATT
	MATT_MIN = int(ceil(MATT * 0.2)) # Minimum of 20% MATT value as damage
	AFFINITY = game.player.ELEMENTAL_AFFINITY

	#Get reductive attributes from other player
	#Note, you can only know these in a score from previous moves.
	if know_def:
		DEF = game.opponent.DEF
	else:
		DEF = 0

	if know_mdef:
		MDEF = game.opponent.MDEF
	else:
		MDEF = 0

	if know_weakness:
		WEAKNESS = game.opponent.ELEMENTAL_WEAKNESS
	else:
		WEAKNESS = "NONE"

	#Also fetch enemy attack stats.
	if know_affinity:
		ENEMY_AFFINITY = game.opponent.ELEMENTAL_AFFINITY
	else:
		ENEMY_AFFINITY = "NONE"
	if know_att:
		ENEMY_ATT = game.opponent.ATT
	else:
		ENEMY_ATT = 0
	if know_matt:
		ENEMY_MATT = game.opponent.MATT
	else:
		ENEMY_MATT = 0

	#Design note: Affinity and weakness each multiply damage by 1.5.
	#Max multiplier is therefore 2.25.
	if move.ELEMENT == AFFINITY and move.ELEMENT == WEAKNESS:
		ELEMENTAL_MULTIPLIER = 2.25
	elif move.ELEMENT == AFFINITY:
		ELEMENTAL_MULTIPLIER = 1.5
	elif move.ELEMENT == WEAKNESS:
		ELEMENTAL_MULTIPLIER = 1.5
	else:
		ELEMENTAL_MULTIPLIER = 1

	#Determine absolute damage with given attributes
	if move.TYPE == 'PHYSICAL':
		#Curb to minimum
		ROUGH_DAMAGE = ATT - DEF
		if ROUGH_DAMAGE < ATT_MIN:
			ROUGH_DAMAGE = ATT_MIN
		else:
			pass
		guess_damage = ROUGH_DAMAGE*ELEMENTAL_MULTIPLIER
	elif move.TYPE == 'MAGICAL':
		#Curb to minimum
		ROUGH_DAMAGE = MATT - MDEF
		if ROUGH_DAMAGE < MATT_MIN:
			ROUGH_DAMAGE = MATT_MIN
		else:
			pass
		guess_damage = ROUGH_DAMAGE*ELEMENTAL_MULTIPLIER

	'''Now determine learning modifier.'''

	'''
	Step 1: Equalize the scores by adding to the score of an attack if it is
	related to an unknown but not related to our affinity.

	We do this because the ideal situation based on incomplete data would max
	out at .5 of the difference between the related and opposing stats.
	(i.e. (ATT/MATT-DEF/MDEF)*.5 = Amount added by elemental affinity multiplier).

	We also want to minimize the ability of the human to guess our affinity,
	so a randomizing our attack is best.

	NOTE: Skip this step if you know both DEF and MDEF of the human.
	'''
	if not know_def or not know_mdef:
		if move.ELEMENT != AFFINITY:
			if move.TYPE == "PHYSICAL" and not know_def:
				learning_modifier = 0.5 * (ATT - DEF)
			elif move.TYPE == "MAGICAL" and not know_mdef:
				learning modifier = 0.5 * (MATT - MDEF)
			else:
				pass
		else:
			pass
	else:
		pass

	'''
	Step 2: With all scores equalized, increase the value of moves based on
	known, elemental factors.

	Example: If we know the affinity, we can eliminate one element from the table
	of potential weaknesses, and we have a high suspicion of what element their weakness
	may be.

	NOTE: Don't do this step at all if the AI already knows the weakness of the human.
	'''
	if not know_weakness:
		elements_tested = game.Elements_Tested
		#If the AI hasn't tested an element, add 50 to the learning modifier.
		if move.ELEMENT not in elements_tested:
			if know_affinity:
				reverse_element = findOpposingElement(ENEMY_AFFINITY)
				if move.ELEMENT == reverse_element:
					#We want a hard modifier here.
					#If you have a 50% chance of finding the weakness, that is your
					#most valuable move right now.
					learning_modifier += 50
				elif move.ELEMENT != ENEMY_AFFINITY:
					learning_modifier += 25
				else:
					pass
			else:
				learning_modifier += 50
		else:
			pass
	else:
		pass

	'''
	Step 3: After creating the learning modifier, add it onto the guess damage
	to determine our score.

	NOTE: NEVER skip this step.
	'''

	score = guess_damage + learning_modifier

	return score

def choose_move(game):
    #Collect moveset
    poss = game.possible_moves()
    #Collect known factors for opponent
    weakness = game.Human_Knowns["Weakness"]
    defense = game.Human_Knowns["DEF"]
    magic_defense = game.Human_Knowns["MDEF"]
    #If you have an ideal move, stick with it.
    if game.Ideal_Move:
    	game.ai_move = game.Ideal_Move
        game.make_move(game.ai_move)
        return game.ai_move
    else:
        #Otherwise, calculate a score for all moves and choose the best.
        top_score = 0
        ideal_moves = []
        for index, move in enumerate(poss):
            score = score_move(game, move)
            if score > top_score:
                top_score = score
                ideal_moves = [move]
            elif score == top_score:
                ideal_moves.append(move)
            else:
				#Ignore scores of moves less than current top score.
                pass
	    #Now, if you have exhausted all unknowns, you have your ideal move.
	    if weakness and defense and magic_defense:
	        game.Ideal_Move = ideal_moves[0]
	     	game.ai_move = game.Ideal_Move
	        game.make_move(game.ai_move)
	        return game.ai_move
	    elif len(ideal_moves) == 1:
			#If you don't know your unknowns but have only a list of length 1,
			#then make that move.
			game.ai_move = ideal_moves[0]
	        game.make_move(game.ai_move)
	        return game.ai_move
	    else:
			#Otherwise, make a random choice.
	        game.ai_move = random.choice(ideal_moves)
	        game.make_move(game.ai_move)
	        return game.ai_move
	#Only return failure if something went terribly wrong and the AI couldn't
	#make a move.
    return "FAILURE"




class Partial_Observe:
    """
    This is a custom algorithm that is made specifically for the Battle class.
    It borrows some ideas from negamax and machine learning, but, instead of using
	a longest path to defeat strategy, it uses a shortest path to victory. The
	algorithm involved also functions on the assumption that the universe is partially
	observable(i.e. both opponents start the game knowing nothing about each other.):

    Parameters
    -----------

    depth:
		How many moves in advance should the AI think ?
	  	(2 moves = 1 complete turn)
	  	Currently not used.

	chosen_move:
		After passing the algorithm, what move has the AI chosen?

    """


    def __init__(self, depth):
        self.depth = depth

    def __call__(self,game):
        """
        Returns the AI's best move given the current state of the game.
        """
        self.chosen_move = choose_move(game)
        return self.chosen_move
