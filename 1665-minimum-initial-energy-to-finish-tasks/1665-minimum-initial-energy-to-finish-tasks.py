class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        # Sort tasks by the difference (minimum - actual) in descending order
        # This prioritizes tasks that require more "overhead" energy first.
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        
        current_energy = 0
        total_initial_energy = 0
        
        for actual, minimum in tasks:
            # If current energy is less than the minimum required to start
            if current_energy < minimum:
                # Add the deficit to our total initial energy pool
                total_initial_energy += (minimum - current_energy)
                # After adding deficit, our current energy becomes exactly 'minimum'
                current_energy = minimum
            
            # Spend the actual energy required for the task
            current_energy -= actual
            
        return total_initial_energy
