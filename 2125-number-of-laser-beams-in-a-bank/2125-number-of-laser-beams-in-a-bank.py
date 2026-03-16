class Solution:
    def numberOfBeams(self, bank):
        prev = 0
        beams = 0

        for row in bank:
            devices = row.count('1')

            if devices > 0:
                beams += prev * devices
                prev = devices

        return beams