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
```
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
### 432. All Oone Data Structure
```
class Node:
    def __init__(self, val = 0):
        self.val = val
        self.keys = set()
        self.prev = None
        self.next = None
        
    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        self.next, self.prev = None, None
        
    def insert_after(self, new_node):
        old_next = self.next
        self.next = new_node
        new_node.prev = self
        new_node.next = old_next
        old_next.prev = new_node
            
class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.begin = Node()
        self.end = Node()
        self.begin.next = self.end
        self.end.prev = self.begin
        self.mapping = {}

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.mapping:
            curr_node = self.begin
        else:
            curr_node = self.mapping[key]
            curr_node.keys.remove(key)
        
        if curr_node.val + 1 != curr_node.next.val:
            new_node = Node(curr_node.val + 1)
            curr_node.insert_after(new_node)
        else:
            new_node = curr_node.next
            
        new_node.keys.add(key)
        self.mapping[key] = new_node
        
        if not curr_node.keys and curr_node.val != 0:
            curr_node.remove()
            

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.mapping:
            return
        
        curr_node = self.mapping[key]
        del self.mapping[key]
        curr_node.keys.remove(key)
        
        if curr_node.val != 1:
            if curr_node.val - 1 != curr_node.prev.val:
                new_node = Node(curr_node.val - 1)
                curr_node.prev.insert_after(new_node)
            else:
                new_node = curr_node.prev
            new_node.keys.add(key)
            self.mapping[key] = new_node
            
        if not curr_node.keys:
            curr_node.remove()
            

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if self.end.prev.val == 0:
            return ""
        key = self.end.prev.keys.pop()
        self.end.prev.keys.add(key)
        return key
        

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self.begin.next.val == 0:
            return ""
        key = self.begin.next.keys.pop()
        self.begin.next.keys.add(key)
        return key
```
### 1146. Snapshot Array
```
import bisect
class SnapshotArray:

    def __init__(self, length: int):
        self.array = [[(-1, 0)] for _ in range(length)]
        self.snap_id = 0
        
    def set(self, index: int, val: int) -> None:
        self.array[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
        
    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect(self.array[index], (snap_id + 1, 0)) - 1
        return self.array[index][i][1]
```
