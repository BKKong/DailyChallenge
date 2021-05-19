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
### 581. Shortest Unsorted Continuous Subarray
```
# class Solution:
#     def findUnsortedSubarray(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         n = len(nums)
#         left, right = [], []
#         for i, num in enumerate(nums):
#             while left and num < nums[left[-1]]:
#                 left.pop()
#             if i == 0 or (left and i == left[-1] + 1):
#                 left.append(i)
#         if len(left) == n:
#             return 0
#         for i in reversed(range(len(nums))):
#             num = nums[i]
#             while right and num > nums[right[-1]]:
#                 right.pop()
#             if i == n - 1 or (right and i == right[-1] - 1):
#                 right.append(i)
        
#         left_start = left[-1] + 1 if left else 0
#         right_end = right[-1] - 1 if right else n - 1
#         return right_end - left_start + 1
            
```
