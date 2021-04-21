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

### 308. Range Sum Query 2D - Mutable
```
class FenwickTree:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.bit_matrix = [[0] * cols for _ in range(rows)]
        
    def update(self, r, c, value):
        i = r
        while i < self.rows:
            j = c
            while j < self.cols:
                self.bit_matrix[i][j] += value
                j += self.lowbit(j)
            i += self.lowbit(i)
            
    def query(self, r, c):
        s = 0
        i = r
        while i > 0:
            j = c
            while j > 0:
                s += self.bit_matrix[i][j]
                j -= self.lowbit(j)
            i -= self.lowbit(i)
        return s
        
    def lowbit(self, x):
        return x & -x
        
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.bits = FenwickTree(self.m + 1, self.n + 1)
        for i in range(self.m):
            for j in range(self.n):
                self.bits.update(i + 1, j + 1, matrix[i][j])

    def update(self, row: int, col: int, val: int) -> None:
        #old_val = self.sumRegion(row, col, row, col)
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        self.bits.update(row + 1, col + 1, delta)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a = self.bits.query(row2 + 1, col2 + 1)
        b = self.bits.query(row2 + 1, col1)
        c = self.bits.query(row1, col2 + 1)
        d = self.bits.query(row1, col1)
        return a - b - c + d
```
