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
### 1567. Maximum Length of Subarray With Positive Product
```
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        pos = 0
        neg = 0
        max_len = -math.inf
        for i in range(n):
            if nums[i] > 0:
                pos += 1
                if neg > 0:
                    neg += 1
            elif nums[i] < 0:
                last_pos, last_neg = pos, neg
                if last_pos > 0:
                    neg = last_pos + 1
                else:
                    neg = 1
                if last_neg > 0:
                    pos = last_neg + 1
                else:
                    pos = 0
            else:
                pos, neg = 0, 0
                
            max_len = max(max_len, pos)    
        
        if max_len > 0:
            return max_len
        return 0
```