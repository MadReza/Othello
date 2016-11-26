print "Othello Start"

print "Display: "

print "________________"
print "[ O | O | O | O ]"
print "[ 0 | W | B | O ]"
print "[ 0 | B | W | O ]"
print "[ O | O | O | O ]"
print "________________"

class Othello:
    """Othello Game Engine"""

    W = "W"
    B = "B"
    row = 8     #Eventually upgrade to adjustable board
    col = 8
    BOARD_TOTAL_MOVES = row * col    
     
    
    def __init__(self):
        print "Othello start"
        self.__reset_board__()

    def __reset_board__(self):
        self.board = [[' ' for x in range(self.col)] for y in range(self.row)]
        self.board[3][3] = self.B
        self.board[4][4] = self.B
        self.board[3][4] = self.W
        self.board[4][3] = self.W
        self.cur_moves = 4
        self.history = ()   #Takes Tuples of (x,y) values with Black be first
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
                if dir_col != 0 or dir_row != 0:
                    if (self.is_flippable(dir_col, dir_row, col, row, self.turn)):
                        self.flip(dir_col, dir_row, col, row, self.turn)
        self.cur_moves = self.cur_moves + 1
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
        row = start_row
        col = start_col

        self.__flip_and_update(row, col, tile)

        while self.out_of_bounds(col, row) == False and self.board[row][col] != " ":
            self.__flip_and_update(row, col, tile)
            row = row + dir_row
            col = col + dir_col

    def __flip_and_update__(self, row, col, tile):
        """Flip the current piece and update relevant attributes"""
        self.board[row][col] = tile
        if tile == self.B:
            self.score = self.score + 1
        else:
            self.score = self.score - 1

    def is_flippable(self, dir_col, dir_row, start_col, start_row, target):
        if target == self.W:
            jump = self.B
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
    

x = Othello()
print x
print x.get_possible_moves()


