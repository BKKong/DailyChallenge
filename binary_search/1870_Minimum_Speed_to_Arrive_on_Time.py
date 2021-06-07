class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        if hour < n - 1:
            return -1
        left = 1
        r1 = max(dist) + 1
        if hour - n + 1 != 0.0: 
            r2 = math.ceil(dist[-1] / (hour - n + 1)) + 1
        else:
            r2 = -math.inf
        right = max(r1, r2)
        #print(math.ceil(dist[-1] / (hour - n + 1)) + 1)
        #print(left, right)
        while left < right - 1:
            mid = (left + right) // 2
            if self.check(mid, dist, hour):
                right = mid
            else:
                left = mid
        #print(left)
        if self.check(left, dist, hour):
            return left
        elif self.check(right, dist, hour):
            return right
        return -1
        
    def check(self, speed, dist, hour):
        count = 0
        for i in range(len(dist) - 1):
            d = dist[i]
            if d % speed != 0:
                count += d // speed + 1
            else:
                count += d // speed
        count += dist[-1] / speed
        return count <= hour
