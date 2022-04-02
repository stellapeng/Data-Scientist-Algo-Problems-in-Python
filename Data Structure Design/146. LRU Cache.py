# Time Complexsity: get() and put() are both O(1)
# Space Complexity: O(capacity)

# OrderedDict() is similar to LinkedHashMap<>() in java
# cache.move_to_end()
# cache.popitem(last = False)

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if (key not in self.cache):
            return -1;
        self.cache.move_to_end(key) # put the LRU key in the last
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if (key in self.cache):
            self.cache.move_to_end(key)
        
        elif(len(self.cache)>=self.cap):
            # oldestKey = next(iter(self.cache))
            self.cache.popitem(last=False)
        
        self.cache[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)