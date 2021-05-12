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
### 1345. Jump Game IV
```
from collections import defaultdict, deque
# class Solution:
#     def minJumps(self, arr: List[int]) -> int:
#         n = len(arr)
#         if n == 1:
#             return 0
#         val2index = defaultdict(set)
#         for i, num in enumerate(arr):
#             val2index[num].add(i)

#         queue = deque([(0, 0)])
#         visited = set([0])
#         while queue:
#             node, dist = queue.popleft()
#             if arr[node] in val2index:
#                 num_neighbors = val2index[arr[node]]
#             else:
#                 num_neighbors = set()
#             for nei in (num_neighbors | set([node + 1, node - 1])):
#                 if 0 <= nei < n and nei not in visited:
#                     if nei == n - 1:
#                         return dist + 1
#                     queue.append((nei, dist + 1))
#                     visited.add(nei)
#             if arr[node] in val2index:
#                 del val2index[arr[node]]
#         return -1                
```
### 1340. Jump Game V
```
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        res = [0] * n
        
        def dp(i):
            if res[i]:
                return res[i]
            res[i] = 1
            for di in [-1, 1]:
                for j in range(i + di, i + d * di + di, di):
                    if not (0 <= j < n and arr[j] < arr[i]):
                        break
                    res[i] = max(res[i], dp(j) + 1)
            return res[i]
        return max(map(dp, range(n)))
```
### 975. Odd Even Jump
```
# from sortedcontainers import SortedDict
# class Solution:
#     def oddEvenJumps(self, arr: List[int]) -> int:
#         n = len(arr)
#         store = SortedDict()
#         dp = [[False] * 2 for _ in range(n)]
#         dp[n - 1][0] = True
#         dp[n - 1][1] = True
#         store[arr[n - 1]] = n - 1
#         ans = 1
#         for i in range(n - 2, -1, -1):
#             next_greater = store.bisect_left(arr[i])
#             if next_greater != len(store):
#                 dp[i][0] = dp[store.peekitem(next_greater)[1]][1]
#             next_smaller = store.bisect_right(arr[i]) - 1
#             if next_smaller != -1:
#                 dp[i][1] = dp[store.peekitem(next_smaller)[1]][0]
#             store[arr[i]] = i
#             if dp[i][0]:
#                 ans += 1
#         return ans
```
