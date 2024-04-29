import copy
import time


class StensCA:
    height = 10
    width = 10
    board = []

    def __init__(self, width, height):
        self.height = height
        self.width = width
        for i in range(0, self.width):
            tmp = []
            for j in range(0, self.height):
                tmp.append(0)
            self.board.append(tmp)

    def print_board(self):
        for column in self.board:
            for row in column:
                print(row, end="")
            print()
        print()

    def set_cell(self, x, y, value):
        self.board[x][y] = value

    def get_neighbors_num(self, x, y):
        out = 0
        if 0 < x < self.width-1:
            if 0 < y < self.height-1:
                if self.board[x-1][y] == 1:
                    out += 1
                if self.board[x+1][y] == 1:
                    out += 1
                if self.board[x][y-1] == 1:
                    out += 1
                if self.board[x][y+1] == 1:
                    out += 1
        return out

    def simulate(self):
        new = copy.deepcopy(self.board)
        for x in range(0, self.width):
            for y in range(0, self.height):
                n = self.get_neighbors_num(x, y)
                if n == 2 or n == 1:
                    new[x][y] = 1
                else:
                    new[x][y] = 0
        self.board = new

    def get_board(self):
        return self.board


s = StensCA(20, 40)

s.set_cell(4, 3, 1)
s.set_cell(5, 2, 1)
s.set_cell(6, 3, 1)
s.set_cell(7, 4, 1)
s.print_board()

while True:
    s.simulate()
    s.print_board()
    time.sleep(0.05)
