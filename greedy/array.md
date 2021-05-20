### 1665. Minimum Initial Energy to Finish Tasks
```
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda a: a[1] - a[0])
        res = 0 
        # min - actual means how much you save after invest energy, if you start from largest save, 
        # you might end up spend too much energy, so start from smallest save and finish tasks
        for a, m in tasks:
            res = max(res + a, m)
        return res
```
