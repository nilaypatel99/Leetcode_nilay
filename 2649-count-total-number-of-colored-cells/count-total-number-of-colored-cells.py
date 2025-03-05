class Solution:
    def coloredCells(self, n: int) -> int:
        #at n=1-->1 at n=2-->5 at n=3-->13
        #at n=4-->21 at n=5-->29

        #no of blue cells added at each minute is a multiple of 4

        return 1+2*(n-1)*n