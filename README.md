# DSA IN PYTHON 

- DSA Helps in problem solving as well as making it easy to make efficient code 
- Algorithm is a set of instructions that solve a problem
- Data Structures hold and manipulate data when we execute an algorithm

## Linked lists
- A linked list is a sequence of data connected through links
- Each linked list has an item called a node 
- A node has 2 parts
- The first part is the data and the second part is the pointer to the next node 
- The last link points to null
- The first node is the head 
- The final node is the tail 
- The data does not need to be stored in continuous blocks of memory so it can be located in any available memory address
- If each node has one link it is called a singly linked list 
- If each node has two links in either direction it is called a doubly linked list 
- Linked lists can be used to implement other data structures such as [stacks, queues,graphs]
- A common application of linked list is :
- -Access information by navigating backwards and forwards such as a web browser, music playlist
- Linked list methods include :
- - [insert_at_beginning()]
- - [remove_at_beginning()]
- - [insert_at_end()]
- - [remove_at_end()]
- - [insert_at()]
- - [remove_at()]
- - [search()]

## Big O Notation
- This is a tool used to explain the complexity of Algorithms
- Measures the worst case complexity of an algorithm
- - Time Complexity: time taken to run completely
- - Space Complexity : extra memory Space required by an algorithm
- Does not use seconds/bytes because:
- - Different results depending on the hardware
- Mathematical Expressions: O(1), O(n), O(n*n)...
- An increase in the input size of an algorithm increases the number of executed operations
- For algorithms of O(1) , the number of operations remains constant even if the input size changes, it has constant time 
- O(n) follows a linear path , the number of operations increases proportionally with the number of input
- O(log n) has logarithmic time complexity
- o(n*n) O of n squared is called quadratic time
- o(n*n*n) O of n cubed is called cubic time 
- The number of operations increases by alot when we increase the input
- We simplify Big-O-Notaion by:
- - We simplify by removing constants - O(4 + 2n + 2m) -> O(n + m)
- - Different variables for different inputs - O(n+m)
- - Remove Smaller terms by keeping the one that keeps increasing faster

## Working with Stacks
- Stacks use the principle of LIFO(Last-In-First-Out)
- Meaning the last item inserted is the first item to be removed
- For example adding a book is done on the top of a stack which is known as {push}pushing to the stack
- We can only take from the top of a stack which is also called {pop}popping from a stack
- We can only read the last statement which is also called {peek}peeking from a stack
- Stack real uses:
- - Undo functionality
- - - We {push} each item using a keystroke when typing 
- - - We {pop} the last keystroke
- - Symbol Checker ([{}])
- - - we {push} the opening symbols
- - - we {check} closing symbol
- - - we {pop} matching opening symbol
- - Function calls:
- - - we {push} a block of memory
- - - we {pop} after the execution ends
- We implement stacks using a singly linked list
- Instead of creating from scratch each time, we can leverage the LifoQueue class from Pythons Queue Model
- - LifoQueue behaves lika a stack:
- - - We start by first importing the queue inbuilt class
- - - We then by declaring the size of the stack,0 is infinite
- - - We add by using {.put()} which typically adds at the top of the stack
- - - We remove by using {.get()} which typically removes from the top of the stack

## Working with Queues in Python
- A queue in python is a data structure that follows the FIFO(First-In-First-Out) principle
- Meaning that the first item added is the first item removed from the list
- The beginning of the queue is called the head and the last item is called the tail
- Items are typically added to the end of a queue, items inserted at the end of the queue in an operation called enqueue
- Other kinds of queues include ->  Doubly ended queues, Circular queues, Priority Queues
- The basic operations we can do for a queue are:
- - {Enqueue} Adding an element to the queue
- - {Dequeue} Removes and returns the first element of the queue
- - {peek} Returns the first element of the queue
- - {isEmpty} Checks if the queue is empty
- - {size} Finds the number of items in the queue
- Queues can be implemented using arrays or linked lists
- Example of implementation of queues:
- - Job Scheduling for an office printer -> Documents are printed in the order they are received
- - Order processing of E-tickets
- - Create Algorithms for Breadth-First search in graphs
- - Applications where the order of requests matters such as tickets, taxi services
- Queues are similar to stacks can be implemented using singly linked lists

