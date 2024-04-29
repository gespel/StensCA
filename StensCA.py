import copy
import time
from random import random


def zufallszahl():
    if random() < 0.4:
        return 1
    else:
        return 0

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
                tmp.append(zufallszahl())
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
                if self.board[x-1][y-1] == 1:
                    out += 1
                if self.board[x-1][y+1] == 1:
                    out += 1
                if self.board[x+1][y-1] == 1:
                    out += 1
                if self.board[x-1][y+1] == 1:
                    out += 1
        return out

    def simulate(self):
        new = copy.deepcopy(self.board)
        for x in range(0, self.width):
            for y in range(0, self.height):
                n = self.get_neighbors_num(x, y)
                if self.board[x][y] == 0:
                    if n == 3:
                        new[x][y] = 1

                if self.board[x][y] == 1:
                    if n < 2:
                        new[x][y] = 0
                    if n == 2 or n == 3:
                        new[x][y] = 1
                    if n > 3:
                        new[x][y] = 0
        self.board = new

    def get_board(self):
        return self.board


s = StensCA(20, 40)

s.set_cell(4, 3, 1)
s.set_cell(5, 2, 1)
s.set_cell(6, 3, 1)
s.set_cell(7, 4, 1)
s.set_cell(4, 4, 1)
s.set_cell(5, 4, 1)
s.set_cell(5, 5, 1)
s.set_cell(6, 5, 1)
s.set_cell(4, 3, 1)
s.set_cell(3, 2, 1)
s.print_board()

while True:
    s.simulate()
    s.print_board()
    time.sleep(0.2)
