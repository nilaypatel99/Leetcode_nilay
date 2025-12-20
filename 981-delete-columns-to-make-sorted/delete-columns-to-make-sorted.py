class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0

        for row in range(len(strs[0])):
            for col in range(1,len(strs)):
                if strs[col][row]<strs[col-1][row]:
                    res+=1
                    break

        return res


