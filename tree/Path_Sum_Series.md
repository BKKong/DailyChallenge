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
