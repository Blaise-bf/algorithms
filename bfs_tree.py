from os import listdir

from os.path import isfile, join
from collections import deque


def print_tree(root: str):

    search_queue = deque()
    search_queue.append(root)
    while search_queue:
        dir = search_queue.popleft()

        for file in sorted(listdir(dir)):
            if isfile(join(dir, file)):
                print(file)
            else:
                search_queue.append(join(dir, file))



def print_tree_recursive(root: str):

    for file in sorted(listdir(root)):
        full_path = join(root, file)

        if isfile(full_path):
            print(file)
        else:
            print_tree_recursive(full_path)
