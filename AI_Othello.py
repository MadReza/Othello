from Othello import *

class AI_Othello(object):
    """Ai Player for Othello game engine"""

    def __init__(self, game, AI_player):
        """The Othello game and the player the AI is, we can start determining the moves and gameplay that should be performed"""
        self.game = game
        self.AI_player = AI_player

    def get_next_move(self):
        raise NotImplementedError("Inheritator forgot to implement this")

class MinMax_AI(AI_Othello):
    """MinMax using heuristic TO ADD HERE"""

    def __init__(self, game, AI_player, max_depth=0):
        """TODO: Not great to get the game as this shouldn't be changing anything"""
        """max_depth of 0 means to go to infinity"""
        super(MinMax_AI, self).__init__(game, AI_player)
        self.max_depth = max_depth

    def get_next_move(self):
        pass

    def min_max(self, board, depth, alpha, beta, player):
        """MinMax with pruning of the possile moves"""

        game_board = Othello.pre_built(board, player)
        game_moves = game_board.get_possible_moves()
        
        if len(game_moves) == 0: #TODO: Might cause trouble when no more moves available but game ain't over
            return positional_score(board), board
        
        if self.max_depth != 0 and depth >= self.max_depth: #max_depth of 0 is to infinit depth
            return positional_score(board), board

        if player == game_board.B:
            v = int("-inf") #the score of the board
            move = board    #The board that made that score

            for child_board in game_moves:
                s, b = min_max(child_board, depth+1, alpha, beta, game_board.get_opponent(player))
                if s > v:
                    v = s
                    move = b
                alpha = max(alpha, v)
                if beta <= alpha:
                    break    #Beta Pruning
            return v, move
        else:
            v = int("inf") #the best score of the board
            move = board   #the best board with that score

            for child_board in game_moves:
                s, b = min_max(child_board, depth+1, alpha, beta, game_board.get_opponent(player))
                if s < v:
                    v = s
                    move = b
                beta = min(beta, v)
                if beta <= alpha:
                    break    #Alpha Pruning
            return v, move

    #TODO: clean up this part later on
    pos_value = [
        [100, -1, 5, 2, 2, 5, -1, 100],
        [-1, -20, 1, 1, 1, 1, -20, -1],
        [ 5,   1, 1, 1, 1, 1,  1,  1 ],
        [ 2,   1, 1, 0, 0, 1,  1,  2 ],
        [ 2,   1, 1, 0, 0, 1,  1,  2 ],
        [ 5,   1, 1, 1, 1, 1,  1,  1 ],
        [-1, -20, 1, 1, 1, 1, -20, -1],
        [100, -1, 5, 2, 2, 5, -1, 100]
    ]
    
    def positional_score(self, board):
        score = 0

        for col in range(0, 9):
            for row in range(0, 9):
                if board[col][row] == "B":
                    score = score + pos_value[col][row]
                elif board[col][row] == "W":
                    score = score - pos_value[col][row]
        return score
        
                
class Greedy_AI(AI_Othello):
    """Greedy in terms of flips for each turn. The more you can flip the better for that turn"""

    def __init__(self, game, AI_player):
        """TODO: Not great to get the game as this shouldn't be changing anything"""
        super(Greedy_AI, self).__init__(game, AI_player)

    def get_next_move(self):
        possible_moves = self.game.get_possible_moves()
        best_move_score = self.game.score #Set to current initial score, Assumption that moves will always be better
        best_move = () #empty tuple to store best move

        print "possible moves: ", possible_moves

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
    

    
        
    
