class Solution:
    def specialArray(self, nums: List[int]) -> int:
        if not nums:
            return -1
        nums = sorted(nums)
        left, right = 1, max(nums) + 1
        while left < right - 1:
            mid = (left + right) // 2
            if self.check(nums, mid):
                left = mid
            else:
                right = mid
                
        if self.check_equal(nums, left):
            return left
        elif self.check_equal(nums, right):
            return right
        return -1
    
    def check(self, nums, times):
        idx1 = bisect_left(nums, times)
        idx2 = bisect_right(nums, times)
        # times does not exist in nums
        if idx1 == idx2:
            return len(nums) - idx2 >= times
        else:
            return len(nums) - idx1 >= times
        
    def check_equal(self, nums, times):
        idx1 = bisect_left(nums, times)
        idx2 = bisect_right(nums, times)
        # times does not exist in nums
        if idx1 == idx2:
            return len(nums) - idx2 == times
        else:
            return len(nums) - idx1 == times
