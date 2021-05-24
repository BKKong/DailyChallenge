### 179. Largest Number
```
# class Solution:
#     def largestNumber(self, nums: List[int]) -> str:
#         if not nums:
#             return ""        
#         nums_str = map(str, nums)
        
#         class Key:
#             def __init__(self, value):
#                 self._value = value
#             def __lt__(self, other):
#                 return self._value + other._value < other._value + self._value
            
#         nums_str = sorted(nums_str, key = Key, reverse = True)
#         if nums_str[0] == "0":
#             return "0"
#         return "".join(nums_str)
```
### 164. Maximum Gap
```
# class Solution:
#     def maximumGap(self, nums: List[int]) -> int:
#         for shift in range(0, 32, 8):
#             lists = [[] for _ in range(256)]
#             for num in nums:
#                 lists[(num >> shift) & 0xff].append(num)
#             nums = []
#             for l in lists:
#                 nums += l
#         return max((num2 - num1 for num1, num2 in zip(nums, nums[1:])), default=0)
```
