class Node:
    def __init__(self, value):
        self._parent = None
        self._children = []
        self._value = value

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children
# input needed

    @property
    def parent(self, node):
        self._parent = node
        self.add_children(node)

    @parent_getter
    def parent(self):
        return self._parent
# input unneeded

    def add_children(self, node):
        if not node in self._children:
            self._children.append(node)
            node._parent = self

    def remove_child(self, node):
        self._children.remove(node)
        node._parent = None
