class Node:
    def __init__(self, value: int = None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert(self, value):
        pass 

    def delete(self, value):
        pass

    def search(self, value):
        pass

    def get(self, value):
        pass


n1 = Node(value=3)
n2 = Node(value=7)
n3 = Node(value=7)
n4 = Node(value=9)

LL = LinkedList()

LL.head = n1

n1.next = n2 

n2.next = n3

n3.next = n4

print(id(n1))

print(id(n2))
