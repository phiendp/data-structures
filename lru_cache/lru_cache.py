class LRUCache(object):

    def __init__(self, capacity):
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
            if len(self.item_list) > self.capacity:
                self.remove_item(self.item_list[-1])
            self.cache[key] = value
            self.item_list.insert(0, key)


    def remove_item(self, key):
        del self.hash[key]
        del self.item_list[self.item_list.index(key)]
