## Object Oriented Design

### 380. Insert Delete GetRandom O(1)
Implement the RandomizedSet class:
- RandomizedSet() Initializes the RandomizedSet object.
- bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
- bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
- int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
```
import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = {}
        self.nums = []
        self.size = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.store:
            return False
        self.nums.append(val)
        self.store[val] = self.size
        self.size += 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.store:
            return False
        index = self.store[val]
        last_index = self.size - 1
        self.nums[index] = self.nums[last_index]
        self.store[self.nums[index]] = index
        self.nums.pop()
        del self.store[val]
        self.size -= 1
        return True
        
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        index = random.randint(0, self.size - 1)
        return self.nums[index]
```
### 381. Insert Delete GetRandom O(1) - Duplicates allowed

import random
class RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = defaultdict(set)
        self.nums = []
        self.size = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        not_exist = False
        if val not in self.store:
            not_exist = True
        self.store[val].add(self.size)
        self.nums.append(val)
        self.size += 1
        return not_exist

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.store:
            return False
        last_num, last_index = self.nums[-1], self.size - 1
        if last_num == val:
            self.store[val].remove(last_index)
            if not self.store[val]:
                del self.store[val]
            self.nums.pop()
            self.size -= 1
            return True
        del_index = next(iter(self.store[val]))
        self.nums[del_index] = last_num
        self.store[val].remove(del_index)
        if not self.store[val]:
            del self.store[val]
        self.store[last_num].add(del_index)
        self.store[last_num].remove(last_index)
        self.nums.pop()
        self.size -= 1
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        index = random.randint(0, self.size - 1)
        return self.nums[index]
```
