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
    print(f"\n*** our_cache initiated with capacity 5 ***\n")
    our_cache = LRU_Cache(5)
    print(f"Test0: our_cache.get(1000) returns -1, cache is empty")
    #-1
    print(f"{our_cache.get(0)}")

    print(f"\n*** Add four values to our_cache ***\n")
    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);

    print(f"Test1: our_cache.get(1) returns 1")
    #1
    print(f"{our_cache.get(1)}")
    print(f"Test2: our_cache.get(2) returns 2")
    #2
    print(f"{our_cache.get(2)}")
    print(f"Test3: our_cache.get(9) returns -1")
    #-1
    print(f"{our_cache.get(9)}")

    print(f"\n*** Add two new elements to our_cache ***\n")
    our_cache.set(5, 5) 
    our_cache.set(6, 6)

    print(f"Test3: our_cache.get(3) returns -1 as 3 was replaced as least recently used element")
    #-1
    print(f"{our_cache.get(3)}")
