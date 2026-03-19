import random

class Solution:

    def __init__(self, nums):
        self.map = {}
        
        for i, num in enumerate(nums):
            if num not in self.map:
                self.map[num] = []
            self.map[num].append(i)

    def pick(self, target):
        return random.choice(self.map[target])