## Working with Hash Tables
- A Hash table is a data structure that stores a collection of items in key value pairs. for example:
- - lasagna: 14.75
- - moussaka: 21.15
- - sushi: 16.05
- In the above examples they are in {key:value} format.
- Almost every programming language has a built-in Hash table known as [hashes,hash maps,dictionaries,associative arrays]
- In Python, they are known as dictionaries
- Structure:
- - In a hash table each position is called a a slot or bucket
- - When we create a Hash table each slot will be empty
- - When we add an element to a hash table, there will be a mapping between the key and the slot where the value will be stored
- - Mapping will be performed thanks to a Hash function
- - Everytime a hash function is applied, it must return the same value for the same input
- - When we need to find a value associated with a key we need to hash the key and then look inside the corresponding slot to return the stored value
- - The operation above takes O(1)
- Sometimes Hash functions can return the same output for different inputs 
- Suppose we have already inserted a value for a certain key, when we want to insert another value for that particular key we will have a collision, collisions must be resolved
- Python Hash tables are called Dictionaries
- - An Empty dictionary will be defined as [my_empty_dictionary = {}]
- - If we do not have a key we will get an error
- - We can check if an item exists using the [.get()] method
- - To get all items of a dictionary using the [.items()] method
- - To get all keys in the dictionary we use the [.keys()] method
- - To get all the values in a dictionary we use the [.values()] method
- - To add a new key value pair we need to specify the new key with its value i.e [my_dictionary['new_Key'] = new_value ]
- - To modify the value of a particular key we need to specify it and assign a new desired value [my_dictionary['existing_key'] = new_value]
- - To delete a dictionary completely we use the [del] keyword [del my_dictionary], and to remove a key value pair we [del my_dictionary['dict_key']]
- - To empty a dictionary we use the [.clear()] method i.e [my_dictionary.clear()]
- - We can iterate over a dictionary using a for loop for each item i.e
- - - {
        for key, value in my_menu.items():
            print(f"\nkey:{key} ")
            print(f"value:{value} ")
    }
- - A dictionary can be nested within another dictionary
- - - {
  - key:{
    - key:value
    - }
  - }

## Working with Trees and graphs
- Trees are node based data structures where each node can have links to more than one node
- - The first node of a Tree is known as a Root
- - A node can be the parent of other nodes which are called children
- - Trees have levels, which are basic representation of descendants for example, the Root is normally the first level
- - A Binary Tree is a Tree in which each node has zero, one or two children
- - Trees have many application such as:
- - - Storing Hierarchical relationships such as the file system of a computer, structure of a HTML Document,
- - - Storing the possible moves of a rival in Chess
- - - Searching and sorting algorithms
- A Graph is a data structure formed by a set of nodes also called vertices, the nodes are connected by links called edges
- - They can represent a social network
- - Trees are a type of graph
- - Graphs can be directed when they have one specific direction
- - Graphs can also be undirected when the edges have no direction we assume the relationship is mutual
- - Weighted Graphs have numeric values associated with the edges, these Graphs can be either directed or undirected 
- Differences between Trees and Graphs
- - Trees cannot have cycles, meaning nodes cannot reference each other circularly, while Graphs can have cycles
- - In a Tree all nodes must be connected while in Graphs there can be unconnected nodes
- Graphs can represent:
- - User relationships in social networks -> Friendship, Follows, Likes, etc
- - Location and distances -> Route optimization
- - Graph databases can be used to store the information that is consumed by lots of applications
- - Just like Trees they appear in most search and sort algorithms 
- Graphs will have a dictionary to store all vertices
- Vertices can be added with the [add_vertex] method and Edges with the [add_edge] method

## Recursion
- Recursion is the term used to refer to a function calling itself
- In almost all situations where we use loops we can substitute loops with recursion
- Can solve problems that seem very complex at first
- To avoid infinite recursion we first have to identify the base case by:
- - Add a condition to ensure that algorithm does not execute forever
- Computer uses stack to keep track of the functions known as the [call stack]
- Dynamic programming is an optimization technique mainly applied to recursion, it can reduce the complexity of recursive algorithms
- - Can be used for any problem that can be divided into smaller subproblems
- - Can also be used for subproblems overlap
- - Solutions of subproblems are saved, avoiding the need to recalculate - memorization technique

## Linear Search and Binary Search
- Searching is an essential operation
- Linear search tries to search for a value by looping through each element in a list if element is found, algorithm stops and returns result, otherwise algorithm continues
- Linear Search has a complexity of O(n)
- Binary Search only applies to ordered lists
- The complexity of a binary search is O(log n) which is better than the linear search complexity especially when the size of the list is big

## Binary Search Tree
- In a Binary search Tree:
- - The left subtree of a node contains only nodes with values less than the node itself
- - The right subtree contains nodes with values greater than the node 
- - The left and right subtrees must be binary search trees
- Used to order lists efficiently
- Much faster at searching than arrays and linked lists
- Much faster at inserting and deleting than arrays or linked lists
- Used to implement more advanced data structures like dynamic sets, lookup tables, priority queues
- Deleting In BST:
- - If the node we want to delete has no children we delete it
- - If the node has one child , we delete the node and connect the child with the node's parent.
- - If the node we are deleting has two children we replace it with its successor
- - The successor is the node with the smallest value greater than the value of the node we want to delete
- - To find the successor we visit the right child of the node being deleted and keep visiting its left nodes until the end then we replace the node with its successor
- - If the successor has a right child, this child becomes the left child of the successors parent

