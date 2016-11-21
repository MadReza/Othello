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
        if self.board[col][row] != " ":
            #raise IndexError("Key Already There")
            return False

    def is_playable(self, col, row):
        if out_of_bounds(col, row):
            return False
        if self.board[col][row] != " ":
            #raise IndexError("Key Already There")
            return False
        
    def out_of_bounds(self, col, row):
        if col < 0 or row < 0 or col >= self.col or row >= self.row:
            return True
        return False
    
    def is_flippable(self, dir_col, dir_row, start_col, start_row, target):
        if target == self.W:
            jump = self.B
        else:
            jump = self.W

        row = start_row + dir_row
        col = start_col + dir_col

        if self.board[col][row] != jump:
            return False

        while True:
            if self.out_of_bounds(col, row):
                return False
            if self.board[col][row] == target:
                return True
            if self.board[col][row] == " ":
                return False
            row = row + dir_row
            col = col + dir_col
    

x = Othello()
print x
print x.is_flippable(-1, 0, 5, 3, "B")
print x.is_flippable(0, -1, 3, 5, "B")
print x.is_flippable(0, 1, 3, 2, "W")
    
