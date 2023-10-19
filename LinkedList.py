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

    def __str__(self):
        return f"{self.value}"
class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        old_node = self.head
        self.head = new_node
        self.head.next = old_node
                
    def search(self, value):
        current_node = self.head
        
        while current_node is not None:
            if current_node.value == value:
                return current_node
            current_node = current_node.next
            
        return None    
    
    def remove(self, value):
        # check if head is the value
        if self.head.value == value:
            #set next node as head
            self.head = self.head.next

            #set current nodes next to None
            current_node = None
            return True
        # we know head is not the value
        current_node = self.head
        # check all nodes for value
        while current_node is not None:
            if current_node.next.value == value:

                # set current node next to the next next
                current_node.next = current_node.next.next

                return
            
            current_node = current_node.next
    
    def size(self):
        current_node = self.head
        counter = 0
        while current_node is not None:
            counter += 1
            current_node = current_node.next
            
        return counter
    
    def is_empty(self):
        return self.size() == 0
    
    def display(self):
        current_node = self.head
        node_str = ""
        while current_node is not None:
            node_str += str(current_node.value)
            node_str += "=>"
            current_node = current_node.next
        node_str += "None"
        print(node_str) 
    
# []

new_list = LinkedList()  
new_list.insert(12)
new_list.insert(13)
new_list.insert(14)
new_list.insert(15)
new_list.insert(16)


new_list.display()

print(new_list.size())