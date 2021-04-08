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
