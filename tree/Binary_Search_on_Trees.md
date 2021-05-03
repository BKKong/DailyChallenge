### 222. Count Complete Tree Nodes
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

```
# class Solution:
#     def countNodes(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         depth = self.get_depth(root)
#         if depth == 0:
#             return 1
#         left, right = 0, 2 ** depth
#         while left < right - 1:
#             mid = (left + right) // 2
#             if self.exist_node(mid, depth, root):
#                 left = mid
#             else:
#                 right = mid
#         #print("l: ", left)
#         return 2 ** depth + left
        
#     def get_depth(self, node):
#         d = 0
#         while node.left:
#             d += 1
#             node = node.left 
#         return d
    
#     def exist_node(self, target, depth, node):
#         left, right = 0, 2 ** depth
#         while left < right - 1:
#             mid = (left + right) // 2
#             if target >= mid:
#                 node = node.right
#                 left = mid
#             else:
#                 node = node.left
#                 right = mid
#         return node is not None
        
```

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
