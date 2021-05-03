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
