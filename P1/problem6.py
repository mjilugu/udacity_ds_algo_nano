#
# Union and Intersection of Two Linked Lists
#

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    u_list = LinkedList()
    temp_set = set()
    curr = llist_1.head

    for curr in [llist_1.head, llist_2.head]:
        while curr: 
            temp_set.add(curr.value)
            curr = curr.next

    for item in temp_set:
        u_list.append(item)

    return u_list

def intersection(llist_1, llist_2):
    i_list = LinkedList()
    arr_1 = list()
    arr_2 = list()

    curr = llist_1.head
    while curr:
        if curr.value not in arr_1:
            arr_1.append(curr.value)
        curr = curr.next

    curr = llist_2.head
    while curr:
        if curr.value not in arr_2:
            arr_2.append(curr.value)
        curr = curr.next

    for item in arr_1:
        if item in arr_2:
            i_list.append(item)
        
    return i_list


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print('\n-----------------------')
print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print('\n-----------------------')
print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [1,2,3]
element_2 = [1,4,5]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print('\n-----------------------')
print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))

# Test case 4

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = [1,2,3]
element_2 = [4,5]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print('\n-----------------------')
print (union(linked_list_7,linked_list_8))
print (intersection(linked_list_7,linked_list_8))