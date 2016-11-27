class Player(object):
    """Abstract Method to define rules for Players of Othello"""

    def __init__(self, game, player):
        self.game = game
        self.player = player

    def play():
        raise NotImplementedError("Inheritator should implement this")

class Hooman(Player):

    def __init__(self, game, player):
        super(Hooman, self).__init__(game, player)

    def play():
        print "Player " + self.player + " turn to play!"
        print "Possible moves: " + str(self.game.get_possible_moves())
        col = int(raw_input("Select coloumn: "))
        row = int(raw_input("Select row: "))
        #TODO: Add loop to validate move
        self.game.play(col, row)

class Computer(Player):
    
    def __init__(self, game, player, AI):
        super(Hooman, self).__init__(game, player)
        self.AI = AI

    def play():
        #initiate AI selected here
        self.game.play(col, row)