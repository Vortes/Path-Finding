openList = []
closedList = []


class Cell:
    """Makes the cell, based Formula: f(n) = g(n) + h(n) for A* search"""
    def __init__(self, f, g, h):
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


def initCell(grid, row, column):
    for i in range(row):
        for j in range(column):
            grid[i][j] = Cell() #TODO: find a way to init this with the cell class


def main():
    game_board = Grid(5, 5)
    game_board.make_grid()
    game_board.get_grid()


main()








