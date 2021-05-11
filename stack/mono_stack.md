### 1696. Jump Game VI
```
# from collections import deque
# class Solution:
#     def maxResult(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         dp = [-math.inf] * n
#         dp[0] = nums[0]
#         queue = deque([0])
        
#         for i in range(1, n):
#             while queue and i - queue[0] > k:
#                 queue.popleft()
#             dp[i] = dp[queue[0]] + nums[i]
#             while queue and dp[i] >= dp[queue[-1]]:
#                 queue.pop()
#             queue.append(i)    
#         return dp[n - 1]
```
