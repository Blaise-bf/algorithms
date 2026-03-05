
class Node:

    def __init__(self, value):
        self.value = value
        self.adjecent_list = []
        self.visited = False # important for graph traversal in a an undirected graph


class Graph:
    
    def bfs(self, node):
        queue = []
        queue.append(node)
        node.visited = True
        traversal = []
        while queue:
            current = queue.pop(0)

            traversal.append(current.value)
            for neighbors in current.adjecent_list:
                if not neighbors.visited:
                    queue.append(neighbors)
                    neighbors.visited = True
        return traversal
    def dfs(self, node, traversal):
        node.visited = True
        traversal.append(node.value)
        for element in node.adjecent_list:
            if element.visited is False:
                self.dfs(element, traversal)
        return traversal



# Sample usage
# A: B C D
if __name__ == "__main__":
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")
    node1.adjecent_list.extend((node2, node3, node4))
    node2 .adjecent_list.extend((node1, node5, node6))
    node3.adjecent_list.append(node1)
    node4.adjecent_list.extend((node1, node7))
    node5.adjecent_list.append(node2)
    node6.adjecent_list.append(node2)
    node7.adjecent_list.append(node4)

    graph = Graph()
    print(graph.bfs(node1))
    
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")
    node8 = Node("H")
    node1.adjecent_list.extend((node2, node3, node4))
    node2 .adjecent_list.extend((node1, node5, node6))
    node3.adjecent_list.append(node1)
    node4.adjecent_list.extend((node1, node7))
    node5.adjecent_list.append(node2)
    node6.adjecent_list.extend((node2, node8))
    node7.adjecent_list.append(node4)

    print(graph.dfs(node1, traversal=[]))



    

