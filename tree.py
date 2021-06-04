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

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        if self._parent is node:
            return
        if self._parent is not None:
            self._parent.remove_child(self)
        # then self.parentremove(self)
        # self.remove_child(node)
        self._parent = node
        if node is not None:
            node.add_child(self)

    def add_child(self, node):
        if node not in self._children:
            self._children.append(node)
            node.parent = self

    def remove_child(self, node):
        if node in self._children:
            self._children.remove(node)
            node.parent = None

    def depth_search(self, value):
        if self._value is value:
            return self
        for child in self._children:
            node = child.depth_search(value)
            if node is not None:
                return node
        return None

    def breadth_search(self, value):
        queue = [self]
        while len(queue) > 0:
            node = queue.pop(0)
            if node.value == value:
                return node
            elif node is not None:
                queue.extend(node.children)
        return None


node1 = Node("root1")
node2 = Node("root2")
node3 = Node("root3")

node3.parent = node1
node3.parent = node2

# print(node1.children)
# print(node2.children)

# brute force solutiuons
'''
def search(root):
    if root is None:
        return None
    visit(root) #adds root to visted list
    for Node in root.children:
        if !visited.includes(Node):
            search(Node
'''
'''
bfs(root):
    Queue queue = new Queue()
    root.marked = true
    queue.enque(root)
    while(!queue.isEmpty()):
        node r = queue.dequeue()
        visit(r)
        for node n in r.children:
            if(n.marked == false):
                n.marked = true
                queue.enqueue(n)
'''
