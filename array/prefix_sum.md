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
### 1442. Count Triplets That Can Form Two Arrays of Equal XOR
```
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        preXOR = []
        res = 0
        temp = 0
        for i in arr:
            temp ^= i
            preXOR.append(temp)
        
        for i in range(len(arr)):
            for k in range(i+1, len(arr)):
                if preXOR[i] ^ arr[i] == preXOR[k]:
                    res += k - i
        return res  
```
