'''
Made in the spirit of the negamax algorithm, this algorithm will do two things.
1. Implement a negamax in a partially observable environment.
2. Actually bring in the scoring algorithm that couldn't transfer for easyAI.
'''

class Custom_Negamax:
    """
    This implements Negamax on steroids. The following example shows
    how to setup the AI and play a Connect Four game:

        >>> from easyAI.games import ConnectFour
        >>> from easyAI import Negamax, Human_Player, AI_Player
        >>> scoring = lambda game: -100 if game.lose() else 0
        >>> ai_algo = Negamax(8, scoring) # AI will think 8 turns in advance
        >>> game = ConnectFour([Human_Player(), AI_Player(ai_algo)])
        >>> game.play()

    Parameters
    -----------

    depth:
      How many moves in advance should the AI think ?
      (2 moves = 1 complete turn)

    scoring:
      A function f(game)-> score. If no scoring is provided
         and the game object has a ``scoring`` method it ill be used.

    win_score:
      Score above which the score means a win. This will be
        used to speed up computations if provided, but the AI will not
        differentiate quick defeats from long-fought ones (see next
        section).

    tt:
      A transposition table (a table storing game states and moves)
      scoring: can be none if the game that the AI will be given has a
      ``scoring`` method.

    Notes
    -----

    The score of a given game is given by

    >>> scoring(current_game) - 0.01*sign*current_depth

    for instance if a lose is -100 points, then losing after 4 moves
    will score -99.96 points but losing after 8 moves will be -99.92
    points. Thus, the AI will chose the move that leads to defeat in
    8 turns, which makes it more difficult for the (human) opponent.
    This will not always work if a ``win_score`` argument is provided.

    """


    def __init__(self, depth, scoring=None, win_score=+inf, tt=None):
        self.scoring = scoring
        self.depth = depth
        self.tt = tt
        self.win_score= win_score



    def __call__(self,game):
        """
        Returns the AI's best move given the current state of the game.
        """

        scoring = self.scoring if self.scoring else (
                       lambda g: g.scoring() ) # horrible hack

        self.alpha = negamax(game, self.depth, self.depth, scoring,
                     -self.win_score, +self.win_score, self.tt)
        return game.ai_move
