from tree import Node


class KnightPathFinder:
    def __init__(self, start_pos=()):
        # Creating an instance variable, self._root

        # self.postion = Node(start_position)
        self._root = Node(start_pos)
        self._considered_positions = {start_pos}

# (x,y) = possible_move
# when we return, for another starting postion ,
    def get_valid_moves(self, pos):
        possible_moves = [
            (pos[0] + 1, pos[1] + 2),
            (pos[0] + 1, pos[1] - 2),
            (pos[0] + 2, pos[1] + 1),
            (pos[0] + 2, pos[1] - 1),
            (pos[0] - 1, pos[1] + 2),
            (pos[0] - 1, pos[1] - 2),
            (pos[0] - 2, pos[1] + 1),
            (pos[0] - 2, pos[1] - 1),
        ]
        valid_moves = [(x, y) for x, y in possible_moves if x in range(
            0, 8) and y in range(0, 8)]

        # x, y = pos
        # for x, y in possible_moves:
        #     new_pos = (x, y)
        #     new_x, new_y = new_pos
        #     if new_x in range(0, 9) and new_y in range(0, 9):
        #         valid_moves.append((new_x, new_y))
        return valid_moves

    def new_move_positions(self, pos):
        v_moves = set(self.get_valid_moves(pos))
        # return v_moves
        new_moves = v_moves.difference(
            self._considered_positions)
        self._considered_positions = self._considered_positions.union(
            new_moves)
        return new_moves

    def build_move_tree(self):
        root = self._root
        queue = [root]
        while len(queue) > 0:
            curr_node = queue.pop(0)
            new_moves = self.new_move_positions(curr_node.value)
            for move in new_moves:
                child = Node(move)
                curr_node.add_child(child)
                queue.append(child)

    def trace_to_root(self, ending_node):
        path = []
        pointer = ending_node
        while pointer is not None:
            path.append(pointer.value)
            if pointer.parent is not None:
                pointer = pointer.parent
            else:
                return
        return path.reverse()


finder = KnightPathFinder((0, 0))
finder.build_move_tree()
print(finder._root.children)
# print(finder.get_valid_moves((4, 4)), "💛")
# print(finder.new_move_positions((0, 0)), '🙂')
