####API####
# push - add item to top
# pop - remove and return item from top
# peek - return top item
# size - return number of items
# is_empty - True if no items, False otherwise

def reverse_string(string):
    new_stack = Stack()
    for char in string:
        new_stack.push(char)
    rev = ""
    
    while(not new_stack.is_empty):
        rev += new_stack.peek()
        new_stack.pop()
    return rev

class Stack:
    def __init__(self):
        self._base = []
    
    def push(self, item):
        self._base.append(item)
        
    def pop(self):    
        return self._base.pop()
    
    def peek(self):
        return self._base[-1]
    
    @property
    def size(self):
        return len(self._base)
    
    @property
    def is_empty(self):
        return self._base == []
    
print(reverse_string("motor"))