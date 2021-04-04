class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        """        
        Edge cases:
            N = length of sweetness
            1. if K == N - 1: return min(sweetness)
            2. if K > N - 1: return -1
            3. if K == 0: sum(sweetness)
        Algo:
            binary search on possible total sweetness you can get
        Complexity:
            O( log(N * 10^5) * N )
        """
        n = len(sweetness)
        if K == n - 1:
            return min(sweetness)
        if K > n - 1:
            return -1
        if K == 0:
            return sum(sweetness)
        min_item = min(sweetness)
        left = min_item
        right = sum(sweetness)
        while left < right - 1:
            mid = (left + right) // 2
            if self.is_possible(sweetness, mid, K):
                left = mid
            else:
                right = mid
        if self.is_possible(sweetness, left, K):
            return left
        elif self.is_possible(sweetness, right, K):
            return right
        return -1
    
    def is_possible(self, sweetness, target, K):
        count = 0
        curr = 0
        for i in range(len(sweetness)):
            curr += sweetness[i]
            if curr >= target:
                count += 1
                curr = 0
                if count > K:
                    return True
        return count > K
    
            
            
