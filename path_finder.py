from tree import Node


class KnightPathFinder:
    def __init__(self, start_pos=()):
        # Creating an instance variable, self._root

        # self.postion = Node(start_position)
        self._root = Node(start_pos)
        self._considered_positions = set(start_pos)

# (x,y) = pos
# (x,y) = possible_move
# when we return, for another starting postion ,
    def get_valid_moves(self, pos):
        possible_moves = [
            (1, 2),
            (1, -2),
            (2, 1),
            (-2, 1),
            (-1, 2),
            (-1, -2),
            (-1, -2),
            (-2, -1),
        ]
        return possible_moves


finder = KnightPathFinder((0, 0))
