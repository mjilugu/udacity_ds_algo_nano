# Problem 1 - Square Root

Square root implementation returning the square root of a number or the floor int of the square root.
The implementation checks the integers between 0 and number//2. Using divide and conquer we compare the square value of the mid value with the number and reduce the check to the half of the number where the square root lies.
Time complexity is O(logn) and space is constant O(1).

# Problem 2 - Rotated Array Search

Function rotated_array_search finds given number in a rotated array. Splitting the array in two, one portion will be sorted and we can detect if the number lays in that portion. This helps us eliminate one half in every iteration. 
Time complexity is O(logn) and space is constant O(1) since we search in place.

# Problem 3 - Rearrange Array Digit To Get Max Sum Pair

The solution involves first sorting the array in descending order. We then remove two elements at a time from the array untill it is empty appending the first as next lower digit of num_1 and appending the second as next lower digit of num_2. 
Time complexity is O(nlogn) from the quick sort and space is constant O(1).

# Problem 4 - Sort Array of 0s, 1s and 2s

General approach is to move all the 0s to the front and all the 2s to the back. The 1s will be in correct position after that. 
Time complexity is O(n) and space is constant O(1) as we sort in place.

# Problem 5 - Trie

The trie has the usual insert() and find() methods that add/locate nodes. For a given node they iterate on the characters to either insert the word or locate it. Both have time efficiency of O(n) and space efficiency of O(1).
The suffixes() method takes a prefix and it first locates the node matching the last characher in the prefix. If any char in the prefix does not have a matching node we return empty list of suffixes. Otherwise we call _suffixes_rec() with the last node in prefix and empty suffix. The _suffixes_rec() method searches recursively the sub-tree starting at prefix as root and collects all nodes which are wordends and the words they form from the root (prefix).
This list is returned as the suffix list. The time efficiency of this is linear O(n) as we the whole sub tree and space complexity is O(1) 

# Problem 6 - Min Max

Initializing both min and max to the first element, we traverse the list comparing every element to min and max and assign where suitable.
The complexity is O(n) and space is constant O(1).

# Problem 7 - Web Router

The main methods in the implementation are add_handler() and lookup(). 
add_handler() splits the path into array of components and passes the array and handler to the trie insert() method. The router trie insert() passes these to the root node insert which recursively calls insert to add every path in the array. The the handler gets passed to the last node. Efficiency of insert is linear O(n) and space efficiency is constant O(1).
The lookup() method splits the path into array of paths and calls find on the root node with this array. For every path we examine the corresponding node. If any part in the path is does not match a node we return None otherwise we return 
the handler of last node. Efficiency of find is linear O(n) and space is constant O(1)
