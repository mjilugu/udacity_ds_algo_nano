#
# Huffman Coding
#

import sys
from heapq import heapify, heappush, heappop

class TreeNode:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

    def get_freq(self):
        return self.freq

    def get_value(self):
        return self.value

    def set_right(self, node):
        self.right = node

    def set_left(self, node):
        self.left = node

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def __lt__(self, other):
        if self.freq == other.freq:
            if self.value and other.value:
                return self.value < other.value
            elif self.value:
                return False
            else:
                return True

        return self.freq < other.freq

def build_huff_table(huff_tree, huff_table, huff_code = ""):

    if huff_tree == None:
        return

    if huff_tree.value:
        huff_table[huff_tree.value] = huff_code

    build_huff_table(huff_tree.right, huff_table, huff_code + "1")
    build_huff_table(huff_tree.left, huff_table, huff_code + "0")


def huffman_encoding(data):
    huff_table = dict()
    char_freq = dict()
    char_list = list()
    encoded_data = ""

    for char in data:
        char_freq[char] = char_freq.get(char, 0) + 1

    for char, freq in char_freq.items():
        _node = TreeNode(char, freq)
        char_list.append(_node)

    # sort smallest to highest frequency
    heapify(char_list)

    # build the huff tree
    while len(char_list) >= 2:
        item1 = heappop(char_list)
        item2 = heappop(char_list)

        internal_node = TreeNode(None, item1.get_freq() + item2.get_freq())
        internal_node.set_left(item1)
        internal_node.set_right(item2)

        heappush(char_list, internal_node)

    # build the huff table
    build_huff_table(char_list[0] if char_list else None, huff_table)

    # encode the data
    for letter in data:
        encoded_data += huff_table[letter]

    return (encoded_data, char_list[0] if char_list else None)

def huffman_decoding(data,tree):
    decoded_data = ""
    curr = tree
    idx = 0

    while idx < len(data):
        if curr.get_value():
            decoded_data += curr.get_value()
            curr = tree
            continue

        item = data[idx]

        if item == '0':
            curr = curr.get_left()
        else:
            curr = curr.get_right()
        idx += 1

    if curr and curr.get_value():
        decoded_data += curr.get_value()
        curr = tree

    return decoded_data

def print_huff_table(huff_table):
    for key,value in huff_table.items():
        print(f"{key}\t{value}")
#
# MAIN
#

if __name__ == "__main__":

    print(f"\n************** Test0: huffman_encoding('The bird is the word')")
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}".format(decoded_data))

    print(f"\n************** Test1: huffman_encoding('1 + 1 = 2')")
    a_great_sentence = "1 + 1 = 2"

    print ("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}".format(decoded_data))

    print(f"\n************** Test2: huffman_encoding('A')")
    a_great_sentence = "A"

    print ("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}".format(sys.getsizeof(encoded_data)))
    print ("The content of the encoded data is: {}".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}".format(decoded_data))

    print(f"\n************** Test3: huffman_encoding('')")
    a_great_sentence = ""

    print ("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}".format(sys.getsizeof(encoded_data)))
    print ("The content of the encoded data is: {}".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}".format(decoded_data))

    print(f"\n************** Test4: huffman_encoding('*>  <*')")
    a_great_sentence = "*>  <*"

    print ("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}".format(decoded_data))