# Example of Linked List implementation and methods
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        print(f"'{data}' inserted at the beginning.")

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        print(f"'{data}' inserted at the end.")

    def search(self, target):
        current_node = self.head
        while current_node:
            # Compare the data inside the node, not the node object itself
            if current_node.data == target:
                print(f"Item: '{target}' found!")
                return True
            current_node = current_node.next

        print(f"Item: '{target}' not found in the list.")
        return False

    def __str__(self):
        # Bonus: A way to visualize your list easily
        nodes = []
        curr = self.head
        while curr:
            nodes.append(str(curr.data))
            curr = curr.next
        return " -> ".join(nodes)

    def remove_at_beginning(self):
        if not self.head:
            print("List is empty, nothing to remove.")
            return None

        removed_data = self.head.data
        # Move the head pointer to the next node
        self.head = self.head.next

        # If the list is now empty, we must also set the tail to None
        if self.head is None:
            self.tail = None

        print(f"Removed '{removed_data}' from the beginning.")
        return removed_data

    def remove_at_end(self):
        if not self.head:
            print("List is empty, nothing to remove.")
            return None

        removed_data = self.tail.data

        # Case 1: Only one item in the list
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            # Case 2: Multiple items. We need to find the second-to-last node.
            current = self.head
            while current.next != self.tail:
                current = current.next

            # 'current' is now the second-to-last node
            current.next = None
            self.tail = current

        print(f"Removed '{removed_data}' from the end.")
        return removed_data

# Example of the functions
sushi_preparation = LinkedList()
sushi_preparation.insert_at_end("prepare")
sushi_preparation.insert_at_end("roll")
sushi_preparation.insert_at_beginning("assemble")

sushi_preparation.search("roll")
sushi_preparation.search("mixing")

