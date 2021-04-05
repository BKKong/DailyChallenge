#### 774. Minimize Max Distance to Gas Station

You are given an integer array stations that represents the positions of the gas stations on the x-axis. You are also given an integer k.

You should add k new gas stations. You can add the stations anywhere on the x-axis, and not necessarily on an integer position.

Let penalty() be the maximum distance between adjacent gas stations after adding the k new stations.

Return the smallest possible value of penalty(). Answers within 10-6 of the actual answer will be accepted.

Example:
  Input: stations = [23,24,36,39,46,56,57,65,84,98], k = 1   
  Output: 14.00000
```
import math
class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        max_dist = -math.inf
        dists = []
        n = len(stations)
        for i in range(n - 1):
            dist = stations[i + 1] - stations[i]
            dists.append(dist)
            max_dist = max(dist, max_dist)
        left = 0
        right = max_dist
        while left < right - 5e-7:
            mid = (left + right) / 2
            if self.is_possible(mid, k, stations, dists):
                right = mid
            else:
                left = mid
        return left                                        ### Bug: `if self.is_possible(left, k, stations, dists): return left`
                                                           ### 二分答案不需要再验证条件是否成立
    def is_possible(self, delta, k, stations, dists):
        st_to_add = 0
        for i in range(len(stations) - 1):
            st_to_add += math.ceil(dists[i] / delta) - 1   ### Bug: st_to_add += int(dists[i] / delta) 如果 1 / 0.5 = 2, 实际要加两个点？不对
        return st_to_add <= k
        
```
