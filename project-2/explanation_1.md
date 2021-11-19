# Problem 1 - Least Recently Used Cache

This LRU cache uses a dictionary to store entries. Each entry
consists of an object with value and age field. Age is initialized at the time of instantiation of the cache and each object gets the current value of age at the time they are added to the cache before it is incremented.
The efficiency of both get() and set() is O(1). The total space complexity of both get() and set() is O(N) matching the capacity of the cache.

# Problem 2 - File Recursion

The function find_files(suffix, path) recursively searches for files with given suffix under path. At each directory level we search the directory entries, repeating the search if entry is a directory. 
This algorithm will visit every sub path once for an efficiency of O(N). Space complexity of the function is also O(N) as each recursive call require space for the path and suffix string.

# Problem 3 - Huffman Coding

The function huffman_encoding() builds the huffman tree and encodes the data with it. Time significant part of the algorithm is the loop that builds the huffman tree which takes O(nlogn) time.
The huffman_decode() decodes encoded data using the huffman tree. It has efficiency of O(N), it's time significant part loops through each item in data.
Both functions have space complexity of O(N) as their most singnificant space at any point is input data.

# Problem 4 - Active Directory

Function is_user_in_group() searches for first occurence of given user in sub group structure of a given group. Worst case scenario it will traverse all subgroups for a total time of O(N). This will also be the worst case size of the call stack for a space complexity of O(N)

# Problem 5 - Blockchain

Solution consists of the class Blockchain. The add_block() method has efficiency of O(1). The verify_blockchain() and find() methods have efficiency of O(N). All the function have 
the space complexity of O(N) matching to the number of blocks in the blockchain.

# Problem 6 - Union and Intersection of Two Linked Lists

Solution consists of new functions union() and intersection(). Both function have time complexity of O(N). The space complexity of both functions will be O(N^2) matching to the size of both input lists.