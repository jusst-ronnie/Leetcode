class Solution:
    def minTime(self, skill, mana):
        n = len(skill)
        m = len(mana)

        prefix = [0]*n
        prefix[0] = skill[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1] + skill[i]

        start = 0

        for j in range(1, m):
            prev = start
            need = prev
            for i in range(n):
                prev_prefix = prefix[i-1] if i > 0 else 0
                need = max(need, prev + mana[j-1]*prefix[i] - mana[j]*prev_prefix)
            start = need

        return start + mana[-1]*prefix[-1]