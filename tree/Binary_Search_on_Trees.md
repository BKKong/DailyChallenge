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
