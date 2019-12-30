openList = []
closedList = []


class Cell:
    """Makes the cell, based Formula: f(n) = g(n) + h(n) for A* search"""
    def __init__(self, f=0, g=0, h=0):
        self.f = f
        self.g = g
        self.h = h


class Grid:
    """Makes the game board

    Attributes:
        make_grid -- A 2D array with rows and columns specified by user
        get_grid -- Returns the 2D array with formatting
    """
    grid = []

    def __init__(self, row, column):
        self.row = row
        self.column = column

    def make_grid(self):
        for i in range(self.row):
            self.grid.append([])
            for j in range(self.column):
                self.grid[i].append(0)
        return self.grid

    def get_grid(self):
        for i in range(self.row):
            print()
            for j in range(self.column):
                print(self.grid[i][j], end=' ')

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column


def initCell(game_board, row, column):
    for i in range(row):
        for j in range(column):
            if i == 0 and j == 0:
                game_board[0][0] = 0
            else:
                game_board[i][j] = Cell()

    return game_board


def main():
    grid = Grid(5, 5)
    game_board = grid.make_grid()
    game_board = initCell(game_board, grid.get_row(), grid.get_column())
    start = game_board[0][0]
    end = game_board[-1][-1]

    openList.append(start)

    # Start the A* Search Loop!
    while openList:



main()








