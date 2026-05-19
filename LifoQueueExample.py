# LifoQueue Example
import queue

my_book_stack = queue.LifoQueue(maxsize=0)
my_book_stack.put("The misunderstanding")
my_book_stack.put("Persepolis")
my_book_stack.put("1984")

print("The size: ",my_book_stack.qsize())

print(my_book_stack.get())
print(my_book_stack.get())
print(my_book_stack.get())

print("Empty Stack:",my_book_stack.empty())