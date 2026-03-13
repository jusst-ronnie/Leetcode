class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        
        def can_finish(T):
            total = 0
            
            for w in workerTimes:
                left, right = 0, mountainHeight
                
                while left <= right:
                    mid = (left + right) // 2
                    
                    if w * mid * (mid + 1) // 2 <= T:
                        left = mid + 1
                    else:
                        right = mid - 1
                
                total += right
                
                if total >= mountainHeight:
                    return True
            
            return False
        
        left, right = 1, 10**18
        
        while left < right:
            mid = (left + right) // 2
            
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1
        
        return left