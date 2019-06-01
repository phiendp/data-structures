class DoubleLinkedNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.total_elements = 0

    def size(self):
        return self.total_elements

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, key, value):
        """
        Add the new item to the end of the queue
        """
        node = DoubleLinkedNode(key, value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.total_elements += 1
        return node

    def dequeue(self):
        """
        Remove the item from the start of the queue
        """
        if self.is_empty():
            return None

        node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None

        self.total_elements -= 1
        return node.key


class LRUCache:
    def __init__(self, capacity=5):
        self.cache = {}
        self.queue = Queue()
        self.total_items = 0
        self.capacity = capacity

    def update(self, node):
        """
        Move the node to the end of the queue (recently use)
        """

        # Edge cases: when there is only one item or the given item is already recently used
        if self.total_items == 1:
            return
        elif node == self.queue.tail:
            return

        # Handle cases when there is item in front of and behind the item in the queue
        if node.prev is not None:
            node.prev.next = node.next

        if node.next is not None:
            node.next.prev = node.prev
            if node == self.queue.tail:
                self.queue.head = node.next

        # Move the item to the end of the queue
        self.queue.tail.next = node
        node.prev = self.queue.tail
        self.queue.tail = node
        self.queue.tail.next = None

    def get_item(self, key=None):
        """
        Get operation:
        - If cache hit, update the node's position in the queue, then return its value.
        - If cache miss, return -1
        """
        if key is None:
            return -1

        node = self.cache.get(key)
        if node is not None:
            self.update(node)
            return node.value
        return -1

    def set_item(self, key, value):
        """
        Set operation:
        - Set the key and value if the key is not in the cache.
        - If the cache hits its capacity, then remove the oldest item from both the queue and cache dictionary
        """
        if key is None:
            return

        if self.get_item(key) == -1:
            if self.total_items == self.capacity:
                self.remove()
            node = self.queue.enqueue(key, value)
            self.cache[key] = node
            self.total_items += 1
        else:
            self.cache[key].value = value

    def remove(self):
        key = self.queue.dequeue()
        del self.cache[key]
        self.total_items -= 1


def test_LRU():
    cache = LRUCache()

    cache.set_item(1, 1)
    cache.set_item(2, 2)

    assert cache.get_item(1) == 1
    assert cache.get_item(2) == 2
    assert cache.get_item(3) == -1

    cache.set_item(3, 3)
    cache.set_item(4, 4)
    cache.set_item(5, 5)
    cache.set_item(6, 6)

    assert cache.get_item() == -1
    assert cache.get_item(1) == -1
    assert cache.get_item(6) == 6
    assert cache.get_item(5) == 5

    print("Tests passed!")

if __name__ == "__main__":
    test_LRU()
