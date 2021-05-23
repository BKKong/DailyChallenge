### 856. Score of Parentheses
```
# class Solution:
#     def scoreOfParentheses(self, s: str) -> int:
#         if not s:
#             return 0
#         n = len(s)
#         dp = [0] * n
#         score = [0] * n
#         for i in range(1, n):
#             if s[i] == ")" and s[i - 1] == "(":
#                 dp[i] = 2
#                 score[i] = 1
#         for i in range(1, n):
#             if s[i] == ")" and s[i - 1] == "(":
#                 if i - 2 >= 0 and s[i - 2] == ")":
#                     dp[i] = dp[i - 2] + 2
#                     score[i] = score[i - 2] + 1
#             if s[i] == ")" and s[i - 1] == ")":
#                 if s[i - dp[i - 1] - 1] == "(":
#                     dp[i] = dp[i - 1] + 2
#                     score[i] = 2 * score[i - 1]
#                 if i - dp[i - 1] - 2 >= 0 and s[i - dp[i - 1] - 2] == ")":
#                     dp[i] += dp[i - dp[i - 1] - 2]
#                     score[i] += score[i - dp[i - 1] - 2]
#         return score[n - 1]
                
                    
```
