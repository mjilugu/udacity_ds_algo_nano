# 
# Least Recently Used Cache
# 
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.items = dict()
        self.age = 1

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if self.items.get(key) is None:
            return -1
        self.items[key]['age'] = self._generate_age()
        return self.items.get(key)['value']

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if len(self.items) >= self.capacity:
            self._remove_lru_item() 

        self.items[key] = {"value":value, "age":self._generate_age()}
    
    def _remove_lru_item(self):
        lru_key = min(self.items, key = lambda x: self.items[x]['age'])
        self.items.pop(lru_key) 

    def _generate_age(self):
        curr = self.age
        self.age += 1

        return curr

if __name__ == "__main__":
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);


    assert our_cache.get(1) == 1, "our_cache.get(1) should return 1"       # returns 1
    assert our_cache.get(2) == 2, "Fail"      # returns 2
    assert our_cache.get(9) == -1, "Fail"     # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5) 
    our_cache.set(6, 6)

    assert our_cache.get(3) == -1, "Fail"      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
