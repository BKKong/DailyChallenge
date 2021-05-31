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
### 241. Different Ways to Add Parentheses
```
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        n = len(expression)
        ans = []
        for i in range(n):
            if expression[i] in ["+", "-", "*"]:
                part1 = self.diffWaysToCompute(expression[:i])
                part2 = self.diffWaysToCompute(expression[i + 1:])
                for num1 in part1:
                    for num2 in part2:
                        if expression[i] == "+":
                            ans.append(num1 + num2)
                        elif expression[i] == "-":
                            ans.append(num1 - num2)
                        else:
                            ans.append(num1 * num2)
        if not ans:
            ans.append(int(expression))
        return ans
```
