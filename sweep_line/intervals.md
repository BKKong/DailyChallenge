### 1520. Maximum Number of Non-Overlapping Substrings
```
# class Solution:
#     def maxNumOfSubstrings(self, s: str) -> List[str]:
#         if not s:
#             return []
#         n = len(s)
#         keep = {}
#         for i, ch in enumerate(s):
#             if ch not in keep:
#                 keep[ch] = [i, i]
#             else:
#                 keep[ch][1] = i
        
#         intervals = []
#         for ch in set(s):
#             ch_start = keep[ch][0]
#             ch_end = keep[ch][1]
#             i = ch_start
#             while i < ch_end and ch_start == keep[ch][0]:
#                 ch_start = min(ch_start, keep[s[i]][0])
#                 ch_end = max(ch_end, keep[s[i]][1])
#                 i += 1
#             if ch_start == keep[ch][0]:
#                 intervals.append((ch_start, ch_end))
#         intervals = sorted(intervals, key = lambda x: (x[1], x[0]))
        
#         ans, prev_end = [], -1
#         for start, end in intervals:
#             if start > prev_end:
#                 ans.append(s[start : end + 1])
#                 prev_end = end
#         return ans
            
```
