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
Time complexity is O(nlogn) from the quick sort as the part that gets the two numbers is linear O(n). Space complexity is linear O(n) from the quicksort.

# Problem 4 - Dutch National Flag Problem

In this problem we are sorting an array of 0s, 1s and 2s. I use a linear approach, processing the numbers one at a time. 
General approach is to move all the 0s to the front and all the 2s to the back. The 1s will be in correct position after that. 
Time complexity is linear O(n) and space is constant O(1) as we sort in place.

# Problem 5 - Autocomplete with Tries

The solution consists of classes TrieNode and Trie. 

The TrieNode class has a constructor and methods insert() and suffixes(). 
The constructor initializes the class and it's time and space complexity are both constant O(1). 
The insert() method adds a new child node to the children of the node if it isn't already in the children list. It has linear time complexity as it checks the full list of children before adding and it has constant space complexity.
The suffixes() method uses a modified breadth first algorithm to return a list of all suffixes of a given prefix. Starting at the prefix node, I recursively construct the suffix by calling the private _suffixes_rec() method for each child of the node. At any node with word_end set to true we add a new suffix to the return list. The time complexity is linear O(n) as we check every node of the prefix sub tree. Space complexity is linear O(n) as we make recursive call for every node on the sub tree.

The Trie class has a constructor and methods insert() and find(). The constructor has constant time and space complexity O(1). 
The insert() method adds a word to the trie. It has linear time complexity O(n) and constant space complexity O(1).
The find() method finds the node that represents a given prefix. It has linear time complexity O(n) and constant time complexity O(1).

# Problem 6 - Max and Min in a Unsorted Array

In this problem we are searching for the max and min values in an array of integers. I use a linear approach, evaluating one number at a time.
Initializing both min and max to the first element, we traverse the list comparing every element to min and max and reassign where suitable.
The time complexity is O(n) and space complexity is constant O(1).

# Problem 7 - HTTPRouter using a Trie

The solution consists of classes Router, RouteTrie and RouteTrieNode.
The RouteTrieNode class has a constructor and method insert().
The constructor initializes the class and has constant time and space complexity O(1).
The insert() method adds the first path to the node and recursively adds the rest to the first path's node. It assign the passed handler to the last node in the path. It has linear time complexity O(n). Space complexity is linear O(1) since we recurse on very path in the path array.

The RouteTrie class has a constructor and methods insert() and find().
The constructor initializes the class and has constant time complexity and constant space complexity.
The insert() method inserts an array of routes to the trie. It does this by calling insert() on the root node which recursively adds the routes. It's time complexity is linear O(n) and space complexity is linear O(n). Both time and space are from the node's insert method.
The find() method finds the node matching the path i.e. last node in the path. Returns None otherwise. It has linear O(n) time complexity and constant O(1) space complexity.

The Router class has a constructor and methods add_handler(), lookup() and split_path().
The constructor initializes the class and has constant O(1) time and space complexity.
The add_handler() method splits the path string with the split_path() method. It then passes on the path array and handler to the insert method of the routes trie. Both split and insert have linear O(n) time complexity and thus it is the complexity of this function as well. Space complexity is linear O(n) contributed by the trie's insert call.
The lookup() method finds the handler for a given path or returns the not-found handler. It splits the path string with the split_path() method and passes the path array to the route trie find() method. Both split_path() and find() are linear and thus time complexity is linear O(n). Space complexity is constant O(1).
The split_path() method splits the path string into the constituent paths and return them as an array. It has linear O(n) time complexity and constant O(1) space complexity.
