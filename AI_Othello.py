from Othello import *

class AI_Othello(object):
    """Ai Player for Othello game engine"""

    def __init__(self, game, AI_player):
        """The Othello game and the player the AI is, we can start determining the moves and gameplay that should be performed"""
        self.game = game
        self.AI_player = AI_player

    def get_next_move(self):
        raise NotImplementedError("Inheritator forgot to implement this")

class Greed_AI(AI_Othello):
    """Greedy in terms of flips for each turn. The more you can flip the better for that turn"""

    def __init__(self, game, AI_player):
        """TODO: Not great to get the game as this shouldn't be changing anything"""
        super(Greed_AI, self).__init__(game, AI_player)

    def get_next_move(self):
        possible_moves = self.game.get_possible_moves()
        best_move_score = self.game.score #Set to current initial score
        best_move = () #empty tuple to store best move

        for move in possible_moves:
            col = move[0]
            row = move[1]
            
            test_move = Othello.pre_built(self.game.board, self.AI_player)
            test_move.play(col, row)

            if self.__better_score__(best_move_score, test_move.score) == 1:
                best_move_score = test_move.score
                best_move = move
        return best_move

    def __better_score__(self, init_score, new_score):
        """TODO: remove this from here but for now depending if the player is White or Black the better score
                 would be negative or positive"""
        """  1 for new_score is better score
            -1 for new_score is not better score
             0 for Tie"""
        if self.AI_player == self.game.B:
            if new_score > init_score:
                return 1
            elif new_score < init_score:
                return -1
        else:
            if new_score < init_score:
                return 1
            elif new_score > init_score:
                return -1
        return 0
    

    
        
    
