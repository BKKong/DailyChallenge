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
