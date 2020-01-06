class Node:
    """Makes the cell, based on Formula: f(n) = g(n) + h(n) for A* search"""
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.f = 0
        self.g = 0
        self.h = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    start_node = Node(None, start)
    end_node = Node(None, end)

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

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        children = []

        """
                     (-1,0)
                        N
            (-1,-1) NW    |     NE (-1,1)
                        |
       (0,-1) W - - - - | - - - - E (0,1)
                        |   
           (1,-1) SW    |     SE (1,1)    
                        S 
                      (1,0)
        """

        for pos in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
            node_coord = (current_node.position[1] + pos[1],  # x
                          current_node.position[0] + pos[0])  # y

            x_less_than_zero = node_coord[1] < 0
            y_less_than_zero = node_coord[0] < 0
            x_bigger_than_maze = node_coord[1] > (len(maze[len(maze)-1]) - 1)
            y_bigger_than_maze = node_coord[0] > len(maze) - 1

            if x_less_than_zero or y_less_than_zero or x_bigger_than_maze or y_bigger_than_maze:
                continue
            if maze[node_coord[0]][node_coord[1]] == 1:
                continue

            compatible_node = Node(current_node, node_coord)
            children.append(compatible_node)

        for child in children:
            for closed_nodes in closed_list:
                if child == closed_nodes:
                    continue

            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            open_list.append(child)


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

    start = (0, 0)
    end = (7, 6)

    path = astar(maze, start, end)
    print(path)


if __name__ == '__main__':
    main()