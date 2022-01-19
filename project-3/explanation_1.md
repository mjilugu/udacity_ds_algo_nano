# Problem 1 - Square Root of an Integer

In this problem we are looking for the square root of a number or the floor int of the square root.
The implementation uses binary search algorithm to check the integers between 0 and number//2. We compare the square of the mid value with the number and reduce the check to the half of the number where the square root lays.
Time complexity is O(logn) and space complexity is constant O(1).

# Problem 2 - Search in a Rotated Sorted Array

Function rotated_array_search finds a given number in a rotated array. 
The implementation uses a modified binary search algorithm to eliminate one half of the array in every iteration. Splitting the array in two, one portion will be in sorted order and we can detect if the number lays in that portion. This helps us eliminate one half in every iteration. 
Time complexity is O(logn) and space complexity is constant O(1) since we search in place.

# Problem 3 - Rearrange Array Elements

The solution involves first sorting the array in descending order. I chose to use quick sort algorithm for the sort. 
We move on to generate the two numbers with max sum from the array. We linearly process the numbers in the array. We do this by removing a number from the array and append it to the first number as the new lowest digit. We then remove the next number and append it as the new lowest digit of second number. We repeat this until no more numbers are left in the array. 
If any of the two numbers is empty, it will be represented by -1.
Time complexity is O(nlogn) from the quick sort as the part that gets the two numbers is linear O(n). Space complexity is constant O(1).

# Problem 4 - Dutch National Flag Problem

In this problem we are sorting an array of 0s, 1s and 2s. I use a linear approach, processing the numbers one at a time. 
General approach is to move all the 0s to the front and all the 2s to the back. The 1s will be in correct position after that. 
Time complexity is O(n) and space is constant O(1) as we sort in place.

# Problem 5 - Autocomplete with Tries

The trie has the usual insert() and find() methods that add/locate nodes. For a given node they iterate on the characters to either insert the word or locate it. Both have time efficiency of O(n) and space efficiency of O(1).
The suffixes() method takes a prefix and it first locates the node matching the last characher in the prefix. If any char in the prefix does not have a matching node we return empty list of suffixes. Otherwise we call _suffixes_rec() with the last node in prefix and empty suffix. The _suffixes_rec() method searches recursively the sub-tree starting at prefix as root and collects all nodes which are wordends and the words they form from the root (prefix).
This list is returned as the suffix list. The time efficiency of this is linear O(n) as we the whole sub tree and space complexity is O(1) 

# Problem 6 - Max and Min in a Unsorted Array

In this problem we are searching for the max and min values in an array of integers. I use a linear approach, evaluating one number at a time.
Initializing both min and max to the first element, we traverse the list comparing every element to min and max and reassign where suitable.
The time complexity is O(n) and space complexity is constant O(1).

# Problem 7 - HTTPRouter using a Trie

The main methods in the implementation are add_handler() and lookup(). 
add_handler() splits the path into array of components and passes the array and handler to the trie insert() method. The router trie insert() passes these to the root node insert which recursively calls insert to add every path in the array. The the handler gets passed to the last node. Efficiency of insert is linear O(n) and space efficiency is constant O(1).
The lookup() method splits the path into array of paths and calls find on the root node with this array. For every path we examine the corresponding node. If any part in the path is does not match a node we return None otherwise we return 
the handler of last node. Efficiency of find is linear O(n) and space is constant O(1)
