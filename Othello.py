from Player import *
from AI_Othello import *

print "Othello Start***"

print "Display: "

print "________________"
print "[ O | O | O | O ]"
print "[ 0 | W | B | O ]"
print "[ 0 | B | W | O ]"
print "[ O | O | O | O ]"
print "________________"

class Othello:
    """Othello Game Engine"""

    W = "W"     #TODO: Renamed W and B with better names
    B = "B"
    row = 8     #Eventually upgrade to adjustable board
    col = 8
    BOARD_TOTAL_MOVES = row * col    
     
    
    def __init__(self):
        self.__reset_board__()

    @classmethod
    def pre_built(cls, board, turn):
        """When you have a setup you want to load"""
        """TODO: Later with board being changable will require a verifier"""
        new_game = cls()
        new_game.__reset_board__()
        new_game.board = [[board[col][row] for row in range(new_game.row)] for col in range(new_game.col)]
        new_game.turn = turn
        return new_game

    def __reset_board__(self):
        self.board = [[' ' for row in range(self.row)] for col in range(self.col)]
        self.board[3][3] = self.B
        self.board[4][4] = self.B
        self.board[3][4] = self.W
        self.board[4][3] = self.W
        self.cur_moves = 4
        self.history = []   #Takes Tuples of (x,y) values with Black be first
        self.turn = self.B
        self.score = 0   #+1 for Black Pieces -1 for White Pieces.
        
    def __str__(self):
        s = "    0   1   2   3   4   5   6   7  " + "\n"
        s = s + "  ---------------------------------" + "\n"
        i = 0
        for row in self.board:
            s = s + str(i) +  " | "
            for loc in row:
                s = s + loc + " | "
            s = s + "\n"
            i = i + 1
        s = s + "  ---------------------------------"
        return s

    def print_history(self, display_board):
        hist = self.history
        self.__reset_board__()

        print "History of Game: "

        if display_board:
            print self;

        while hist:
            col, row = hist.pop(0)
            print self.turn + " plays at col: " + str(col) + " row: " + str(row)
            self.play(col, row)
            if display_board:
                print self
            

    def __switch_turn__(self):
        if self.turn == self.B:
            self.turn = self.W
        else:
            self.turn = self.B

    def play(self, col, row):
        if self.is_playable(col, row) == False:
            return
        for dir_col in range(-1, 2):
            for dir_row in range(-1, 2):
                if dir_col != 0 or dir_row != 0: #if moving to the contratry of not moving
                    if (self.is_flippable(dir_col, dir_row, col, row, self.turn)):
                        self.flip(dir_col, dir_row, col, row, self.turn)
        self.cur_moves = self.cur_moves + 1
        self.history.append((col, row))
        self.__switch_turn__()

    def get_possible_moves(self):
        playable = []

        for col in range(0, self.col):
            for row in range(0, self.row):
                if self.board[row][col] == " " and self.is_playable(col, row):
                    playable.append((col, row))
        return playable

    def is_playable(self, col, row):
        if self.out_of_bounds(col, row):
            return False
        if self.board[row][col] != " ":
            return False
        
        for dir_col in range(-1, 2):
            for dir_row in range(-1, 2):
                if dir_col != 0 or dir_row != 0:
                    if (self.is_flippable(dir_col, dir_row, col, row, self.turn)):
                        return True
        return False

    def game_finished(self):
        if self.cur_moves == self.BOARD_TOTAL_MOVES:
            return True
        return False
        
    def out_of_bounds(self, col, row):
        if col < 0 or row < 0 or col >= self.col or row >= self.row:
            return True
        return False

    def flip(self, dir_col, dir_row, start_col, start_row, tile):
        """TODO: Switch to internal function
           Should only be called after checked"""
        row = start_row
        col = start_col

        self.__flip_and_update__(col, row, tile)    #Flip the position they dropped
        row = row + dir_row
        col = col + dir_col

        while self.out_of_bounds(col, row) == False and self.board[row][col] != tile:
            """Do this while not out of bounds and haven't reached the sandiwch tile(The other bun"""
            self.__flip_and_update__(col, row, tile)
            row = row + dir_row
            col = col + dir_col

    def __flip_and_update__(self, col, row, tile):
        """Flip the current piece and update relevant attributes"""
        if self.board[row][col] == tile:
            return
        
        self.board[row][col] = tile
        if tile == self.B:
            self.score = self.score + 1
        else:
            self.score = self.score - 1

    def is_flippable(self, dir_col, dir_row, start_col, start_row, target):
        if target == self.W:
            jump = self.B     #the player to jump over
        else:
            jump = self.W

        row = start_row + dir_row
        col = start_col + dir_col

        if self.out_of_bounds(col, row) or self.board[row][col] != jump:
            return False

        while True:
            if self.out_of_bounds(col, row) or self.board[row][col] == " ":
                return False
            if self.board[row][col] == target:
                """Found Sandwich of tiles"""
                return True
            row = row + dir_row
            col = col + dir_col


def player_choice():
    correct_choice = True
    while correct_choice == True:
        print "Please select one of the following to start a game:"
        print "0 => Player vs Player"
        print "1 => Player vs Computer"
        print "2 => Computer vs Computer"

        choice = int(raw_input("Selection (0, 1, 2): "))
        if choice >= 0 and choice <= 2:
            correct_choice = False
    return choice

def PlayPlay(b_player, w_player):
    """TODO: RENAME this crap"""
    while game.game_finished() == False:
        print game
        b_player.play()
        print game
        w_player.play()    

def player_vs_player():
    #Doesn't matter which human player is currently white or black
    b_player = Hooman(game, game.B)
    w_player = Hooman(game, game.W)
    PlayPlay(b_player, w_player)

def player_vs_ai():
    #TODO: Figure who is First Player(Black) or Second Player(White)
    b_player = Hooman(game, game.B)
    ai = Greed_AI(game, game.W)  #TODO: Allow selecting AI
    w_player = Computer(game, game.W, ai)
    PlayPlay(b_player, w_player)       

def ai_vs_ai():
    return False

if __name__ == "__main__":
    print "Welcome to Othello Game"
    game = Othello()

    choice = player_choice()

    if choice == 0: #TODO replace this junk with a better design
        player_vs_player()
    elif choice == 1:
        player_vs_ai()
    else:
        ai_vs_ai()

    print "History of game:"
    game.history(False)

