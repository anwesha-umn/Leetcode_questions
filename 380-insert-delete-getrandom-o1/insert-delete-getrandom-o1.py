class RandomizedSet:

    def __init__(self):
        self.new_set = []

    def insert(self, val: int) -> bool:
        if val not in self.new_set:
            self.new_set.append(val)
            return True
        return False
        
    def remove(self, val: int) -> bool:
        for n in self.new_set:
            if n == val:
                self.new_set.remove(val)
                return True
        return False
        
    def getRandom(self) -> int:
        import random
        return random.choice(self.new_set)
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()