### 1402. Reducing Dishes
```
# class Solution:
#     def maxSatisfaction(self, A: List[int]) -> int:
#         """
#             -9,     -8,     -1,     0,     5
#         0:   0       0       0      0      0
#         1:  -9      -8      -1      0      5
#         2:         -25     -10     -1     10
#         3:                 -28    -10     14
#         4:                        -28     10
#         5:                                -3
        
#         for j in range(n):
#             x = min(dp[i - 1][j])
#         dp[i][j] = x + i * A[j] 
#         """
#         if not A:
#             return 0
#         A = sorted(A)
#         n = len(A)
#         dp = [[None] * n for _ in range(n + 1)]
        
#         for j in range(n):
#             dp[0][j] = 0
        
#         for i in range(1, j + 2):
#             last_max = -math.inf
#             for j in range(n):
#                 if j + 1 < i:
#                     continue
#                 if j == 0:
#                     last_max = 0
#                 else:
#                     last_max = max(last_max, dp[i - 1][j - 1])
#                 dp[i][j] = last_max + i * A[j]
        
#         ans = 0
#         for i in range(1, n + 1):
#             ans = max(ans, dp[i][n - 1])
#         return ans
        
        
```
