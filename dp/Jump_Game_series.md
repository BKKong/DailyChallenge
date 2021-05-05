### 55. Jump Game
```
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         if not nums:
#             return False
#         m = len(nums)
#         far = nums[0]
#         for i in range(m):
#             if i > far:
#                 break
#             else:
#                 far = max(far, i + nums[i])
#                 if far >= m - 1:
#                     return True
#         return far >= m - 1
```
### 45. Jump Game II
```
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [math.inf] * n
#         dp[0] = 0
#         for i in range(n):
#             for j in range(nums[i]):
#                 if i + j + 1 < n:
#                     dp[i + j + 1] = min(dp[i + j + 1], dp[i] + 1)
#         return dp[n - 1]
```
