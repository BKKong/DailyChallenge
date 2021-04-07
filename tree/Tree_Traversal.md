
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
