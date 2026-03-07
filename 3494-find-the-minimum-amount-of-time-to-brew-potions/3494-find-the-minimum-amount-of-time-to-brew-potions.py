class Solution:
    def minTime(self, skill, mana):
        n = len(skill)
        m = len(mana)

        # prefix sums of skill
        prefix = [0]*n
        prefix[0] = skill[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1] + skill[i]

        finish = [0]*n

        for j in range(m):
            start = finish[0]

            for i in range(1,n):
                start = max(start, finish[i] - mana[j]*prefix[i-1])

            cur = start
            for i in range(n):
                cur += skill[i]*mana[j]
                finish[i] = cur

        return finish[-1]