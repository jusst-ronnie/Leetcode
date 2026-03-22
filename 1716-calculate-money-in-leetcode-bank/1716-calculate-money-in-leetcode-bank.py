class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        monday_value = 1
        
        # Iterate through n days
        for i in range(n):
            # i // 7 gives the week offset (0, 1, 2...)
            # i % 7 gives the day of the week offset (0, 1, 2, 3, 4, 5, 6)
            week_offset = i // 7
            day_offset = i % 7
            
            total += (monday_value + week_offset + day_offset)
            
        return total