from collections import deque

def person_is_seller(name):
    return name[-1] == 'h'

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph['thom'] = ["mitch"]
graph["jonny"] =[]
graph["mitch"] = []

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = [] # Keep track of peole youve searched before
    while search_queue:
        person = search_queue.popleft()
        # Only search this person if you haven't already searched them
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller")
                return True
            else:
                search_queue += graph[person]
                # Mark this person as serached
                searched.append(person)
                
    return False
search("you")