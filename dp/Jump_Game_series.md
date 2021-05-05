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
### 1306. Jump Game III
```
# from collections import deque
# class Solution:
#     def canReach(self, arr: List[int], start: int) -> bool:
#         if not arr:
#             return False
#         n = len(arr)
#         if arr[start] == 0:
#             return True
#         queue = deque([start])
#         visited = set([start])
#         while queue:
#             idx = queue.popleft()
#             for new_idx in [idx + arr[idx], idx - arr[idx]]:
#                 if 0 <= new_idx < n and new_idx not in visited:
#                     if arr[new_idx] == 0:
#                         return True
#                     queue.append(new_idx)
#                     visited.add(new_idx)
#         return False
```
