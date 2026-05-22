# Example of working with stacks

class Stack:
    def __init__(self):
        self.top = None

    # Adding an item to a stack
    def push(self,data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node

    # Removing an item from a stack
    def pop(self,data):
        # If stack is empty we return none
        if self.top is None:
            return None
        # If stack has items we remove the top item and set the item beneath the top item as the top item
        else:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data

    # Peeking in stacks, returns the data of the last element, but does not alter the stack
    def peek(self,data):
        if self.top:
            return self.top.data
        else:
            return None

