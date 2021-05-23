### 301. Remove Invalid Parentheses
```
# class Solution:
#     def removeInvalidParentheses(self, s: str) -> List[str]:
#         left, right = 0, 0
#         for ch in s:
#             if ch == "(":
#                 left += 1
#             elif ch == ")":
#                 if left == 0:
#                     right += 1
#                 else:
#                     left -= 1
#         self.ans = []
#         self.dfs(s, 0, left, right)
#         return self.ans
    
#     def dfs(self, s, start, left, right):
#         if left == 0 and right == 0 and self.is_valid(s):
#             self.ans.append(s)
#             return
        
#         for i in range(start, len(s)):
#             if i != start and s[i] == s[i - 1]:
#                 continue
#             if s[i] == "(" or s[i] == ")":
#                 curr = s[:i] + s[i + 1:]
#                 if right > 0 and s[i] == ")":
#                     self.dfs(curr, i, left, right - 1)
#                 elif left > 0 and s[i] == "(":
#                     self.dfs(curr, i, left - 1, right)
    
#     def is_valid(self, string):
#         count = 0
#         for ch in string:
#             if ch == "(":
#                 count += 1
#             elif ch == ")":
#                 count -= 1
#                 if count < 0:
#                     return False
#         return count == 0
```
