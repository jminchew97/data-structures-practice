####API####
# enqueue - add item to beginning
# dequeue - remove and return item from end
# peek - return last item
# size - return number of items
# is_empty - True if no items, False otherwise

class Queue:
    def __init__(self):
        self._base = []
    
    def enqueue(self, item):
        self._base.insert(0, item)
    
    def dequeue(self):
        return self._base.pop()
    
    def peek(self):
        if self._base:
            return self._base[0]
        return None
    
    def size(self):
        return len(self._base)
    
    def is_empty(self):
        return self._base == []
    
q = Queue()
