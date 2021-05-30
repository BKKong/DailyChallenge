### 930. Binary Subarrays With Sum
```
# from collections import Counter
# class Solution:
#     def numSubarraysWithSum(self, A: List[int], S: int) -> int:
#         if sum(A) < S:
#             return 0
#         sums = [0]
#         for num in A:
#             sums.append(sums[-1] + num)
#         counter = Counter()
#         ans = 0
#         for item in sums:
#             if item - S >= 0 and item - S in counter:
#                 ans += counter[item - S]
#             counter[item] += 1
#         return ans
```
