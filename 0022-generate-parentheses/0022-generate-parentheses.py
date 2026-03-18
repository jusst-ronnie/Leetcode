class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(current_string, open_count, close_count):
            # Base Case: If the string is complete (length is 2 * n)
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
            
            # Rule 1: We can always add an '(' if we haven't used up all n
            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count)
            
            # Rule 2: We can only add a ')' if it won't make the string invalid
            # This happens when there are more '(' than ')' currently in the string
            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1)
        
        # Start the recursion with an empty string and 0 counts
        backtrack("", 0, 0)
        return result