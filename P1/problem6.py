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

    def append_array(self, arr):
        for element in arr:
            self.append(element)

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


if __name__ == '__main__':

    print(f"Test0: is_user_in_group(sub_child_user, child)")
    # True

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    linked_list_1.append_array([3,2,4,35,6,65,6,4,3,21])
    linked_list_2.append_array([6,32,4,9,6,1,11,21,1])

    u_list = union(linked_list_1,linked_list_2)
    i_list = intersection(linked_list_1,linked_list_2)
    print (u_list)
    print (i_list)

    print(f"Test1: is_user_in_group(sub_child_user, child)")
    # True

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    linked_list_3.append_array([3,2,4,35,6,65,6,4,3,23])
    linked_list_4.append_array([1,7,8,9,11,21,1])

    u_list = union(linked_list_3,linked_list_4)
    i_list = intersection(linked_list_3,linked_list_4)
    print (u_list)
    print (i_list)

    print(f"\nTest2: is_user_in_group(sub_child_user, child)")
    # True

    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    linked_list_5.append_array([1,2,3])
    linked_list_6.append_array([1,4,5])

    u_list = union(linked_list_5,linked_list_6)
    i_list = intersection(linked_list_5,linked_list_6)
    print (u_list)
    print (i_list)

    print(f"\nTest3: is_user_in_group(sub_child_user, child)")
    # True

    linked_list_7 = LinkedList()
    linked_list_8 = LinkedList()

    linked_list_7.append_array([1,2,3])
    linked_list_8.append_array([4,5])

    u_list = union(linked_list_7,linked_list_8)
    i_list = intersection(linked_list_7,linked_list_8)
    print (u_list)
    print (i_list)