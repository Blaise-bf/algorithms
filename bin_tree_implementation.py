class Node:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def peek(self):
        if not self.is_empty():
            return self.items[0].value




class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)
    def pre_order_traversal(self, start, traversal: list):
        # Pre-order traversal: root -> left -> right
        if start:
            traversal.append(start.value)
            self.pre_order_traversal(start.left, traversal)
            self.pre_order_traversal(start.right, traversal)
        return traversal
    def in_order_traversal(self, start, traversal: list):
        # In-order traversal: left -> root -> right
        if start:
            self.in_order_traversal(start.left, traversal)
            traversal.append(start.value)
            self.in_order_traversal(start.right, traversal)
        return traversal
    def post_order_traversal(self, start, traversal:list):
        # Post-order traversal: left -> right -> root
        if start:
            self.post_order_traversal(start.left, traversal)
            self.post_order_traversal(start.right, traversal)
            traversal.append(start.value)
        return traversal
    def level_order_traversal(self, start):
        # Level-order traversal (Breadth First Search)
        if not start:
            return []
        traversal = []
        queue = Queue()
        queue.enqueue(start)
        
        while queue.size() > 0:
            traversal.append(queue.peek())
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                
                queue.enqueue(node.right)
        return traversal



tree = BinaryTree(3)
tree.root.left = Node(4)
tree.root.right = Node(5)

tree.root.left.left = Node(6)
tree.root.left.right = Node(7)
tree.root.right.left = Node(8)
tree.root.right.right = Node(9)
print(tree.pre_order_traversal(tree.root, []))
print(tree.in_order_traversal(tree.root, []))
print(tree.post_order_traversal(tree.root, []))
print(tree.level_order_traversal(tree.root))
