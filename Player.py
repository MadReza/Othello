class Player(object):
    """Abstract Method to define rules for Players of Othello"""

    def __init__(self, game, player):
        self.game = game
        self.player = player

    def play():
        raise NotImplementedError("Inheritator forgot to implement this")

class Hooman(Player):

    def __init__(self, game, player):
        super(Hooman, self).__init__(game, player)

    def play(self):
        print "Player " + self.player + " turn to play!"
        possible_moves = self.game.get_possible_moves()
        print "Possible moves: " + str(possible_moves)
        if len(possible_moves) == 0:
            print "No moves possible!"
            return 1
        col = int(raw_input("Select coloumn: "))
        row = int(raw_input("Select row: "))
        #TODO: Add loop to validate move
        print "Player:", self.player, "Playing: col:", col, "row:", row
        self.game.play(col, row)

class Computer(Player):
    
    def __init__(self, game, player, AI):
        super(Computer, self).__init__(game, player)
        self.AI = AI

    def play(self):
        #initiate AI selected here
        possible_moves = self.game.get_possible_moves()
        if len(possible_moves) == 0:
            print "No moves possible:"
            return 1
        move = self.AI.get_next_move()
        col = move[0]
        row = move[1]
        print "Computer:", self.player, "Playing: col:",col, "row:", row
        self.game.play(col, row)
