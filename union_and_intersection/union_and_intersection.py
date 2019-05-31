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
    all_elements = set()
    result = LinkedList()

    current_list_1 = llist_1.head
    while current_list_1:
        if current_list_1.value not in all_elements:
            all_elements.add(current_list_1.value)
            result.append(current_list_1)
        current_list_1 = current_list_1.next

    current_list_2 = llist_2.head
    while current_list_2:
        if current_list_2.value not in all_elements:
            all_elements.add(current_list_2.value)
            result.append(current_list_2)
        current_list_2 = current_list_2.next

    return result


def intersection(llist_1, llist_2):
    all_elements = set()
    result = LinkedList()

    current_list_1 = llist_1.head
    while current_list_1:
        if current_list_1.value not in all_elements:
            all_elements.add(current_list_1.value)
        current_list_1 = current_list_1.next

    current_list_2 = llist_2.head
    while current_list_2:
        if current_list_2.value in all_elements:
            result.append(current_list_2)
            all_elements.remove(current_list_2.value)
        current_list_2 = current_list_2.next

    return result


# Test case 1
def test_1():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))

# Test case 2
def test_2():
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3, linked_list_4))

    print(intersection(linked_list_3, linked_list_4))


# Test case 3
def test_3():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = []
    element_2 = []

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))


# Test case 4
def test_4():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [1, 2, 3]
    element_2 = []

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
