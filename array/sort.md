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
