### 105. Construct Binary Tree from Preorder and Inorder Traversal
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder and not inorder:
            return None
        self.preorder = preorder
        self.inorder = inorder
        self.lookup = {}
        for i, val in enumerate(inorder):
            self.lookup[val] = i
        n = len(preorder)
        return self.build(0, n, 0, n)
    
    def build(self, pre_start, pre_len, in_start, in_len):
        if pre_len == 0:
            return None
        root_val = self.preorder[pre_start]
        i = self.lookup[root_val]
        left_tree_size = i - in_start
        right_tree_size = in_len - left_tree_size - 1
        root = TreeNode(root_val)
        root.left = self.build(pre_start + 1, left_tree_size, in_start, left_tree_size)
        root.right = self.build(pre_start + 1 + left_tree_size, right_tree_size, i + 1, right_tree_size)
        return root
```

### 106. Construct Binary Tree from Inorder and Postorder Traversal
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.
```
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder and not postorder:
            return None
        m = len(inorder)
        root_val = postorder[-1]
        root = TreeNode(root_val)
        for i, v in enumerate(inorder):
            if v == root_val:
                left_tree_len = i 
                right_tree_len = m - i - 1
                root.left = self.buildTree(inorder[:i], postorder[:i])
                root.right = self.buildTree(inorder[i + 1:], postorder[i: m - 1])
        return root
```
