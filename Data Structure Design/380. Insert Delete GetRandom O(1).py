# all methods are in O(1)

class RandomizedSet:

    def __init__(self):
        self.nums = [] # the set itself
        self.valToIndex = {} # use a map to manage the set value to index for O(1) swapping
        self.idx = -1
        

    def insert(self, val: int) -> bool:
        if val in self.valToIndex:
            return False
        
        self.nums.append(val)
        self.idx += 1
        self.valToIndex[val] = self.idx
        
        return True

    # swap the delete target to the list end, pop from the end is O(1)
    def remove(self, val: int) -> bool:
        if val in self.valToIndex:
            last_val_idx = self.valToIndex[val]
            last_val = self.nums[-1]
            
            # swap the last element to the place of the target
            self.nums[last_val_idx], self.valToIndex[last_val] = last_val, last_val_idx
            
            # delete
            self.nums.pop()
            self.valToIndex.pop(val)
            self.idx -= 1
            return True
        return False
            
    
    def getRandom(self) -> int:
        # etRandom could be implemented in O(1) time with the help of standard random.choice in Python and Random object in Java.
        return choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()