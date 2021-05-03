## Binary Search Tree

### 333. Largest BST Subtree
```
# import math
# class Solution:
#     def largestBSTSubtree(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         max_bst = 0
        
#         def largest(node):
#             if not node:
#                 return math.inf, -math.inf, 0, 0
#             l_min, l_max, l_bst, l_best = largest(node.left)
#             r_min, r_max, r_bst, r_best = largest(node.right)
#             if l_max < node.val and node.val < r_min:
#                 c_min = min(l_min, node.val)
#                 c_max = max(r_max, node.val)
#                 if l_bst != -1 and r_bst != -1:
#                     c_bst = l_bst + r_bst + 1
#                 else:
#                     c_bst = -1
#                 c_best = max(l_best, r_best, c_bst)
#                 return c_min, c_max, c_bst, c_best
#             else:
#                 return -math.inf, math.inf, -1, max(l_best, r_best)
        
#         r_min, r_max, r_bst, r_best = largest(root)
#         return r_best     
```
