####API####
# insert - add node to beginning (or end)
# search - find and return a given node
# remove - remove a given node
# size - return number of nodes
# is_empty - True if no nodes, False otherwise


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    