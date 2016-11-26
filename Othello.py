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
    row = 8
    col = 8
    BOARD_TOTAL_MOVES = row * col    
    cur_moves = 0
    
    def __init__(self):
        print "Othello start"
        self.__reset_board__()
        self.turn = self.B

    def __reset_board__(self):
        self.board = [[' ' for x in range(self.col)] for y in range(self.row)]
        self.board[3][3] = self.B
        self.board[4][4] = self.B
        self.board[3][4] = self.W
        self.board[4][3] = self.W
        self.cur_moves = 4

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


    def is_playable(self, col, row):
        if self.out_of_bounds(col, row):
            return False
        if self.board[row][col] != " ":
            #raise IndexError("Key Already There")
            return False
        
        for dir_col in range(-1, 2):
            for dir_row in range(-1, 2):
                if dir_col != 0 or dir_row != 0:
                    if (self.is_flippable(dir_col, dir_row, col, row, self.turn)):
                        return True
        return False

    def end_game(self):
        if self.cur_moves == self.BOARD_TOTAL_MOVES:
            return True
        return False

    def winner(self):
        score = 0

        if self.end_game() == False:
            return #Can't determine winner yet.
        
        for row in range(0, 8):
            for col in range(0, 8):
                if self.board[row][col] == self.W:
                    score = score + 1
                else
                    score = score - 1
        if score > 0:
            return self.W
        elif score < 0 :
            return self.B
        return "T"  #Tie
        
    def out_of_bounds(self, col, row):
        if col < 0 or row < 0 or col >= self.col or row >= self.row:
            return True
        return False

    def flip(self, dir_col, dir_row, start_col, start_row, tile):
        row = start_row
        col = start_col

        self.board[row][col] = tile

        while self.out_of_bounds(col, row) == False and self.board[row][col] != " ":
            self.board[row][col] = tile
            row = row + dir_row
            col = col + dir_col

    def is_flippable(self, dir_col, dir_row, start_col, start_row, target):
        if target == self.W:
            jump = self.B
        else:
            jump = self.W

        row = start_row + dir_row
        col = start_col + dir_col

        if self.board[row][col] != jump:
            return False

        while True:
            if self.out_of_bounds(col, row):
                return False
            if self.board[row][col] == " ":
                return False
            if self.board[row][col] == target:
                """Found Sandwich of tiles"""
                return True
            row = row + dir_row
            col = col + dir_col
    

x = Othello()
print x


