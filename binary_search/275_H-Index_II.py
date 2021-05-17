class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        left, right = 0, citations[-1] + 1
        while left < right - 1:
            mid = (left + right) // 2
            if self.check(mid, citations):
                left = mid
            else:
                right = mid
        if self.check(left, citations):
            return left
        return 1
    
    def check(self, num, citations):
        n = len(citations)
        idx = bisect_left(citations, num)
        return n - idx >= num
