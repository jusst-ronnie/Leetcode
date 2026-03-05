from bisect import bisect_right

class Solution:
    def avoidFlood(self, rains):
        last_rain = {}
        dry_days = []
        ans = [-1] * len(rains)

        for i, lake in enumerate(rains):
            
            if lake == 0:
                dry_days.append(i)
                ans[i] = 1
            else:
                if lake in last_rain:
                    
                    idx = bisect_right(dry_days, last_rain[lake])
                    
                    if idx == len(dry_days):
                        return []
                    
                    dry_day = dry_days[idx]
                    ans[dry_day] = lake
                    dry_days.pop(idx)
                
                last_rain[lake] = i
                ans[i] = -1

        return ans