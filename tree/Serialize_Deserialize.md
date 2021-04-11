## Serialize and Deserialize Tree

#### 331. Verify Preorder Serialization of a Binary Tree
One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as '#'.    
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where '#' represents a null node.    
Given a string of comma-separated values preorder, return true if it is a correct preorder traversal serialization of a binary tree.     
It is guaranteed that each comma-separated value in the string must be either an integer or a character '#' representing null pointer.    
You may assume that the input format is always valid.    
- Example 1:
  - Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
  - Output: true
- Example 2:
  - Input: preorder = "9,#,#,1"
  - Output: false  
```
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if not preorder:
            return True
        stack = []
        for node in preorder.split(","):
            stack.append(node)
            if len(stack) > 1 and stack[0] == "#":
                return False
            while len(stack) >= 2 and stack[-1] == "#" and stack[-2] == "#":
                stack.pop()
                stack.pop()
                if stack:
                    stack.pop()
                stack.append("#")
        return len(stack) == 1 and stack[0] == "#"
```
#### 1028. Recover a Tree From Preorder Traversal
We run a preorder depth-first search (DFS) on the root of a binary tree.    
At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.    
If a node has only one child, that child is guaranteed to be the left child.    
Given the output S of this traversal, recover the tree and return its root.    
Example:
  + Input: S = "1-2--3--4-5--6--7"
  + Output: [1,2,5,3,4,6,7]
```
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        n = len(S)
        i = 0
        stack = []
        while i < n:
            level, val = 0, 0 
            while i < n and S[i] == "-":
                level += 1
                i += 1
            while i < n and S[i] != "-":
                val = val * 10 + int(S[i])
                i += 1
            node = TreeNode(val)
            while len(stack) > level:
                stack.pop()
            if stack and stack[-1].left is None:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
```
