class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        answer = [0] * n
        stack = [] # This will be a monotonic decreasing stack (from bottom to top)
        
        # Process from right to left
        for i in range(n - 1, -1, -1):
            count = 0
            
            # While the current person is taller than the person on the stack
            # they can see that person, and that person will be hidden 
            # from anyone further to the left.
            while stack and heights[i] > stack[-1]:
                stack.pop()
                count += 1
            
            # If there is still someone on the stack, the current person 
            # can see them too (this is the first person taller than them).
            if stack:
                count += 1
            
            answer[i] = count
            stack.append(heights[i])
            
        return answer