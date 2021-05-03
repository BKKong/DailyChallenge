### 113. Path Sum II

```
# class Solution:
#     def pathSum(self, root: TreeNode, sums: int) -> List[List[int]]:
#         if not root:
#             return []
#         self.ans = []
#         self.dfs(root, 0, [], sums)
#         return self.ans
    
#     def dfs(self, node, prev_sum, curr, target):
#         if not node.left and not node.right and prev_sum + node.val == target:
#             self.ans.append(curr + [node.val])
#             return 
#         prev_sum += node.val
#         curr.append(node.val)
#         if node.left:
#             self.dfs(node.left, prev_sum, curr, target)
#         if node.right:
#             self.dfs(node.right, prev_sum, curr, target)
#         prev_sum -= node.val
#         curr.pop()
```

### 437. Path Sum III
```
# class Solution:
#     def pathSum(self, root: TreeNode, sums: int) -> int:
#         if not root:
#             return 0
#         self.ans = 0
#         self.dfs(root, 0, sums, {0: 1})         ### Bug: missing {0: 1}
#         return self.ans
    
#     def dfs(self, node, prev_sum, target, counter):
#         if not node:
#             return 
#         if prev_sum + node.val - target in counter:
#             self.ans += counter[prev_sum + node.val - target]
#         prev_sum += node.val
#         counter[prev_sum] = counter.get(prev_sum, 0) + 1
#         self.dfs(node.left, prev_sum, target, counter)
#         self.dfs(node.right, prev_sum, target, counter)
#         counter[prev_sum] -= 1
#         if counter[prev_sum] == 0:
#             del counter[prev_sum]
#         prev_sum -= node.val
```

### 666. Path Sum IV
```
# from collections import defaultdict
# class Solution:
#     def pathSum(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         numbers = defaultdict(dict)
#         for num in nums:
#             str_num = str(num)
#             start = int(str_num[0])
#             mid = int(str_num[1])
#             val = str_num[2]
#             numbers[start][mid] = int(val)
#         self.ans = 0
#         self.dfs(1, 1, numbers[1][1], numbers)
#         return self.ans
    
#     def dfs(self, row, col, curr, numbers):
#         if row + 1 not in numbers:
#             self.ans += curr
#             return 
#         if all(i not in numbers[row + 1] for i in [col * 2 - 1, col * 2]):
#             self.ans += curr
#             return
#         for new_col in [col * 2 - 1, col * 2]:
#             if new_col in numbers[row + 1]:
#                 self.dfs(row + 1, new_col, curr + numbers[row + 1][new_col], numbers)
            
```
