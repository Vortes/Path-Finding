class Node:
    """Makes the cell, based on Formula: f(n) = g(n) + h(n) for A* search"""
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.f = 0
        self.g = 0
        self.h = 0


def aStar(maze, start, end):
    start_node = Node(None, start)
    end_node = Node(None, start)

    open_list = []
    closed_list = []

    open_list.append(start_node)

    while open_list:
        current_node = open_list[0]
        current_index = 0

        for index, open_node in enumerate(open_list):
            if open_node.f < current_node.f:
                current_node = open_node
                current_index = index

        closed_list.append(current_node)
        open_list.pop(current_index)

        """
                 (-1,0)
                    N
        (1,0) NW    |     NE (-1,1)
                    |
   (0,-1) W - - - - | - - - - E (0,1)
                    |   
       (1,-1) SW    |     SE (1,1)    
                    S 
                  (1,0)
        """


def main():
    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # Start the A* Search Loop!


if __name__ == '__main__':
    main()








