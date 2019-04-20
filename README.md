# Core Data Structures
*This is a repo that contains all core data structure knowledge and code base is in python*

### Number Bases *(April 1)*
*bases: decimal, binary, hexidecimal*

###### 8 bits one's complement, addition
*with negative values, reverse all the values of the 8 bits from 0 to 1, 1 to 0.\
*addition*: grab one's complement values and plus them, 1 + 1 = 0, but carry the 1 to the next addition.*
###### 8 bits two's complement, addition
*ith negative values, get the 8 bit value, look for the one from right to left. and flip everything after that one value.*
	
1. [bases.py](https://github.com/RinniSwift/CoreDataStructures/blob/master/bases.py)\
&nbsp;&nbsp;&nbsp;**Decode**: *turns number into base 10*\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;takes in two parameters(1. digits 2. base)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*digits* being string format of the number.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*base* being the integer representation of the digits base.\
&nbsp;&nbsp;&nbsp;**Encode**: *encodes given changes number from base 10 into different base*\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;takes in three parameters(1. digits 2. base1, base2) \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*digits* being an int of the number.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*base1* being the integer representation of the digits base.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*base2* being the integer representation of the base you want to convert to.

### Search algorithms *(April 3)*
*using iterative and recurssive implementation on searching functions*\
**Linear search**: O(n) run time. n being the number of items in the data structure.\
**Binary search**: O(log(n)) run time. Also called the 'divide and conquer' approach since we are only looking at the middle and reducing ini half everytime. [checks middle value and decides to cut the entire left side or entire right]. data structure must be sorted and items must be comparable.\
&nbsp;&nbsp;&nbsp;&nbsp;*logarithm* mainly used for finding x where x is an exponent. log(n), n being the number of items in the data structure, meaning the amount of times it takes to divide the data structure into half until the data structure is 1.

2. [search.py](https://github.com/RinniSwift/CoreDataStructures/blob/master/search.py)
3. [factorial_recurssion.py](https://github.com/RinniSwift/CoreDataStructures/blob/master/factorial_recursion.py)

### String algorithms *(April 8)*
4. [strings.py](https://github.com/RinniSwift/CoreDataStructures/blob/master/strings.py)\
&nbsp;&nbsp;&nbsp;**contains**: *function that returns true if pattern is found in the text*\
&nbsp;&nbsp;&nbsp;**find_index**: *function that returns the first index of found pattern in the text*\
&nbsp;&nbsp;&nbsp;**find_all_indexes**: *function that returns all initial indexes of the pattern that has been found in the text in a list*\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*text: a body of text in (string format)*\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*pattern: a smaller body of text to compare in the text(string format)*

5. [palindromes.py](https://github.com/RinniSwift/CoreDataStructures/blob/master/palindromes.py)\
&nbsp;&nbsp;&nbsp;**palindrom**: *a string that reads the same forwards and backwards*\
&nbsp;&nbsp;&nbsp;**is_palindrome**: *function implemented both iteratively and recurssively returning bool indicating if is a palindrome*

### Arrays and LinkedLists *(April 10)*
6. [linkedlist.py](https://github.com/RinniSwift/CoreDataStructures/blob/master/linkedlist.py)\
&nbsp;&nbsp;&nbsp;**size**: property tracks the length of the linked list\
&nbsp;&nbsp;&nbsp;**get_at_index**: returns the item at that index\
&nbsp;&nbsp;&nbsp;**insert_at_index**: inserts given item at given index\
&nbsp;&nbsp;&nbsp;**replace**: replaces item at given index

7. [doubly_linkedlist.py](https://github.com/RinniSwift/CoreDataStructures/blob/master/doubly_linkedlist.py)\
&nbsp;&nbsp;&nbsp;**previous**: tracks the previous item of each node\
&nbsp;&nbsp;&nbsp;**next**: tracks the next property of each node

### Lists, Stacks, and Queues *(April 15)*
8. [stacks.py](https://github.com/RinniSwift/CoreDataStructures/blob/master/stack.py)\
&nbsp;&nbsp;&nbsp;**LinkedStack**: stack implemented as a linkedlist\
&nbsp;&nbsp;&nbsp;**ArrayStack**: stack implemented as an array\
\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*is_empty: check if the stack is empty*\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*length: checks the total length of the stack*\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*push: push item to top of stack*\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*pop: removes and returns the item on the top of the stack*\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*peek: returns the top item on the stack*

9. [queue.py](https://github.com/RinniSwift/CoreDataStructures/blob/master/queue.py)\
&nbsp;&nbsp;&nbsp;**LinkedQueue**: queue implemented as a linkedlist\
&nbsp;&nbsp;&nbsp;**ArrayQueue**: queue implemented as an array\
\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*is_empty: check if the queue is empty*\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*length: checks the total length of items in the queue*\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*enqueue: append item into the back of the queue*\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*dequeue: removes and returns the item at the fron of the queue*

10. [deque.py](https://github.com/RinniSwift/CoreDataStructures/blob/master/deque.py)\
&nbsp;&nbsp;&nbsp;**ArrayDeque**: deque implemented as an array\
\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*is_empty: check if the deque is empty*\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*length: checks the total length of items in the deque*\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*push_front: append item to front of the deque*\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*push_back: append item to the back of the deque*\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*pop_front: returns item at front of the deque*\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*pop_back: returns item at the back of the deque*

### Hash Tables *(April 17)*
11. [hashtables.py](https://github.com/RinniSwift/CoreDataStructures/blob/master/hashtable.py)\
&nbsp;&nbsp;&nbsp;**load_factor**: used chaining for collision resolution by using linkedlists\
&nbsp;&nbsp;&nbsp;**load_factor**: calculating the load factor of the hash table\
&nbsp;&nbsp;&nbsp;**resize**: method that is called when the load factor is greater than 0.75