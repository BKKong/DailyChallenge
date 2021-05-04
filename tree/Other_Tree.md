## Other Tree

#### 971. Flip Binary Tree To Match Preorder Traversal 
You are given the root of a binary tree with n nodes, where each node is uniquely assigned a value from 1 to n. You are also given a sequence of n values voyage, which is the desired pre-order traversal of the binary tree.    

Any node in the binary tree can be flipped by swapping its left and right subtrees. For example, flipping node 1 will have the following effect: Flip the smallest number of nodes so that the pre-order traversal of the tree matches voyage.    

Return a list of the values of all flipped nodes. You may return the answer in any order. If it is impossible to flip the nodes in the tree to make the pre-order traversal match voyage, return the list [-1].    
- Example 1:
  - Input: root = [1,2], voyage = [2,1]
  - Output: [-1]
  - Explanation: It is impossible to flip the nodes such that the pre-order traversal matches voyage.
- Example 2:
  - Input: root = [1,2,3], voyage = [1,3,2]
  - Output: [1]
  - Explanation: Flipping node 1 swaps nodes 2 and 3, so the pre-order traversal matches voyage. 
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.flip = []
        self.i = 0
        self.n = len(voyage)
        
        def dfs(node):
            if not node:
                return 
            if node.val != voyage[self.i]:
                self.flip = [-1]
                return
            
            self.i += 1
            if self.i < self.n and node.left and node.left.val != voyage[self.i]:
                self.flip.append(node.val)
                dfs(node.right)
                dfs(node.left)
            else:
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        if self.flip and self.flip[0] == -1:
            self.flip = [-1]
        return self.flip
```

#### 1597. Build Binary Expression Tree From Infix Expression
```
# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None): 
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def expTree(self, s: str) -> 'Node':
        def build_node(op, right_node, left_node):
            return Node(op, left_node, right_node)
        def lower_precedence(curr_op, prev_op):
            if prev_op == "(":
                return False
            if curr_op in ["*", "/"] and prev_op in ["+", "-"]:
                return False
            return True
        
        n = len(s)
        nodes, ops = [], []
        for i in range(n):
            c = s[i]
            if c.isdigit():
                nodes.append(Node(c))
            elif c == "(":
                ops.append(c)
            elif c == ")":
                while ops[-1] != "(":
                    nodes.append(build_node(ops.pop(), nodes.pop(), nodes.pop()))
                ops.pop()
            else:
                while len(ops) > 0 and lower_precedence(c, ops[-1]):
                    nodes.append(build_node(ops.pop(), nodes.pop(), nodes.pop()))
                ops.append(c)
        while ops:
            nodes.append(build_node(ops.pop(), nodes.pop(), nodes.pop()))
        return nodes.pop()
```

### Tree Node Distance

### 863. All Nodes Distance K in Binary Tree
```
from collections import deque
# class Solution:
#     def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
#         if K == 0:
#             return [target.val]
#         parents = {root: None}
#         def dfs(node):
#             if not node:
#                 return
#             if node.left:
#                 parents[node.left] = node
#                 dfs(node.left)
#             if node.right:
#                 parents[node.right] = node
#                 dfs(node.right)
#         dfs(root)
#         queue = deque([(target, 0)])
#         visited = set([target])
#         ans = []
#         while queue:
#             node, dist = queue.popleft()
#             if dist == K:
#                 ans.append(node.val)
#                 for nd, d in queue:
#                     ans.append(nd.val)
#                 break
#             for neighbor in [node.left, node.right, parents[node]]:
#                 if neighbor and neighbor not in visited:
#                     queue.append((neighbor, dist + 1))
#                     visited.add(neighbor)
#         return ans
```
