class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        fin = {}
        diff1 = abs(z-x)
        diff2 = abs(z-y)

        fin[1] = diff1
        fin[2] = diff2

        if diff1 == diff2:
            return 0
        else:
            res = min(fin, key = fin.get)  #O(n)
            return res