## Depth First Search
- Traversal is the process of visiting all nodes of a tree or a graph this can be performed with depth first search or breadth first search
- There are 3 ways of traversing a binary tree [in-order,pre-order,post-order]
- In-order traversal:
- - Order : Left -> Current -> Right
- - Traverses the left subtree of the current node, followed by the current node and finally the right subtree
- - Starting from the root, we move to the roots left child and continue until there is no left child and since it has no left child, we move backwards we then move to the right node,after that has no children we go backwards, repeating the same steps for the right subtree
- - The complexity is O(n) where n is the number of nodes
- - Commonly used in binary search trees to obtain the nodes values in ascending order
- Pre-order traversal:
- - Order: Current -> Left -> Right
- - First visits the current node then traverses the left subtree and finally the right subtree
- - The complexity is O(n) where n is the number of nodes
- - Used to create copies of a tree and get prefix expressions
- Post-order traversal:
- - Order: Left -> Right -> Current
- - First traverses the current nodes left subtree then the right subtree and finally visits the current node 
- - Also has O(n) complexity
- - Used to delete binary trees and get postfix expressions
- Since graphs can have cycles we need:
- - To keep track of visited vertices
- - Steps:
- - - The algorithm starts at any vertex
- - - Tracks current vertex to visited vertices list
- - - For each node current adjacent vertex if it has been visited ignore it, if it has not we recursively perform depth first search
- - The complexity of this algorithm is O(V + E) where V represents the number of vertices and E the number of Edges

## Breadth First Search
- Starts from the root and visits every node of every tree level before going on to the next level
- Complexity is O(n) where n is the number of nodes for BSTs
- Since Graphs can have cycles, we need to check if the vertices have already been visited 
- Complexity is O(V+E) for graphs where V is the number of vertices and E is the number of Edges

### BFS vs DFS
- If target is close to the starting vertex, bfs will be more applicable
- Some applications of BFS are web crawling, Finding the shortest path in unweighted graphs, finding connected locations using gps
- If target is far away from the starting vertex dfs becomes more applicable 
- Some applications of DFS are solving puzzles with only one solution i.e Mazes, Detecting cycles in graphs
- Both are used in more complex algorithms

## Bubble Sort Algorithms
- Solve how to sort an unsorted collection in ascending/ descending order 
- Important as they can reduced the complexity of problems 
- Some sorting algorithms include bubble sort, selection sort, insertion sort, merge sort,quicksort
- In bubble sort we start comparing the first 2 values of the collection
- If the first value is greater than the second one we swap them otherwise we do nothing, then proceed to the next two item pairs
- Once we complete the collection we then start again from the beginning and repeat the same steps, we do this again and again until its sorted
- In the example the outer loop will iterate as many times as the length of the list on each iteration the inner loop will iterate as many times as the length of the list minus the variable i, we subtract i to avoid checking the already sorted values that are at the end of the list
- In the inner loop we will compare the adjacent elements and swap them if the first one is greater than the second one 
- Then we start again while the i variable reaches the end 
- At the end of execution we return the sorted list
- Both functions have a complexity of O(n * n) worst case scenario
- Best case when the list is almost sorted will be Omega(n*n) in the not improved version
- In the improved version it will be Omega(n)
- Average case will be Theta(n*n)
- Does not perform well with highly unsorted large lists, performs better if the list large and sorted or almost sorted
- Performs well in small lists 

## Selection Sort  & Insertion sortAlgorithms
- We start at the beginning of the list until the end of the list determining the lowest value
- When we start the first number is the lowest we keep moving and compare the next item with this first number if another item is lower we set it as the lowest number  switch to it and compare the next value
- When we reach the end we swap the lowest value with the first unordered value and carry out a second pass, and carry out many passes until the list is sorted
- Selection sort has the complexity of O(n*n) -> worst case, Theta(n*n) -> Average case, Omega(n*n) -> best case
- In insertion sort we start by comparing the first and second element if one is greater than the other we insert the greater one after on the right
- Insertion sort has a complexity of O(n*n) -> worst case, Theta(n*n) but Omega(n) -> best case

## Merge Sort Algorithm
- Follows the divide and conquer strategy
- - Divide: divides the problem into smaller sub-problems
- - Conquer: sub-problems are solved recursively
- - Combine: solutions of sub-problems are combined to achieve the final solution
- Dividing a list until each list has one element, then sorting while combining the same to make one list of all elements
- Merge sort has a complexity of O(n log n) worst case, significant improvement over bubble sort, selection sort and insertion sort
- Average case Theta(n log n), best case Omega(n log n), other algorithms have a better best case
- The inconvenience of this algorithm is space complexity
- Has space complexity of O(n) other algorithms we have studied have a space complexity of O(1)
- Other variants reduce space complexity

## Quick Sort Algorithms
- Also follows the divide and conquer principle
- Utilizes the partition technique which chooses a value from the list as a pivot 
- All items smaller than the pivot end at the left of the pivot
- Greater elements at the right
- Quick sort will be called recursively on the elements of the left and the right of the pivot
- Hoare's partition approach which sets the pivot as the first element of a list
- - The left pointer points to the first value from the pivot and the right pointer points to the last value We move the pointer until we find a greater value than the pivot
- - We move the right pointer until a value lower than pivot is found 
- Quick sort has the complexity of O(n*n) worst case ,Average case -> Theta(n log n), best case -> Omega(n log n), it is very efficient