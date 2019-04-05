# Core Data Structures
*This is a repo that contains all core data structure knowledge and code base is in python*

### Number Bases *(April 1)*
*bases: decimal, binary, hexidecimal*

###### 8 bits one's complement, addition
*with negative values, reverse all the values of the 8 bits from 0 to 1, 1 to 0.\
*addition*: grab one's complement values and plus them, 1 + 1 = 0, but carry the 1 to the next addition.*
###### 8 bits two's complement, addition
*ith negative values, get the 8 bit value, look for the one from right to left. and flip everything after that one value.*
	
[bases.py](https://github.com/RinniSwift/CoreDataStructures/blob/master/bases.py)\
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

[search.py](https://github.com/RinniSwift/CoreDataStructures/blob/master/search.py)\
[factorial_recurssion.py](https://github.com/RinniSwift/CoreDataStructures/blob/master/factorial_recursion.py)
