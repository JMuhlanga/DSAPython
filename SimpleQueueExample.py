# SimpleQueue Example
import queue

# Instantiating of a queue
order_queue = queue.SimpleQueue()

# Adding elements to the queue
order_queue.put("Sushi")
order_queue.put("Lasagna")
order_queue.put("Paella")

# Printing the size of the queue
print("The size of the queue is: ",order_queue.qsize())

# To remove elements in the queue, prints removed elements
print(order_queue.get())
print(order_queue.get())
print(order_queue.get())

# To check if the queue is empty and prints
print("Empty queue: ",order_queue.empty())
