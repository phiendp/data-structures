class LRUCache():

    def __init__(self, capacity=5):
        self.cache = {}
        self.item_list = []
        self.capacity = capacity

    def get_item(self, key):
        if key in self.cache:
            item_idx = self.item_list.index(key)
            self.item_list[:] = self.item_list[:item_idx] + \
                self.item_list[item_idx + 1:]
            self.item_list.insert(0, key)
            return self.cache[key]

        return -1


    def set_item(self, key, value):
        if key in self.cache:
            item_idx = self.item_list.index(key)
            self.item_list[:] = self.item_list[:item_idx] + \
                self.item_list[item_idx + 1:]
            self.item_list.insert(0, key)
        else:
            print(len(self.item_list))
            print(self.item_list)
            if len(self.item_list) > self.capacity:
                print("Removing")
                self.remove_item(self.item_list[-1])
            self.cache[key] = value
            self.item_list.insert(0, key)


    def remove_item(self, key):
        del self.hash[key]
        del self.item_list[self.item_list.index(key)]


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

    # print(cache.item_list)
    # print(cache.cache)
    # print(cache.capacity)

    assert cache.get_item(1) == -1
    assert cache.get_item(6) == 6

    print("Tests passed!")

if __name__ == "__main__":
    test_LRU()
