# #  Complete implementation of a Queue Class
#
# class Queue:
#     def __init__(self):
#         self.queue = []
#
#     def enqueue(self, data):
#         self.queue.append(data)
#
#     def dequeue(self): # Function used to remove the first item of the queue
#         if self.is_empty():
#             return "Queue is Empty"
#         return self.queue.pop(0)
#
#     def peek(self): # This function is used to see the first element that will be removed within a queue
#         if self.is_empty():
#             return "Queue is Empty"
#         return self.queue[0]
#
#     def is_empty(self): # Function to see if a queue is empty
#         return len(self.queue) == 0
#
#     def size(self): # Function to see the six
#         return len(self.queue)
#
# # Corrected class instantiation
# myQueue = Queue()
#
# myQueue.enqueue('A')
# myQueue.enqueue('B')
# myQueue.enqueue('C')
#
# print("Queue: ", myQueue.queue)
# print("Peek: ", myQueue.peek())
# print("Dequeue: ", myQueue.dequeue())
# print("Queue after Dequeue: ", myQueue.queue)
# print("isEmpty: ", myQueue.is_empty())
# print("Size: ", myQueue.size())

# Node class
class Node:
    def __init__(self,data):
        self.data = None
        self.next = None

# Queue Class
class Queue:
    # init
    def __init__(self,data):
        self.head = None
        self.tail = None

    # Enqueue class
    def enqueue(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next =new_node
            self.tail =new_node

    def dequeue(self):
        if self.head:
            current_node = self.head
            self.head = current_node.next
            current_node.next = None

        if self.head == None:
            self.tail = None
