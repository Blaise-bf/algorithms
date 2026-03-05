from collections import deque
search_queue = deque()
graph = {}

graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

search_queue += graph['you']

def person_is_seller(name):
    return name[-1] == 'm'




def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = set()
    while search_queue:

        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f'{person} is a mango seller!')
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    return False
for i in range(1, 2):
    print(i)
