### 307. Range Sum Query - Mutable
```
class FenwickTree:
    def __init__(self, n):
        self.sums = [0] * n
        self.length = n
        
    def insert(self, index, value):
        while index < self.length:
            self.sums[index] += value
            index += self.lowbit(index)
            
    def query(self, index):
        out = 0
        while index > 0:
            out += self.sums[index]
            index -= self.lowbit(index)
        return out
        
    def lowbit(self, i):
        return i & -i
        
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tree = FenwickTree(len(nums) + 1)
        for i, num in enumerate(nums):
            self.tree.insert(i + 1, num)

    def update(self, index: int, val: int) -> None:
        if index < len(self.nums) and self.nums[index] != val:
            delta = val - self.nums[index]
            self.nums[index] = val
            self.tree.insert(index + 1, delta)

    def sumRange(self, left: int, right: int) -> int:
        left = self.tree.query(left)
        right = self.tree.query(right + 1)
        return right - left
```
